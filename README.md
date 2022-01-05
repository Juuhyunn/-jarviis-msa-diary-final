# 💥🌟 Jarviis Project 🌟💥
***
## 참고 링크
　<img src="https://img.shields.io/badge/youtube-FF0000?style=for-the-badge&logo=youtube&logoColor=white"/>

https://youtu.be/xUKj3qzYAXw

　<img src="https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>



## 개발자

안주현

## 프로젝트 소개
***
## 자비스 프로젝트 
  
이 프로젝트는 영화 아이언맨에 등장하는 토니 스타크의 비서 자비스를 모티브로 만들게 되었습니다.
스케줄러는 노트에 수필로 작성하는 방식에서부터 진화하여 현재는 언제나 들고다니는 모바일 기기에서 사용할 수 있는 어플리케이션 등의 형태로 존재합니다.
여기서 더 나아가 자동으로 사용자의 행동을 기록해주고 미래의 계획을 세워주는 기능이 추가되면, “자비스”의 프로토타입으로서 첫 발걸음이 될 것입니다.

자비스 프로젝트의 차별점으로는 스케줄러의 계획이 수행되었다고 체크되면, 그 내용을 토대로 자동으로 일기를 써주는 자동 다이어리 기능이 있습니다.

기존에는 스케줄러와 다이어리가 각각 분리되어 있어 이를 각각 작성했어야 하는 번거로움이 존재하며, 
시간과 체력 소비도 들게 됩니다. 다이어리의 경우 꾸준히 작성하지 않으면 죄책감이 생기기도 합니다.

스케줄러 내용에 의해 다이어리가 자동으로 작성된다는 차별점은 이러한 문제점을 개선할 수 있습니다.

결론적으로 저희의 목표는 직접 작성하지 않더라도 사용자 맞춤 계획을 추천해주고, 사용자가 todolist에서 수행했다고 체크한 내용에 대하여 일기를 써줄 수 있는 스케줄러, 다이어리 통합 서비스입니다.



***
## 담당 기능

### History

todo list에서 사용자가 완료했다고 체크된 일정에 대한 내용이 추가됩니다.
내용에 대한 기본적인 CRUD도 가능합니다.

### Review

리뷰에서는 todolist에서 수행했다고 체크된 일정, 즉 히스토리를 "루틴"화 하여 추천 시스템에 등록할 수 있습니다. 

비슷한 일정이 반복되어 체크되는지 확인하여 비슷한 내용의 루틴이 존재한다면,  그 루틴을 점점 강화시서 자동으로 생성합니다.
 

### Diary
마지막은 다이어리 기능입니다.
다이어리에서는 하루 동안의 수행한 계획인 히스토리를 기반으로 인공지능이 자동으로 일기를 작성해줍니다. 사용자는 이 기능을 통해 본인의 하루를 자동으로 기록화 할 수 있습니다.

***

## 환경

본 프로젝트는 애플리케이션의 확장을 용이하게 하고, 짧은 기간동안 효율적인 개발을 하기 위해서 마이크로 서비스 아키텍처를 기반으로 진행하였습니다.

도커를 통해 도커라이징하고, AWS에 S3와 RDS를 연결하여 클라우딩 환경을 구축했습니다.

***
## 개발 기간
#### 2021. 11. 1 ~ 2021. 12.24 (7주)

***
## backend 기술 스택

　<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
　<img src="https://img.shields.io/badge/anaconda-44A833?style=for-the-badge&logo=anaconda&logoColor=white"/>
　<img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=black"/>


　<img src="https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=black"/>
　<img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon%20aws&logoColor=black"/>


　<img src="https://img.shields.io/badge/pytorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=black"/>
　<img src="https://img.shields.io/badge/scikit%20learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=black"/>
　<img src="https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=black"/>
　<img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=black"/>
　<img src="https://img.shields.io/badge/selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=black"/>
　<img src="https://img.shields.io/badge/bs4-000000?&logoColor=black"/>

　<img src="https://img.shields.io/badge/Konlpy-FF0000?&logoColor=black"/>
　<img src="https://img.shields.io/badge/KoGPT2-FF6A00?&logoColor=black"/>


