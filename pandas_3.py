# import streamlit as st
import pandas as pd
import numpy as np

print("-------------- 과제 2 : 데이터 클렌징 --------------")
# 파일을 읽고, cp949 인코딩
trade_data = pd.read_csv("raw_trade_data.csv", encoding = "cp949")
print(trade_data)

# '중량' 컬럼에 결측치가 있다면 해당 품목의 평균 중량으로 채우기
""" 1. 품목(HS CODE)별 중량 평균 구하기 """
hs_mean = trade_data.groupby("hs_code")["중량"].mean()

""" 2.  """


# '수출입구분' 컬럼의 데이터가 영문(Import, Export)으로 되어 있다면 국문(수입, 수출)으로 일괄 변경하기


# 현재 '수출금액' 단위 '원'을 '백만 달러' 단위로 변환한 수출금액_M_USD 컬럼 만들기 (환율 1,470원 가정)


# 변경 후 데이터의 각 컬럼별 데이터 타입(df.dtypes)을 확인하여 수치형 데이터가 맞는지 검증
