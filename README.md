# ED-project
📄 [프로젝트 문서 (Notion)](https://www.notion.so/2103c85c39ef80e1b456d0a53ff84089)

본 포트폴리오는 외부 강의나 튜토리얼을 단순히 따라한 것이 아니라, 

주제 선정부터 모델링까지 스스로 문제를 정의하고 방법을 선택하여 수행한 결과물입니다.

## 실행 환경
- OS: Ubuntu 24.04 (WSL2)
- Python: 3.12.3
- 가상환경: venv 사용

## 프로젝트 노트북 (Colab 링크)

> GitHub에서 `.ipynb` 파일이 잘 열리지 않거나, 셀 실행이 바로 안 될 경우  
> 아래 Colab 링크를 클릭하면 실행된 상태의 노트북을 바로 확인할 수 있습니다.

- [01_preprocessing.ipynb](https://colab.research.google.com/github/sonkeehoon/ED-project/blob/main/01_preprocess.ipynb)  
  데이터 정제, 파생 컬럼 생성, 변환 과정

- [02_eda.ipynb](https://colab.research.google.com/github/sonkeehoon/ED-project/blob/main/02_eda.ipynb)  
  데이터 시각화, 요약, 통계량 확인, 가설 검정

- [03_difficulty_prediction.ipynb](https://colab.research.google.com/github/sonkeehoon/ED-project/blob/main/03_difficulty_prediction.ipynb)  
  문제 난이도 분류 모델 학습 및 평가

- [04_answer_rate_regression.ipynb](https://colab.research.google.com/github/sonkeehoon/ED-project/blob/main/04_answer_rate_regression.ipynb)  
  정답률 예측 회귀 모델 구현

## 프로젝트 구조
```
ED-project/
├── crawler/                          # 데이터 크롤링 폴더
│ └── crawler.py                      # 크롤링 코드
│ └── utils.py                        # crawler.py를 보조하는 유틸리티 모듈
|
├── data/                             # 시험문제 관련 데이터 폴더
|
├── .gitignore                        # 불필요하거나 민감한 파일 제외 설정 
├── 01_preprocessing.ipynb            # 파생 컬럼 생성 및 데이터 정제, 변환
├── 02_eda.ipynb                      # 데이터 시각화, 요약, 가설 검정, 통계량 등 출력
├── 03_difficulty_prediction.ipynb    # 난이도를 예측하는 분류 모델
├── 04_answer_rate_regression.ipynb   # 정답률을 예측하는 회귀 모델
├── CHANGELOG.md                      # 변화 로그
├── README.md                         # 프로젝트 설명서, 폴더 구조
├── paths.py                          # 데이터 파일 경로 설정
├── requirements.txt                  # 필요 파이썬 패키지 목록
├── utils.py                          # 유틸리티 함수모음 파일
```
