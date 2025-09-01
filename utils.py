# utils.py

'''
수학 시험 데이터 전처리 유틸리티 함수들
'''

from konlpy.tag import Mecab
import mecab_ko_dic
import re

# 형태소 분석기 (Mecab)
mecab = Mecab(dicpath = mecab_ko_dic.dictionary_path)  # 가상환경에서 작업중일 경우 반드시 dicpath를 지정해야 합니다

def tokenize_math_text(text):
    '''
    수식과 일반 텍스트가 혼합된 문자열을 토큰화하는 함수
    
    수식 내에서는 숫자, 변수, 연산자 등을 개별 토큰으로 분리
    
    일반 텍스트는 형태소 분석기로 분리
    '''
    tokens = []
    
    # 수식 부분 추출: \( ... \)
    parts = re.split(r"(\\\(.*?\\\))", text)
    
    for part in parts:
        
        if part.startswith(r"\(") and part.endswith(r"\)"):  # 수식 부분
            # 수식 부분 → 괄호 제거
            expr = part[2: -2].strip()
            # 수식 토큰화 (숫자, 변수, 연산자 분리)
            math_tokens = re.findall(r"[A-Za-z]+|\d+|[\^\+\-\*/=(){}]|\\[a-zA-Z]+", expr)
            tokens.extend(math_tokens)
            
        else:  # 일반 텍스트 부분
            text_tokens = mecab.morphs(part.strip())  # Mecab 형태소 분석으로 분리
            tokens.extend(text_tokens)
    
    return tokens
