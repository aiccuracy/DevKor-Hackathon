# DevKor-Hackathon
Hackathon on August 21.

## 프로그램명

* 음식 월드컵을 통한 **음식 추천 시스템**

## 프로그램 개요 
* 웹사이트에서 음식 월드컵을 진행하고 음식 월드컵 결과에 따라 사용자가 좋아할만한 음식을 추천해준다.

## 프로그램 구성

```
template_project
├── dataset
│   ├── FoodLists.csv
│   └── FoodData.csv
├── src
│   ├── Dataset.py
│   ├── Recommender.py
│   └── main.py
└── README.md
```

1. src

* 파이썬 프로그램이 저장될 소스 폴더

2. dataset

* 음식 리스트를 담은 csv 파일이 저장되어 있다.
* 파이썬 코드를 통해 Wikipedia에 있는 음식 데이터를 크롤링하여 만든 자체 Dataset을 csv파일로 저장한다.

## 역할 배정

* 웹사이트 구성 : 이건협
* 추천시스템 및 데이터셋 형성 : 안수진

## 추천시스템 및 데이터셋 

1. Dataset 형성 및 전처리 과정

* FoodList가 있는 csv 파일을 parsing한 후, wikipedia 크롤링을 통해 음식 사진 URL 및 음식 관련 정보를 불러온다.
  
* 음식이름 중 중복되는 항 제거
* Description column에서 중복되는 단어 제거
* foodName을 제외한 나머지 항은 하나의 str으로 합침[foodName, foodDescription]

2. 음식 추천

* Content-based filtering 사용
* 음식 월드컵에서 1위한 음식과의 코사인 유사도를 계산하여 코사인 유사도가 높은 항목을 순서대로 추천
* 1명일 경우, 그 개인의 1위 음식만을 가지고 코사인 유사도 계산
* 여러명일 경우, 각각 1위 음식의 feature를 합쳐서 새로운 row로 만들고 그 row와의 코사인 유사도를 계산하여 유사도가 높은 순서대로 추천
