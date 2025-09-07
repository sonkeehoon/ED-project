# ED-project
📄 [프로젝트 문서 (Notion)](https://www.notion.so/2103c85c39ef80e1b456d0a53ff84089)

본 포트폴리오는 외부 강의나 튜토리얼을 단순히 따라한 것이 아니라, 

주제 선정부터 모델링까지 스스로 문제를 정의하고 방법을 선택하여 수행한 결과물입니다.

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
