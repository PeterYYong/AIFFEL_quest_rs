#!/usr/bin/env python
# coding: utf-8

# # 0.  사용환경 설정

# In[98]:


import matplotlib.pyplot as ptt  
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', "InlineBackend.figure_format='retina'")


# In[99]:


import xgboost
import lightgbm
import missingno
import sklearn

print(xgboost.__version__)
print(lightgbm.__version__)
print(missingno.__version__)
print(sklearn.__version__)


# ### packages load

# In[100]:


import warnings
warnings.filterwarnings("ignore")  # Suppress general warnings
warnings.filterwarnings("ignore", category=FutureWarning)  # Suppress FutureWarnings

# OS and path handling
import os
from os.path import join

# Data manipulation and visualization
import pandas as pd  # For data manipulation
import numpy as np  # For numerical operations
import missingno as msno  # For visualizing missing data
import matplotlib.pyplot as plt  # For plotting
import seaborn as sns  # For enhanced data visualization

# Machine learning models and tools
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor, StackingRegressor  # Ensemble models
from sklearn.model_selection import KFold, cross_val_score, train_test_split, RandomizedSearchCV  # Model selection and evaluation
from sklearn.preprocessing import StandardScaler  # For feature scaling
from sklearn.feature_selection import SelectKBest, f_regression  # For feature selection
from sklearn.decomposition import PCA  # For dimensionality reduction
from sklearn.metrics import mean_squared_error  # For regression evaluation

# Specialized libraries for gradient boosting
import xgboost as xgb  # XGBoost library
import lightgbm as lgb  # LightGBM library
from xgboost import XGBRegressor  # XGBoost Regressor
from lightgbm import LGBMRegressor  # LightGBM Regressor

# Statistical tools
from scipy.stats import randint, uniform  # For defining distributions in hyperparameter tuning



# ### 파일 경로 설정

# In[101]:


data_dir = "~/aiffel/kaggle_kakr_housing/data"
# hint : os.getenv를 사용하거나 직접 경로를 작성

train_data_path = join(data_dir, 'train.csv')
sub_data_path = join(data_dir, 'test.csv')      # 테스트, 즉 submission 시 사용할 데이터 경로

print(train_data_path)
print(sub_data_path)


# In[102]:


data = pd.read_csv(train_data_path)
sub = pd.read_csv(sub_data_path)
print('train data dim : {}'.format(data.shape))
print('sub data dim : {}'.format(sub.shape))


# ### 데이터 살펴보기
# 
# pandas의 read_csv 함수를 사용해 데이터를 읽어오고, 각 변수들이 나타내는 의미를 살펴보겠습니다.
# 1. ID : 집을 구분하는 번호
# 2. date : 집을 구매한 날짜
# 3. price : 타겟 변수인 집의 가격
# 4. bedrooms : 침실의 수
# 5. bathrooms : 침실당 화장실 개수
# 6. sqft_living : 주거 공간의 평방 피트
# 7. sqft_lot : 부지의 평방 피트
# 8. floors : 집의 층 수
# 9. waterfront : 집의 전방에 강이 흐르는지 유무 (a.k.a. 리버뷰)
# 10. view : 집이 얼마나 좋아 보이는지의 정도
# 11. condition : 집의 전반적인 상태
# 12. grade : King County grading 시스템 기준으로 매긴 집의 등급
# 13. sqft_above : 지하실을 제외한 평방 피트
# 14. sqft_basement : 지하실의 평방 피트
# 15. yr_built : 집을 지은 년도
# 16. yr_renovated : 집을 재건축한 년도
# 17. zipcode : 우편번호
# 18. lat : 위도
# 19. long : 경도
# 20. sqft_living15 : 2015년 기준 주거 공간의 평방 피트(집을 재건축했다면, 변화가 있을 수 있음)
# 21. sqft_lot15 : 2015년 기준 부지의 평방 피트(집을 재건축했다면, 변화가 있을 수 있음)

# In[103]:


train_len = len(data)
data = pd.concat((data, sub), axis=0)


# In[104]:


train_data_path = f"{data_dir}/train.csv"
test_data_path = f"{data_dir}/test.csv"

# Load the datasets
train = pd.read_csv(train_data_path)
test = pd.read_csv(test_data_path)

# Checking structure and initial rows of the training data
train_info = train.info()  # Structure and data types
train_head = train.head()  # Display first few rows

# Checking for missing values in each column
missing_values = train.isnull().sum()

train_info, train_head, missing_values


# In[105]:


data.head()


# ## 2. 간단한 전처리 
# 각 변수들에 대해 결측 유무를 확인하고, 분포를 확인해보면서 간단하게 전처리를 하겠습니다.
# ### 결측치 확인
# 먼저 데이터에 결측치가 있는지를 확인하겠습니다.<br>
# missingno 라이브러리의 matrix 함수를 사용하면, 데이터의 결측 상태를 시각화를 통해 살펴볼 수 있습니다.

# In[106]:


msno.matrix(data)


# 모든 변수에 결측치가 없는 것으로 보이지만, 혹시 모르니 확실하게 살펴보겠습니다.<br>

# In[107]:


for c in data.columns:
    print('{} : {}'.format(c, len(data.loc[pd.isnull(data[c]), c].values)))


