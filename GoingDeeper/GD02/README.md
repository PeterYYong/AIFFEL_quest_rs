# AIFFEL Campus Online Code Peer Review Templete
- 코더 : 김용석
- 리뷰어 : 윤수영


# PRT(Peer Review Template)
- [O]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - 문제에서 요구하는 최종 결과물이 첨부되었는지 확인
        - 중요! 해당 조건을 만족하는 부분을 캡쳐해 근거로 첨부
          
          
        - 아래 사진과 같이 각 모델의 결과 그래프를 출력하였으며, 이를 회고를 통해 비교 분석 하였음
        - ![image](https://github.com/user-attachments/assets/c257655c-bd5e-486f-a4ef-a9c9fc499509)
        - ![image](https://github.com/user-attachments/assets/c7ee7bbe-80f1-4dc6-86d1-a63c238b83ff)
        - ![image](https://github.com/user-attachments/assets/0836e28f-fc0e-4cc0-b577-e564c92fe074)

    
- [O]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - 해당 코드 블럭을 왜 핵심적이라고 생각하는지 확인
    - 해당 코드 블럭에 doc string/annotation이 달려 있는지 확인
    - 해당 코드의 기능, 존재 이유, 작동 원리 등을 기술했는지 확인
    - 주석을 보고 코드 이해가 잘 되었는지 확인
        - 중요! 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부
          
          
        - 아래와 같이 특정 기능을 수행하는 코드가 모두 설명과 함께 작성되어 있어 이해에 용이함
        - 이미지를 normalization하고 augmentation, cutmix, mixup을 하는 함수
        - ![image](https://github.com/user-attachments/assets/d284d73f-73ba-446a-a4b5-33c0548f021d)
        - 모델을 학습하고, 저장하고, 저장된 모델을 불러와 재학습하는 함수

        - ![image](https://github.com/user-attachments/assets/0765e3a6-964b-4760-b817-0073bdcf4744)

        
- [O]  **3. 에러가 난 부분을 디버깅하여 문제를 해결한 기록을 남겼거나
새로운 시도 또는 추가 실험을 수행해봤나요?**
    - 문제 원인 및 해결 과정을 잘 기록하였는지 확인
    - 프로젝트 평가 기준에 더해 추가적으로 수행한 나만의 시도, 
    실험이 기록되어 있는지 확인
        - 중요! 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부
          
          
        - 아래 사진과 같이 에러가 난 코드를 보존하여 두었으며, 주석을 통해 수정된 코드를 확인할 수 있음
        - 수정전
        - ![image](https://github.com/user-attachments/assets/73dd1b3d-3223-460f-bcfc-3ecdc8c774d4)
        - 수정후
        - ![image](https://github.com/user-attachments/assets/a14210ba-0b71-4e20-bee1-910e886db439)


        
- [O]  **4. 회고를 잘 작성했나요?**
    - 주어진 문제를 해결하는 완성된 코드 내지 프로젝트 결과물에 대해
    배운점과 아쉬운점, 느낀점 등이 기록되어 있는지 확인
    - 전체 코드 실행 플로우를 그래프로 그려서 이해를 돕고 있는지 확인
        - 중요! 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부
          
          
        - 아래 사진과 같이 전체 회고를 잘 작성하여 두었음
        - ![image](https://github.com/user-attachments/assets/0836e28f-fc0e-4cc0-b577-e564c92fe074)

        
- [O]  **5. 코드가 간결하고 효율적인가요?**
    - 파이썬 스타일 가이드 (PEP8) 를 준수하였는지 확인
    - 코드 중복을 최소화하고 범용적으로 사용할 수 있도록 함수화/모듈화했는지 확인
        - 중요! 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부
          
          
        - 함수를 이용하여 자동화를 많이 해 두었으며, 아래 그림과 같이 효율적이고 간결하게 사용이 가능하도록 하였음
        - 데이터를 import하고 전처리 및 증강을 수행하는 함수를 이용하는 부분
        - ![image](https://github.com/user-attachments/assets/df96de94-ac05-4c3d-b5cc-35a00953ff7e)
        - 데이터들를 이용해서 모델을 학습시키는 함수를 이용하는 부
        - ![image](https://github.com/user-attachments/assets/dc7a0d78-e194-4f5c-bd44-0f501b7fc32a)



# 회고(참고 링크 및 코드 개선)
```
# 리뷰어의 회고를 작성합니다.
# 코드 리뷰 시 참고한 링크가 있다면 링크와 간략한 설명을 첨부합니다.
# 코드 리뷰를 통해 개선한 코드가 있다면 코드와 간략한 설명을 첨부합니다.
```
- 프로젝트 고생많으셨습니다!! 추가 실험도 잘 진행되길 바랍니다.
- 회고에 작성해주신 논문 내용 잘 읽었습니다. 저도 가능하면 읽어보고 구현 할 수 있다면, 도전해보겠습니다.
- 추가적으로, 저는 아직 cutmix와 mixup의 차이에 대하여 구분 및 평가가 어려운데, 용석님께서 올려주신 자료가 좋은 참고가 될것 같습니다.
- 차후 가능하다면 추가 탐구한 부분을 공유하는 시간을 가질 수 있으면 좋을 것 같습니다!
