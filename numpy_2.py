import pandas as pd
import numpy as np
import time

# 데이터 가져오기
try:
    df = pd.read_csv("./advanced_trade_data.csv", encoding = "cp949")
    print(f"✅ 데이터를 성공적으로 불러왔습니다! 총 {len(df):,} 행")
except FileNotFoundError:
    print("❌ 파일을 찾을 수 없습니다.")
    exit()

#---------------------------------------------------------------------------------------

""" 과제 1 """

print("\n---------------- 수익성 분석 ----------------")

# pandas 컬럼을 numpy 배열로 변환
# 순수 수치 데이터만 추출하기
export_value = df["export_value"].values
weight = df["weight"].values
logistics_rate = df["logistics_cost_rate"].values
tax_rate = df["tax_rate"].values
region_code = df["region_code"].values

# 시작 시간
start_time = time.time()

# 물류비용 = 수출액 * 물류비율
logistics_cost = export_value * logistics_rate

# 관세 = 수출액 * 관세율
tax_cost = export_value * tax_rate

# 최종 순이익 = 수출액 - 물류비용 - 관세
net_profit = export_value - logistics_cost - tax_cost

# 끝난 시간
end_time = time.time()
print(f"[ 소요 시간 : {end_time - start_time} ]")

# 최종 결과
print(f"▶ 전체 순이익 : {net_profit}\n▶ 전체 평균 순이익 : {np.mean(net_profit):.2f}")

#---------------------------------------------------------------------------------------

""" 과제 2 """

print("\n---------------- 주요 통계 지표 분석 ----------------")

# 수출액의 중앙값, 표준편차, 상위 5% 경계값
print(f"▶ 수출액 중앙값 : {np.median(export_value)}")
print(f"▶ 수출액 표준편차 : {np.std(export_value)}")
print(f"▶ 수출액 상위 5% 경계값 : {np.percentile(export_value, 95):.2f}")

#---------------------------------------------------------------------------------------

""" 과제 3 """
# 수출액이 $150,000 이상인 동시에 물류비 비율이 10% 이하인 거래의 건수와 총 수출액 합계를 추출
# 불리언 마스킹을 이용한 우량 거래 필터링

print("\n---------------- 우량 거래 필터링 결과 ----------------")

# 두 조건을 모두 만족하는 거래
prime_mark = (export_value >= 150000) & (logistics_rate <= 0.10)

prime_trades = export_value[prime_mark]

print(f"▶ 해당 건수 : {len(prime_trades):,} 건")
print(f"▶ 해당 거래 총 수출액 : $ {np.sum(prime_trades):.2f}")

#---------------------------------------------------------------------------------------

""" 과제 4 """
# @ 연산자를 사용하여 지역별 평균 지표를 기반으로 종합 점수 산출, 점수가 가장 높은 지역은?
# 행렬 A : 각 지역별 [평균 수출액(만달러 단위), 평균 물류비율, 평균 관세율] 데이터를 4x3 행렬
# 행렬 B : 평가 가중치 [수출액: $0.5$, 물류비: $-0.25$, 관세: $-0.25$]를 3x1 벡터로 정의

unique_region = np.unique(region_code)
region_metrics = []

# 행렬 A
for r in unique_region:
    mask = (region_code == r)
    region_metrics.append([
        np.mean(export_value[mask]),
        np.mean(logistics_rate[mask]),
        np.mean(tax_rate[mask])
    ])

A = np.array(region_metrics) # 배열로 만들기

# 행렬 B
B = np.array([
    [0.5],
    [-0.25],
    [-0.25]
])

# 행렬 A와 행렬 B를 곱한다
market = A @ B

print("\n---------------- 지역별 시장 매력도 점수 ----------------")
region_name = ["아시아", "유럽", "북미", "기타"]
for i, name in enumerate(region_name):
    print(f"▶ {name} : {market[i, 0]:,.2f} 점")

#---------------------------------------------------------------------------------------

""" 과제 5 """
# 물류비 비율이 15%를 초과하는 데이터를 np.where 함수를 사용하여 전체 평균 물류비 비율로 대체(Replace)
# 보정 전후의 최대 물류 비율 변화 확인

avg_log = np.mean(logistics_rate)
cleaned_log = np.where(logistics_rate > 0.15, avg_log, logistics_rate)

print("\n---------------- 이상치 데이터 보정 ----------------")
print(f"▶ 보정 전 최대 물류 비율 : {np.max(logistics_rate):.2%}")
print(f"▶ 보정 후 최대 물류 비율 : {np.std(cleaned_log):.2%}")