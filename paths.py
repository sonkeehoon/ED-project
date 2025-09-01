# paths.py

'''
데이터 파일 경로 설정
'''

from pathlib import Path

DATA_PATH = Path("./data")  # 데이터 폴더
RAW_DATA = DATA_PATH / "수학시험_데이터.csv"  # 원본 데이터
PROCESSED_DATA = DATA_PATH / "수학시험_데이터_processed.csv"  # 전처리된 데이터
CATEGORY_DATA = DATA_PATH / "수학시험_데이터_with_category.csv"  # 라벨링된 데이터
