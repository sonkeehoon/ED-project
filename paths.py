# paths.py

from pathlib import Path

DATA_PATH = Path("./data")  # 데이터 폴더
RAW_DATA = DATA_PATH / "수학시험_데이터.csv"  # 원본 데이터
PREPROCESSED_DATA = DATA_PATH / "수학시험_데이터_preprocessed.csv"  # 전처리된 데이터

