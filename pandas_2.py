import pandas as pd
import numpy as np

# 파일을 읽고, cp949 인코딩
trade_data = pd.read_csv("raw_trade_data.csv", encoding = "cp949")
print(trade_data)

# HS CODE 앞 두자리가 85인 데이터만 추출
hs_85 = trade_data[trade_data["hs_code"].astype(str).str.startswith("85")]
print(hs_85)

# 국가명이 미국 혹은 베트남인 데이터만 추출
usa_vnm = hs_85[hs_85["국가명"].isin(["미국", "베트남"])]
print(usa_vnm)

# 수출금액이 0인 데이터 제거
exp_notna = usa_vnm[usa_vnm["수출금액"].notna()]
print(exp_notna)

# 결과 데이터 상위 10개 출력
print(exp_notna.head(10))

# 파일명을 semiconductor_report.csv로 저장
exp_notna.to_csv("./semiconductor_report.csv", index = False) # ignore_index = True