""" PANDAS """

#---------------------------------------------------------------------------------------

import pandas as pd
import numpy as np

dict_data = {"a":1, "b":2, "c":3}
series_data = pd.Series(dict_data)
print(type(series_data))
print(series_data)

# <class 'pandas.core.series.Series'>
# a    1
# b    2
# c    3
# dtype: int64

#---------------------------------------------------------------------------------------

list_data = ["2026-01-19", 3.14, "abc", 100, True]
series_data = pd.Series(list_data)
print(type(series_data))
print(series_data)

# <class 'pandas.core.series.Series'>
# 0    2026-01-19
# 1          3.14
# 2           abc
# 3           100
# 4          True
# dtype: object

#---------------------------------------------------------------------------------------

dict_data = {"c0":[1, 2, 3], "c1":[4, 5, 6], "c2":[7, 8, 9], "c3":[10, 11, 12], "c4":[13, 14, 15]}
df = pd.DataFrame(dict_data)
print(type(df))
print(df)

# <class 'pandas.core.frame.DataFrame'>
#    c0  c1  c2  c3  c4
# 0   1   4   7  10  13
# 1   2   5   8  11  14
# 2   3   6   9  12  15

#---------------------------------------------------------------------------------------

""" pandas 데이터 내용 확인 """

# .columns : 컬럼명 확인
# .head(): 데이터 상단의 5개 행 출력
# .tail(): 데이터 하단의 5개 행 출력, () 안에 숫자 넣을 수 있음
# .shape: (행, 열) 크기 확인
# info(): 데이터에 대한 전반적인 정보 제공
    # ex) 행과 열의 크기, 컬럼명, 컬럼별 결측치, 컬럼별 데이터 타입 등
# .type() : 데이터 타입 확인

#---------------------------------------------------------------------------------------

""" 파일 불러오기 """

# 형식 :    읽기       |      쓰기
# csv :   read_csv         to_csv
# excel : read_excel      to_excel
# json :  read_json        to_json
# html :  read_html        to_html
# sql :   read_sql         to_sql

#---------------------------------------------------------------------------------------

titanic = pd.read_csv("Titanic-Dataset.csv")
    # py와 파일이 같은 폴더에 있을 경우 : 변수 = pd.read_csv("파일명.확장자")
    # 다른 폴더에 있을 경우 : (1) py가 상위 폴더, 파일이 하위 폴더 : 변수 = pd.read_csv("./하위폴더명/파일명.확장자")
    #                      (2) py가 하위 폴더, 파일이 상위 폴더 : 변수 = pd.read_csv("../파일명.확장자")
    # ./(파일명)/ : 내가 있는 위치 기준 하위 폴더로 들어가기
    # ../ : 내가 있는 위치 기준 상위 폴더로 나가기

""" titanic의 데이터 내용 확인하기 """
print(titanic)

#      PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
# 0              1         0       3  ...   7.2500   NaN         S
# 1              2         1       1  ...  71.2833   C85         C
# 2              3         1       3  ...   7.9250   NaN         S
# 3              4         1       1  ...  53.1000  C123         S
# 4              5         0       3  ...   8.0500   NaN         S
# ..           ...       ...     ...  ...      ...   ...       ... ( => 중간 생략)
# 886          887         0       2  ...  13.0000   NaN         S
# 887          888         1       1  ...  30.0000   B42         S
# 888          889         0       3  ...  23.4500   NaN         S
# 889          890         1       1  ...  30.0000  C148         C
# 890          891         0       3  ...   7.7500   NaN         Q

# [891 rows x 12 columns]

""" .columns (컬럼명 확인) """
print(titanic.columns)
# Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
#       'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
#      dtype='object')

""" head.(), tail() - 상단/하단 n개 행 출력 """
print(titanic.head())
# PassengerId  Survived  Pclass                                               Name  ...            Ticket     Fare  Cabin  Embarked
# 0            1         0       3                            Braund, Mr. Owen Harris  ...         A/5 21171   7.2500    NaN         S
# 1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  ...          PC 17599  71.2833    C85         C
# 2            3         1       3                             Heikkinen, Miss. Laina  ...  STON/O2. 3101282   7.9250    NaN         S
# 3            4         1       1       Futrelle, Mrs. Jacques Heath (Lily May Peel)  ...            113803  53.1000   C123         S
# 4            5         0       3                           Allen, Mr. William Henry  ...            373450   8.0500    NaN         S

