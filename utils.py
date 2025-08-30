from konlpy.tag import Mecab
import mecab_ko_dic
import re

# 형태소 분석기 (Mecab)
mecab = Mecab(dicpath = mecab_ko_dic.dictionary_path)  # 가상환경에서 작업중일 경우 반드시 dicpath를 지정해야 합니다

def tokenize_math_text(text):
    tokens = []
    
    # 수식 부분 추출: \( ... \)
    parts = re.split(r"(\\\(.*?\\\))", text)
    
    for part in parts:
        if part.startswith(r"\(") and part.endswith(r"\)"):
            # 수식 부분 → 괄호 제거
            expr = part[2: -2].strip()
            # 수식 토큰화 (숫자, 변수, 연산자 분리)
            math_tokens = re.findall(r"[A-Za-z]+|\d+|[\^\+\-\*/=(){}]|\\[a-zA-Z]+", expr)
            tokens.extend(math_tokens)
        else:
            # 일반 텍스트는 Mecab 형태소 분석으로 분리
            text_tokens = mecab.morphs(part.strip())
            tokens.extend(text_tokens)
    
    return tokens
