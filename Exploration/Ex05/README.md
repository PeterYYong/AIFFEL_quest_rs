# AIFFEL Campus Online Code Peer Review Templete
- 코더 : 김용석
- 리뷰어 : 이예지

# PRT(Peer Review Template)
- [V]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - 다양한 방법으로 Text Classification 태스크 구현
    - LSTM 모델 이용하여 감성분석 정확도 85% 이상 달성
    - gensim 임베딩 레이어 분석은 진행 중 이십니다.
    - ![image](https://github.com/user-attachments/assets/37bd2c20-6b17-488f-9097-0b1cc6e27f78)
    - ![image](https://github.com/user-attachments/assets/44421c0b-7aeb-408e-9a30-f3145127c273)
    - ![image](https://github.com/user-attachments/assets/6652c5d9-b7b7-4a4f-af3b-1902898c2115)

    
- [V]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - 
    ![image](https://github.com/user-attachments/assets/a62c468e-137a-43dc-b984-d0967a1be912)
    - Mecab을 이용하여 형태소 분석을 진행하고, 중복 제거, 결측치 제거, 문장 토큰화 및 불용어 제거, 훈련 데이터 및 테스트 데이터 전처리, 단어빈도계산, 사전 생성, 텍스트를 문자 시퀀스로 변환 의 과정을 거쳐 결과를 반환하여 word_to_index 딕셔너리를 생성하였습니다. 이 코드는 한글 자연어를 임베딩하기 위한 필수적인 작업이며, 어려운 부분이지만 용석님의 코드를 보고 잘 이해할 수 있었습니다.

        
- [V]  **3. 에러가 난 부분을 디버깅하여 문제를 해결한 기록을 남겼거나
새로운 시도 또는 추가 실험을 수행해봤나요?**
    - 용석님께서는 각 모델에 대해 Loss, Accuracy를 나타내는 그래프를 plot하여 문제가 생긴 부분을 확인하셨습니다.
![image](https://github.com/user-attachments/assets/092d0272-10b7-4300-9bff-a76b13ed4878)
LSTM 외에 Conv1D, Globalmaxpooling 1D 모델에서 각 그래프의 양상을 확인하시고 재실험을 진행하고 있습니다.
또한 오류가 나지는 않았지만, LSTM 외에 Conv1D, Globalmaxpooling 1D 모델에서 어휘사전의 크기를 잘못 설정한 것을 확인하셔서 재실행을 진행하고 있습니다.

        
- [V]  **4. 회고를 잘 작성했나요?**
      - 회고가 잘 작성되어 있습니다.
        ![image](https://github.com/user-attachments/assets/f0563037-5b4a-4456-80d1-357c21eb99c8)

- [V]  **5. 코드가 간결하고 효율적인가요?**
    - ![image](https://github.com/user-attachments/assets/c18accdf-5f88-4321-932a-cbedf05572e9)

코드가 간결하게 잘 작성되어 있습니다.

# 회고(참고 링크 및 코드 개선)
```
![image](https://github.com/user-attachments/assets/ff59ff19-dd7a-4ac9-b0bf-45f881a2e6c9)
용석님의 코드를 샅샅이 살펴보며 저도 많이 배울 수 있었던시간이었습니다!!!! 한글 깨짐을 해결하는 코드를 작성해주셔서 좋은 참고자료로 볼 수 있었어요! 오늘 저녁 안으로 작성하고 디스코드로 전달드리도록 하겠습니다!! 




```