# [5 rows x 12 columns]

print(titanic.tail())
#  PassengerId  Survived  Pclass                                      Name     Sex  ...  Parch      Ticket   Fare Cabin  Embarked
# 886          887         0       2                     Montvila, Rev. Juozas    male  ...      0      211536  13.00   NaN         S
# 887          888         1       1              Graham, Miss. Margaret Edith  female  ...      0      112053  30.00   B42         S
# 888          889         0       3  Johnston, Miss. Catherine Helen "Carrie"  female  ...      2  W./C. 6607  23.45   NaN         S
# 889          890         1       1                     Behr, Mr. Karl Howell    male  ...      0      111369  30.00   C148         C
# 890          891         0       3                       Dooley, Mr. Patrick    male  ...      0      370376   7.75   NaN         Q

# [5 rows x 12 columns]

""" .shape (행, 열 크기 확인) """
print(titanic.shape) # (891, 12)

""" .info() - 데이터 전반적인 정보 제공 """
print(titanic.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 891 entries, 0 to 890
# Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype
# ---  ------       --------------  -----
 # 0   PassengerId  891 non-null    int64
 # 1   Survived     891 non-null    int64
 # 2   Pclass       891 non-null    int64
 # 3   Name         891 non-null    object
 # 4   Sex          891 non-null    object
 # 5   Age          714 non-null    float64
 # 6   SibSp        891 non-null    int64
 # 7   Parch        891 non-null    int64
 # 8   Ticket       891 non-null    object
 # 9   Fare         891 non-null    float64
 # 10  Cabin        204 non-null    object
 # 11  Embarked     889 non-null    object
# dtypes: float64(2), int64(5), object(5)
# memory usage: 83.7+ KB
# None

print(type(titanic)) # <class 'pandas.core.frame.DataFrame'>

#---------------------------------------------------------------------------------------

# pandas에서 특정 열을 선택
# 열 1개 선택 -> Series 객체 반환
# 데이터 프레임의 열 데이터 1개만 선택할 때 2가지 방식 : (1) 대괄호[] 안에 열 이름을 ""로 입력
#                                                 (2) 점(.) 다음에 열 이름 입력
# 열 n개(2개 이상) 선택 -> DataFrame 객체 반환
# 데이터 프레임의 열 데이터 n개 선택할 때 : 이중 대괄호[[]] 안에 열 이름을 ""로 입력
# (열 1개를 DataFrame 객체로 추출하고 싶을 때도 이중 대괄호 [[]] 사용)

#---------------------------------------------------------------------------------------

""" 열 1개 선택하기 """
names = titanic["Name"] # 대괄호
print(names)
# 0                                Braund, Mr. Owen Harris
# 1      Cumings, Mrs. John Bradley (Florence Briggs Th...
# 2                                 Heikkinen, Miss. Laina
# 3           Futrelle, Mrs. Jacques Heath (Lily May Peel)
# 4                               Allen, Mr. William Henry
#                              ...
# 886                                Montvila, Rev. Juozas
# 887                         Graham, Miss. Margaret Edith
# 888             Johnston, Miss. Catherine Helen "Carrie"
# 889                                Behr, Mr. Karl Howell
# 890                                  Dooley, Mr. Patrick
# Name: Name, Length: 891, dtype: object
print(names.head()) # 상단 5개 출력

names_2 = titanic.Name # 점(.)
print(names_2) # 동일한 결과
print(names_2.head()) # 상단 5개 출력
print(type(names_2)) # <class 'pandas.core.series.Series'>
print(names.shape) # (891,)

""" 열 2개 이상 선택하기 """
# Pclass, Age 가져오기
double_columns = titanic[["Pclass", "Age"]] # 이중 대괄호
print(double_columns.head())
# Pclass   Age
# 0       3  22.0
# 1       1  38.0
# 2       3  26.0
# 3       1  35.0
# 4       3  35.0
print(type(double_columns)) # <class 'pandas.core.frame.DataFrame'>
print(double_columns.shape) # (891, 2)

#---------------------------------------------------------------------------------------

""" 판다스 데이터 필터링 """
# 1. boolean 인덱싱 : True값을 가진 행만 추출
# 2. .isin() : 각각의 요소가 DataFrame 또는 Series에 존재하는지 파악한 후 True/False로 반환
# 3. isna() : 결측 값은 True, 그 외에는 False
# 4. .notna() : 결측 값은 False, 그 외에는 True

#---------------------------------------------------------------------------------------

""" 1. boolean 인덱싱 """
    # True와 False가 섞인 Series(검사표) 추출
print(double_columns["Age"]>35) # Age 열에서 35를 초과하는 값들만 보겠다
# 0      False
# 1       True
# 2      False
# 3      False
# 4      False
#        ...
# 886    False
# 887    False
# 888    False
# 889    False
# 890    False
# Name: Age, Length: 891, dtype: bool

    # True인 행만 추출하려면?
above35 = double_columns[double_columns["Age"]>35]
print(above35.head())
# Pclass   Age
# 1        1  38.0
# 6        1  54.0
# 11       1  58.0
# 13       3  39.0
# 15       2  55.0

    # 성별(Sex)에서 남자(male)만 추출하려면?
double_columns = titanic[["Age", "Sex"]]
only_male = double_columns[double_columns["Sex"] == "male"]
print(only_male.head())
# Age   Sex
# 0  22.0  male
# 4  35.0  male
# 5   NaN  male
# 6  54.0  male
# 7   2.0  male

""" .isin() - 요소가 DataFrame 또는 Series에 존재하는지 파악한 후 True/False로 반환 """
pclass_1 = titanic[titanic["Pclass"].isin([1])]
print(pclass_1.head())
# PassengerId  Survived  Pclass                                               Name  ...    Ticket     Fare  Cabin  Embarked  
# 1             2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  ...  PC 17599  71.2833    C85         C  
# 3             4         1       1       Futrelle, Mrs. Jacques Heath (Lily May Peel)  ...    113803  53.1000   C123         S  
# 6             7         0       1                            McCarthy, Mr. Timothy J  ...     17463  51.8625    E46         S  
# 11           12         1       1                           Bonnell, Miss. Elizabeth  ...    113783  26.5500   C103         S  
# 23           24         1       1                       Sloper, Mr. William Thompson  ...    113788  35.5000     A6         S  

# [5 rows x 12 columns]

""" boolean 인덱싱 + .isin() """
print(double_columns.head())
#  Age     Sex
# 0  22.0    male
# 1  38.0  female
# 2  26.0  female
# 3  35.0  female
# 4  35.0    male

    # 20살 이상 40살 이하
age2040 = double_columns[double_columns["Age"].isin(np.arange(20, 41))]
print(age2040.head(7))
# Age     Sex
# 0   22.0    male
# 1   38.0  female
# 2   26.0  female
# 3   35.0  female
# 4   35.0    male
# 8   27.0  female
# 12  20.0    male

""" .isna() - 결측 값은 True, 그 외에는 False """
pclass_2 = double_columns["Age"].isna()
print(pclass_2.head(7))
# 0    False
# 1    False
# 2    False
# 3    False
# 4    False
# 5     True
# 6    False
# Name: Age, dtype: bool

""" .notna() - 결측 값은 False, 그 외에는 True """
pclass_3 = double_columns["Age"].notna()
print(pclass_3.head(7))
# 0     True
# 1     True
# 2     True
# 3     True
# 4     True
# 5    False
# 6     True
# Name: Age, dtype: bool

""" 결측 값을 제거하고, 누락되지 않은 값만 확인 """
    # 결측 값이 있는 행을 제거
age_notna = double_columns[double_columns["Age"].notna()]
print(age_notna.head(10)) # => 결측 값이 있던 5번 행을 삭제하고 출력
#     Age     Sex
# 0   22.0    male
# 1   38.0  female
# 2   26.0  female
# 3   35.0  female
# 4   35.0    male
# 6   54.0    male
# 7    2.0    male
# 8   27.0  female
# 9   14.0  female
# 10   4.0  female

#---------------------------------------------------------------------------------------

""" 결측치 제거 """
# .dropna(axis=0) == .dropna() : 결측값이 존재하는 행 전체를 삭제함
# .dropna(axis=1) : 결측값이 존재하는 열 전체를 삭제함

""" .dropna() - 결측치가 있는 행을 삭제 """
print(titanic.dropna().head())
# PassengerId  Survived  Pclass                                               Name  ...    Ticket     Fare  Cabin  Embarked
# 1             2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  ...  PC 17599  71.2833    C85         C  
# 3             4         1       1       Futrelle, Mrs. Jacques Heath (Lily May Peel)  ...    113803  53.1000   C123         S  
# 6             7         0       1                            McCarthy, Mr. Timothy J  ...     17463  51.8625    E46         S  
# 10           11         1       3                    Sandstrom, Miss. Marguerite Rut  ...   PP 9549  16.7000     G6         S  
# 11           12         1       1                           Bonnell, Miss. Elizabeth  ...    113783  26.5500   C103         S  

# [5 rows x 12 columns]

""" .dropna(axis=1) - 결측치가 있는 열을 삭제 """
print(titanic.dropna(axis=1).head())
# PassengerId  Survived  Pclass                                               Name  ... SibSp  Parch            Ticket     Fare
# 0            1         0       3                            Braund, Mr. Owen Harris  ...     1      0         A/5 21171   7.2500
# 1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  ...     1      0          PC 17599  71.2833
# 2            3         1       3                             Heikkinen, Miss. Laina  ...     0      0  STON/O2. 3101282   7.9250
# 3            4         1       1       Futrelle, Mrs. Jacques Heath (Lily May Peel)  ...     1      0            113803  53.1000
# 4            5         0       3                           Allen, Mr. William Henry  ...     0      0            373450   8.0500

# [5 rows x 9 columns]

#---------------------------------------------------------------------------------------

""" pandas 이름과 인덱스로 특정 행과 열 선택 """
# .loc[] : 행 이름과 열 이름 사용 - ex) DataFrame객체.loc[행 이름, 열 이름]
# .iloc[] : 행 번호와 열 번호 사용 - ex) DataFrame객체.iloc[행 번호, 열 번호]

    # 35살 이상인 경우에만 이름과 나이를 출력
name35 = titanic.loc[titanic["Age"]>=35, ["Name", "Age"]]
print(name35.head())
#                                                  Name   Age
# 1   Cumings, Mrs. John Bradley (Florence Briggs Th...  38.0
# 3        Futrelle, Mrs. Jacques Heath (Lily May Peel)  35.0
# 4                            Allen, Mr. William Henry  35.0
# 6                             McCarthy, Mr. Timothy J  54.0
# 11                           Bonnell, Miss. Elizabeth  58.0

    # name35에서 사람 이름을 출력하고 싶지 않을 때
# ???

#---------------------------------------------------------------------------------------

""" 판다스 데이터 통계 """
# .mean() : 평균값
# .median() : 중앙값
# .describe() : 다양한 통계량 요약
    # ex) mean, std, min, max, 25%, 50%, 70%
# .agg() : 여러 개의 열에 다양한 함수 적용
# 여러 함수를 매핑 : group.객체.agg([함수1, 함수2, 함수3, ......])
# 각 열마다 다른 함수를 매핑 : gruop.객체.agg({"1열":함수1, "2열":함수2, "3열":함수3}) - 딕셔너리 형식
# .groupby() : 그룹별 집계
# .value_counts(): 값의 개수

#---------------------------------------------------------------------------------------

""" .mean() - 평균값 구하기 """
print("---- 평균 나이 ----")
print(titanic["Age"].mean())
# ---- 평균 나이 ----
# 29.69911764705882

""" .describe() - 다양한 통계량 요약 """
print("---- 다양한 통계량 요약 ----")
print(titanic["Age"].describe())
# ---- 다양한 통계량 요약 ----
# count    714.000000
# mean      29.699118
# std       14.526497
# min        0.420000
# 25%       20.125000
# 50%       28.000000
# 75%       38.000000
# max       80.000000
# Name: Age, dtype: float64

""" 모든 열에 동일한 함수 적용 """
print("---- 나이와 요금의 평균 및 표준편차 ----")
print(titanic[["Age", "Fare"]].agg(["mean", "std"]))
# ---- 나이와 요금의 평균 및 표준편차 ----
#             Age       Fare
# mean  29.699118  32.204208
# std   14.526497  49.693429

""" 각 열마다 다른 함수 적용 """
print("---- 열별 사용자 집계 ----")
agg_dict = {"Age":["min", "max", "mean"],
            "Fare":["median", "sum"]}
print(titanic.agg(agg_dict))
# ---- 열별 사용자 집계 ----
#               Age        Fare
# min      0.420000         NaN
# max     80.000000         NaN
# mean    29.699118         NaN
# median        NaN     14.4542
# sum           NaN  28693.9493

""" .groupby() - 그룹별 집계 """
print("---- 성별 기준으로 평균 나이 및 요금 집계 ----")
print(titanic.groupby("Sex")[["Age", "Fare"]].mean())
# ---- 성별 기준으로 평균 나이 및 요금 집계 ----
#               Age       Fare
# Sex
# female  27.915709  44.479818
# male    30.726645  25.523893

""" .value_counts() - 값의 개수 """
print("---- 객실 등급(Pclass)별 인원수  ----")
print(titanic["Pclass"].value_counts())
# ---- 객실 등급(Pclass)별 인원수  ----
# Pclass
# 3    491
# 1    216
# 2    184
# Name: count, dtype: int64

#---------------------------------------------------------------------------------------

    # 예제: 성별 인원수 출력 - 남자 n명, 여자 n명
print("---- 성별 인원수  ----")
print(titanic["Sex"].value_counts())
# ---- 성별 인원수  ----
# Sex
# male      577
# female    314
# Name: count, dtype: int64

#---------------------------------------------------------------------------------------

""" 새로운 열을 만들고, 값을 채워넣기 """
    # 새로운 열 Country를 생성하고 전부 USA로 채우기
print("---- 새로운 열 Country 생성 ----")
titanic["Country"] = "USA"
print(titanic)
# 새로운 Country열이 생성되고 전부 USA로 채워짐

""" 기존의 열 데이터를 기반으로 새로운 열 생성  """
print("---- 기존의 열 데이터에 10씩 더해서 새로운 열 생성 ----")
titanic["New_Age"] = titanic["Age"] + 10
print(titanic)
# 기존의 Age에 +10된 값으로 새로운 New_Age열 생성

#---------------------------------------------------------------------------------------

    # 20세 미만이면 Child, 아니면 Adult
print("---- 20세 미만이면 Child, 아니면 Adult ----")
titanic["Age_group"] = "Adult" # 일단 전부 adult로 설정
# 조건에 맞는 행만 child로 변경
titanic.loc[titanic["Age"]<20, "Age_group"] = "Child"
print(titanic)

#---------------------------------------------------------------------------------------

""" DataFrame의 가장 마지막 인덱스 확인 후 행 추가하기 """
# 가장 마지막 인덱스 확인
new_index = len(titanic)
print(new_index) # 891
    # 891행까지 있으니, 마지막 index 번호는 890

# 상단 5개만 출력해서 정보 확인 -?
print(titanic.head(5))

""" 행 추가하기 """
# 1. list로 추가 (결측치가 있으면 안됨)
titanic.loc[new_index] = [892, 1,1, "Park", "female", 25, 0, 0, "Pc0595", 75.0, "A103", "S", "USA", 35, "Adult"]
print()
print(titanic.tail()) # 행이 추가됨

# 2. DataFrame으로 추가 (딕셔너리, 결측치가 있어도 됨)
new_data = pd.DataFrame({
    "Name":["Park Ina", "bbangnina"],
    "Age":[25, 22],
    "Sex":["female", "female"],
    "Survived":[1, 1]
})
titanic = pd.concat([titanic, new_data], ignore_index = True) # index 번호가 이어서 생성
    # ignore_index = True를 입력하지 않으면 새로 추가된 행부터 index 번호가 0에서 다시 시작함
print(titanic.tail()) # 행이 추가됨 (값을 지정하지 않은 열은 결측값으로 표시)

#---------------------------------------------------------------------------------------

""" ~~로 시작하는 자료만 출력하기 """
    # 문자열 데이터가 S로 시작하는 자료만 추출 :
# titanic["Name"].str.startswith("S")//

    # 숫자 데이터가 2로 시작하는 자료만 추출
# titanic[titanic["Age"].astype(str).str.startswith("2")]
# print(titanic[titanic["Age"].astype(str).str.startswith("2")])  =>   20대인 사람만 출력함

    # 숫자 데이터에 82가 포함된 자료만 추출
# titanic[titanic["Age"].astype(str).str.startswith("^82")]

#---------------------------------------------------------------------------------------

""" 여기서 저장한 값들을 excel 파일로 내보내는 법 """
# 여기서 아무리 수정해도 원본 파일은 변하지 않음!
# to_csv, to_excel 등등...

titanic.to_csv("./sample1.csv", index = False) # 파일명은 sample1로, index 번호 제외하고 파일 생성
titanic.to_excel("./sample1.xlsx", index = False)
print("파일을 성공적으로 저장했습니다!")