# AIFFEL Campus Online Code Peer Review Templete
- 코더 : 김용석
- 리뷰어 : 김하영


# PRT(Peer Review Template)
- [v]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - 이미지내 객체 디텍션의 문제로 이미지내 인물과 동물의 이미지를 감지하고 추출하는 완성된 코드가 제출되었음.
    - 
    - 인물 Detection
    - ![image](https://github.com/user-attachments/assets/92f6f90b-cb95-42cc-8a58-9f5177b3e5cd)
      
    - 동물 Detection
    - ![image](https://github.com/user-attachments/assets/423915e3-2190-4d78-90db-04d61c8ca443)

    
- [v]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - 해당 프로젝트에서 가장 핵심적인 부분은 아래와 같은 순서로 객체를 탐지하여 마스크를 적용하고 배경을 흐릿하게 표현하는 것인데,
    - 각 단계별로 알아보기 쉽게 표현이 잘되어 있고 주석도 잘 처리되어 있음
      
    - 1. 모델을 활용한 객체 Detection
        ![image](https://github.com/user-attachments/assets/7b03f58e-dcbd-406d-9542-d38301fb711e)

      2. 이를 통해 라벨링과 segmentation 함
         ![image](https://github.com/user-attachments/assets/139be686-46fc-4230-a1bb-9df35507a218)

      3. color mask 생성
         ![image](https://github.com/user-attachments/assets/207645d6-4e28-45f1-979c-19721cb0be94)

      4. Segmentstion Mask로 원본내에 객체를 선명하고 배경은 블러하게 표현함.
         ![image](https://github.com/user-attachments/assets/d157d05f-986b-4201-b5ff-0afa5bd9fe87)

        
- [v]  **3. 에러가 난 부분을 디버깅하여 문제를 해결한 기록을 남겼거나
새로운 시도 또는 추가 실험을 수행해봤나요?**
    - 에러가 난 부분에 대한 기록이 잘 남아있음 
      ![image](https://github.com/user-attachments/assets/d8fcfc12-69ac-4539-a9cc-f13a17165893)


    - 또한 다른 시도등을 통해 에러를 해결하려는 기록이 자세히 남아있음
      ![image](https://github.com/user-attachments/assets/5f43ee77-ea83-4d91-a3aa-a31acb03d711)


    - 추가 실험에 대한 부분도 수행한 기록 또한 남아있음
      ![image](https://github.com/user-attachments/assets/8ee76dcd-9bb9-49cc-8e2c-1fa335714b0a)

    
      ![image](https://github.com/user-attachments/assets/99bd0fe3-3904-466c-bf48-9a09c25a87d7)
 

        
- [v]  **4. 회고를 잘 작성했나요?**
    - 프로젝트를 해결하면서 발생한 문제와 다음 단계에 대한 의견 및 방향이 잘 작성되어 있다.
    - ![image](https://github.com/user-attachments/assets/c1f4ce3a-7591-4fd5-bd3d-60a809b80b86)

        
- [v]  **5. 코드가 간결하고 효율적인가요?**
    - 코드는 간결하고 효율적이었음.
      ![image](https://github.com/user-attachments/assets/6e0d933f-0041-4750-8830-bd4bf31dfa06)



# 회고(참고 링크 및 코드 개선)
```
용석님의 프로젝트 코드를 보고 간결하고 단계별로 알아보기 쉽게 정리가 잘 되어 있어서 인상적이었다.
또한 다중객체 detection은 실행래보지 못했는데, 용석님께서 수행하신 내용을 보고 덕분에 이해가 잘되었다.
또한 에러난 부분에 대한 기록과 해결했던 단계들 그리고 앞으로 추가로 진행해보고자 고려한 실험등에 대한
회고가 남아 있어 추후 더 프로젝트를 진행할때 도움이 많이 될것 같다.
```

