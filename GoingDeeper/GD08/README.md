# AIFFEL Campus Online Code Peer Review Templete
- 코더 : 깅용석
- 리뷰어 : 황동주


# PRT(Peer Review Template)
- [O]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - 문제에서 요구하는 최종 결과물이 첨부되었는지 확인
        - 중요! 해당 조건을 만족하는 부분을 캡쳐해 근거로 첨부
        ![image](https://github.com/user-attachments/assets/e523d433-468d-4815-825a-a20097ee77e3)  
        - tfrecord 가 구성 됨
      
        ![image](https://github.com/user-attachments/assets/5139e405-4610-406d-8816-1df4f4277970)  
        ![image](https://github.com/user-attachments/assets/8a967b28-dcb4-4cc9-be10-8f8f3be34c7c)  
        - SimpleBaseline 모델 구현 및 학습 완료 됨
    
- [O]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - 해당 코드 블럭을 왜 핵심적이라고 생각하는지 확인
    - 해당 코드 블럭에 doc string/annotation이 달려 있는지 확인
    - 해당 코드의 기능, 존재 이유, 작동 원리 등을 기술했는지 확인
    - 주석을 보고 코드 이해가 잘 되었는지 확인
        - 중요! 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부
        ![image](https://github.com/user-attachments/assets/9a510c79-d02a-4593-8b71-adb8a9e008b7)
        - 모델 구현 부 주석 및 함수 정의 확인 됨
        
- [O]  **3. 에러가 난 부분을 디버깅하여 문제를 해결한 기록을 남겼거나
새로운 시도 또는 추가 실험을 수행해봤나요?**
    - 문제 원인 및 해결 과정을 잘 기록하였는지 확인
    - 프로젝트 평가 기준에 더해 추가적으로 수행한 나만의 시도, 
    실험이 기록되어 있는지 확인
        - 중요! 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부
        ![image](https://github.com/user-attachments/assets/1353872d-583a-4886-a985-4f82e3f096ac)
        - SimpleBaseline 모델 학습 손실 계산 함수 과정이 기록 됨

        
- [O]  **4. 회고를 잘 작성했나요?**
    - 주어진 문제를 해결하는 완성된 코드 내지 프로젝트 결과물에 대해
    배운점과 아쉬운점, 느낀점 등이 기록되어 있는지 확인
    - 전체 코드 실행 플로우를 그래프로 그려서 이해를 돕고 있는지 확인
        - 중요! 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부
        ![image](https://github.com/user-attachments/assets/9575946b-fb36-4885-a54f-b87e7398cf00)
        - 회고 기록 됨

        
- [O]  **5. 코드가 간결하고 효율적인가요?**
    - 파이썬 스타일 가이드 (PEP8) 를 준수하였는지 확인
    - 코드 중복을 최소화하고 범용적으로 사용할 수 있도록 함수화/모듈화했는지 확인
        - 중요! 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부
        ![image](https://github.com/user-attachments/assets/8930d2c9-1010-495b-ab2f-acc5a7298311)
        ![image](https://github.com/user-attachments/assets/2958afea-de79-432d-aae0-3057ea4f54a2)
        - 함수 모듈 화 및 효율적인 코드 작성 됨




# 회고(참고 링크 및 코드 개선)
```
# 리뷰어의 회고를 작성합니다.
# 코드 리뷰 시 참고한 링크가 있다면 링크와 간략한 설명을 첨부합니다.
# 코드 리뷰를 통해 개선한 코드가 있다면 코드와 간략한 설명을 첨부합니다.
```
- 코드 구현 부분의 자세한 주석처리로 이해하는데 도움이 되었습니다.
- SimpleBaseline 의 ResNet block 을 직접 구현한 부분이 인상적이였습니다.
- 30 epoch 으로 실험 진행하셔서 결과를 확인 하신점 좋았습니다.
- 수고하셨습니다.
