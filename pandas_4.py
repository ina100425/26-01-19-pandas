import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime


#---------------------------------------------------------------------------------------

# 데이터 불러오기

try:
    df_perf = pd.read_csv("./trade_performance.csv", encoding = "cp949")
    df_master = pd.read_csv("./country_master.csv", encoding = "cp949")

except FileNotFoundError:
    print("❌ 파일을 찾을 수 없습니다.")
    exit()

#---------------------------------------------------------------------------------------

""" 데이터 통합 (merge) """
# 두 파일을 ctry_code를 기준으로 병합하여, 실적 데이터에 국가명과 대륙 정보가 나타나도록 하세요.

df = pd.merge(df_perf, df_master, on = "ctry_code", how = "left")
# how = "left" : 파일 2개 중에 왼쪽 파일을 기준으로 삼겠다는 뜻

#---------------------------------------------------------------------------------------

""" 대륙별 성과 분석 (Aggregation) """
# 1. 병합된 데이터를 활용하여 대륙별 총 수출액과 총 수입액을 구하세요.
continent_states = df.groupby("continent")[["export_val", "import_val"]].sum()

# 2. 어느 대륙과의 거래에서 가장 큰 무역수지(수출 － 수입) 흑자(＋)가 발생했는지 확인하세요.
continent_states["balance"] = continent_states["export_val"] - continent_states["import_val"]
print("대륙별 무역 성과 요약")
print(continent_states)

best_continent = continent_states["balance"].idxmax()
print(f"분석 결과: {best_continent} 대륙과의 거래에서 가장 큰 무역 수지 흑자가 발생했습니다.")

#---------------------------------------------------------------------------------------

""" FTA효과 분석 """
# FTA 체결 국가(fta_status == 'Y')와 미체결 국가(fta_status == 'N')의 **평균 수출 단가(수출금액/중량)**를 비교하세요.
df["평균수출단가"] = df["export_val"] / df["weight"]

# FTA 여부에 따른 평균 단가 비교
fta_ans = df.groupby("fta_status")["평균수출단가"].mean()
print(fta_ans)

print("\n FTA 여부에 따른 평균 수출 단가 비교")
print(fta_ans)

# FTA 체결이 수출 경쟁력에 기여하고 있는지 수치로 증명하세요.
if fta_ans["Y"]> fta_ans["N"] :
    print("결과 : FTA 체결 국가의 평균단가가 더 높게 나타나며 수출경쟁력이 수치로 증명되었습니다")
else :
    print("FTA 체결 국가의 평균 단가가 미 체결국가 간의 단가 차이에 대한 추가 분석이 필요함.")

#---------------------------------------------------------------------------------------

""" 품목별 집중도 분석 (Filtering) """
# 특정 품목(hs_code) 중 수출 금액이 가장 큰 상위 2개 품목을 찾으세요.

top2_hs = df.groupby("hs_code")["export_val"].sum().nlargest(2).index.tolist() #nlargest, nsmallest 상위권,하위권 중에 몇개()
print(f"\n 수출 상위 2개 품목 : {top2_hs}")

# 해당 품목들이 주로 어느 국가로 수출되고 있는지 분석하세요.
top2_df=df[df["hs_code"].isin(top2_hs)]

country_focus = top2_df.groupby(["hs_code","ctry_name"])["export_val"].sum().reset_index()
print(country_focus)

final_table = country_focus.reset_index()
print(final_table)
print(datetime.datetime.now())

#---------------------------------------------------------------------------------------

""" 시각화 및 인사이트 도출 (Visualization) """
# 날짜 데이터 월 정보 추출
df["ymd"] = pd.to_datetime(df["ymd"])
df["month"] = df["ymd"].dt.month

# 시각화 월별 수출입 추이 데이터 생성

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

monthly = df.groupby("month")[["export_val", "import_val"]].sum()
plt.figure(figsize = (12, 6))
plt.plot(monthly.index, monthly["export_val"], label = "수출액", marker = "o", linewidth = 2)
plt.plot(monthly.index, monthly["import_val"], label = "수입액", marker = "s", linewidth = 2)

plt.title("월별 수출입 실적 추이")
plt.xlabel("월(month)")
plt.ylabel("금액")
plt.show()

#---------------------------------------------------------------------------------------