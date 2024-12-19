# AIFFEL Campus Online Code Peer Review Templete
- 코더 : 김용석
- 리뷰어 : 윤수영


# PRT(Peer Review Template)
- [O]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - 문제에서 요구하는 최종 결과물이 첨부되었는지 확인
        - 중요! 해당 조건을 만족하는 부분을 캡쳐해 근거로 첨부
          
          
        - 아래 산진과 같이 루브릭에서 요구하는 사항을 모두 만족했음
        - 뿐만아니라 bounding box가 기울어진 것을 보정하여 ioU지표가 신뢰 가능하도록 하였음음
        - 또한 모든 레이어에서 gard-cam featur map을 활성화하여 출력하였음
        - ![image](https://github.com/user-attachments/assets/13690604-8a3d-4b2d-9dc6-85e2416d8c7f)
        - ![image](https://github.com/user-attachments/assets/f3e1cce0-00a7-40b3-883c-a7051d63b273)
        - ![image](https://github.com/user-attachments/assets/8031c90f-af17-4514-ad51-ac908f2627b5)
        - ![image](https://github.com/user-attachments/assets/60ed182a-9a20-41fc-9f59-cd91554f7fc7)
        - ![image](https://github.com/user-attachments/assets/cfc75c4f-cce0-4e5c-9ccc-441c3f576e18)
        - ![image](https://github.com/user-attachments/assets/eae69fd1-6980-4a16-89fd-817123a9ee78)
          
    
- [O]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - 해당 코드 블럭을 왜 핵심적이라고 생각하는지 확인
    - 해당 코드 블럭에 doc string/annotation이 달려 있는지 확인
    - 해당 코드의 기능, 존재 이유, 작동 원리 등을 기술했는지 확인
    - 주석을 보고 코드 이해가 잘 되었는지 확인
        - 중요! 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부
          
          
        - 아래 사진과 같이 주석을 매우 잘 작성하여, 코드의 이해를 도왔음
        - ![image](https://github.com/user-attachments/assets/0be0cfa2-3fbc-4954-91a5-39e55784c863)
        - ![image](https://github.com/user-attachments/assets/6eb5a8a9-64e9-4531-93c9-20f355eb545a)
        - ![image](https://github.com/user-attachments/assets/6ec25df7-abf3-46a6-b8fd-4cba709adf96)
        - ![image](https://github.com/user-attachments/assets/2f1c427b-b903-4ddc-adcf-b3498313790d)
          
        
- [O]  **3. 에러가 난 부분을 디버깅하여 문제를 해결한 기록을 남겼거나
새로운 시도 또는 추가 실험을 수행해봤나요?**
    - 문제 원인 및 해결 과정을 잘 기록하였는지 확인
    - 프로젝트 평가 기준에 더해 추가적으로 수행한 나만의 시도, 
    실험이 기록되어 있는지 확인
        - 중요! 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부
          
          
        - 아래 사진과 같이 문제 상황을 확실하게 정의하고, 이후 코드에서 문제를 해결하였음음
        - ![image](https://github.com/user-attachments/assets/a8ee6488-2648-4296-b88a-bcf8a7b196a9)
          
          
        - ACL 모델을 이용하여 추가 실험을 진행하였음
        - ![image](https://github.com/user-attachments/assets/c1e41f03-9ba1-4a1c-94fa-6974658af60d)
          
        
- [O]  **4. 회고를 잘 작성했나요?**
    - 주어진 문제를 해결하는 완성된 코드 내지 프로젝트 결과물에 대해
    배운점과 아쉬운점, 느낀점 등이 기록되어 있는지 확인
    - 전체 코드 실행 플로우를 그래프로 그려서 이해를 돕고 있는지 확인
        - 중요! 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부
          
          
        - 아래 사진과 같이 말미에 회고를 잘 작성하였음
        - ![image](https://github.com/user-attachments/assets/8c6d0068-3bf7-46c1-b8ce-1ab6971ee540)
          
        
- [O]  **5. 코드가 간결하고 효율적인가요?**
    - 파이썬 스타일 가이드 (PEP8) 를 준수하였는지 확인
    - 코드 중복을 최소화하고 범용적으로 사용할 수 있도록 함수화/모듈화했는지 확인
        - 중요! 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부
          
          
        - 아래 사진과 같이 함수를 적극적으로 사용하여, 복잡하고 어려운 과정을 단순화하고 자동화 하였음
        - ![image](https://github.com/user-attachments/assets/9ad3ff2f-cb1b-45d7-a588-b747fd3b0d11)


# 회고(참고 링크 및 코드 개선)
```
# 리뷰어의 회고를 작성합니다.
# 코드 리뷰 시 참고한 링크가 있다면 링크와 간략한 설명을 첨부합니다.
# 코드 리뷰를 통해 개선한 코드가 있다면 코드와 간략한 설명을 첨부합니다.
```
- 모든 레이어에서 활성화된 feature map을 출력한 부분이 매우 인상 깊습니다.
- 또한 ACL 모델을 이용해서 추가 실험 진행하신 부분도 매우 인상 깊습니다. 정말 고생많으셨습니다!