# ### id, date 변수 정리
# id 변수는 모델이 집값을 예측하는데 도움을 주지 않으므로 제거합니다.<br>
# date 변수는 연월일시간으로 값을 가지고 있는데, int 변수로 만들겠습니다.

# In[108]:


sub_id = data['id'][train_len:]
del data['id']
data['date'] = data['date'].apply(lambda x : str(x[:6])).astype(int)


# In[109]:


display(data.head())
print(data.info())


# ## 1. 기술 통계 및 데이터 정규화
# 
# ### 각 변수들의 분포 확인
# 한쪽으로 치우친 분포는 모델이 결과를 예측하기에 좋지 않은 영향을 미치므로 다듬어줄 필요가 있습니다.

# In[110]:


fig, ax = plt.subplots(10, 2, figsize=(20, 60))

# id 변수는 제외하고 분포를 확인합니다.
count = 0
columns = data.columns
for row in range(10):
    for col in range(2):
        sns.kdeplot(data=data[columns[count]], ax=ax[row][col])
        ax[row][col].set_title(columns[count], fontsize=15)
        count+=1
        if count == 19 :
            break


# price, bedrooms, sqft_living, sqft_lot, sqft_above, sqft_basement 변수가 한쪽으로 치우친 경향을 보였습니다.<br>
# log-scaling을 통해 데이터 분포를 정규분포에 가깝게 만들어 보겠습니다.

# In[111]:


skew_columns = ['bedrooms', 'sqft_living', 'sqft_lot', 'sqft_above', 'sqft_basement']

for c in skew_columns:
    data[c] = np.log1p(data[c].values)


# In[112]:


fig, ax = plt.subplots(3, 2, figsize=(10, 15))

count = 0
for row in range(3):
    for col in range(2):
        if count == 5:
            break
        sns.kdeplot(data=data[skew_columns[count]], ax=ax[row][col])
        ax[row][col].set_title(skew_columns[count], fontsize=15)
        count+=1


# 어느정도 치우침이 줄어든 분포를 확인할 수 있습니다.

# ### 가격분포 확인 및 변수간 상관관계 분석

# In[113]:


# Step 3: Summary statistics for numerical columns in train dataset
train_description = train.describe()

# Step 4: Distribution of target variable (price) visualization
plt.figure(figsize=(10, 6))
sns.histplot(train['price'], kde=True)
plt.title('Distribution of House Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

train_description


# ### 상관관계 분석
# - 가격'과의 상위 상관관계는 sqft_living(0.70), grade(0.67), sqft_above(0.61), **sqft_living15(0.59)**입니다. , **욕실(0.53)**, **우편번호`**는 약한 음의 상관관계(-0.05)를 나타냅니다
# 

# In[114]:


# Step 5: Correlation analysis for numerical features
correlation_matrix = train.corr()

# Plotting the correlation heatmap
plt.figure(figsize=(14, 10))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix for Numerical Features')
plt.show()

# Display top correlations with 'price'
price_correlation = correlation_matrix['price'].sort_values(ascending=False)
price_correlation


# In[117]:


print("데이터 타입 확인:")
print(train.dtypes)


# In[118]:


train.head()


# In[94]:


X = data.drop('price', axis = 1)
y = data['price']

random_state = 526

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2,
                                                    random_state = random_state)
print(X_train.shape, X_test.shape)
print(y_train.shape, y_test.shape)


# # preprocessing
# ## scaling

# In[95]:


# 1. 결측값(NaN) 확인 및 처리
print("결측값 확인:")
print(train.isnull().sum())  # 각 열에 있는 결측값 개수 출력

# 결측값이 있다면 0으로 채우거나 평균/중간값으로 채우기 (필요에 따라 선택)
train = train.fillna(train.mean())

# 2. 무한대 값(inf) 및 너무 큰 값 확인 및 처리
# 무한대 값과 큰 값을 np.nan으로 변환한 후 다시 평균으로 채움
train = train.replace([np.inf, -np.inf], np.nan)
train = train.fillna(train.mean())


# In[66]:


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# In[75]:


selector = SelectKBest(score_func=f_regression, k=10)
X_train_selected = selector.fit_transform(X_train_scaled, y_train)
X_test_selected = selector.transform(X_test_scaled)


# In[67]:


pca = PCA(n_components=0.95)
X_train_pca = pca.fit_transform(X_train_selected)
X_test_pca = pca.transform(X_test_selected)


# ## 3. 모델링
# ### Average Blending
# 여러가지 모델의 결과를 산술 평균을 통해 Blending 모델을 만들겠습니다.

# ### Cross Validation
# 교차 검증을 통해 모델의 성능을 간단히 평가하겠습니다.

# ### Make Submission

# 회귀 모델의 경우에는 cross_val_score 함수가 R<sup>2</sup>를 반환합니다.<br>
# R<sup>2</sup> 값이 1에 가까울수록 모델이 데이터를 잘 표현함을 나타냅니다. 3개 트리 모델이 상당히 훈련 데이터에 대해 괜찮은 성능을 보여주고 있습니다.<br> 훈련 데이터셋으로 3개 모델을 학습시키고, Average Blending을 통해 제출 결과를 만들겠습니다.
