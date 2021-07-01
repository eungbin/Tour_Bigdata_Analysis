import math
import pandas as pd
from pandas.core.dtypes.missing import isna
import matplotlib.pyplot as plt
from matplotlib import rc

rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

read_data = pd.read_spss('./data.sav')
column_list = [] # columns name list

# q1_A Code List
code_list_q1_A = ['q1_A', 'q1_A_m2', 'q1_A_m3', 'q1_A_m4', 'q1_A_m5', 'q1_A_m6', 'q1_A_m7', 'q1_A_m8', 'q1_A_m9']
title_q1_A = ['전시회 관람', '박물관 관람', '음악연주회 관람', '전통예술공연 관람', '연극공연 관람', '무용공연 관람', '영화관람', '연예공연 관람', '보기 중 경험한 활동 없음']

data_length = read_data.__len__()

# q1_A 연령별 파악
def showData_Q1_A(df_age, q1_A_code):
    count = 0
    for data in df_age[q1_A_code]:
        if isna(data):
            continue
        elif data == '보기 중 경험한 활동 없음':
            continue
        else:
            count += 1
    print("count" + str(count))
    return count

for data in read_data:
    # print(data) # column title ex) ID, q1_A, q1_A_m2, ... [str data]
    column_list.append(data)

# 각 연령별로 분류된 DataFrame List
list_df = []

# 각 연령별로 분류
df_age_15_19 = read_data[read_data['DM2'] == "15-19세"]
age_15_19_count_all = df_age_15_19.__len__()
list_df.append(df_age_15_19)

df_age_20 = read_data[read_data['DM2'] == "20대"]
age_20_count_all = df_age_20.__len__()
list_df.append(df_age_20)

df_age_30 = read_data[read_data['DM2'] == "30대"]
age_30_count_all = df_age_30.__len__()
list_df.append(df_age_30)

df_age_40 = read_data[read_data['DM2'] == "40대"]
age_40_count_all = df_age_40.__len__()
list_df.append(df_age_40)

df_age_50 = read_data[read_data['DM2'] == "50대"]
age_50_count_all = df_age_50.__len__()
list_df.append(df_age_50)

df_age_60 = read_data[read_data['DM2'] == "60대"]
age_60_count_all = df_age_60.__len__()
list_df.append(df_age_60)

df_age_70 = read_data[read_data['DM2'] == "70세 이상"]
age_70_count_all = df_age_70.__len__()
list_df.append(df_age_70)

# 각 연령별 q1_A 응답 수
list_count_q1_A = []
for code in code_list_q1_A:
    print(code)
    # 각 연령별 q1_A, q1_A_m2, ... 응답 수
    list_count_detail_q1_A = []
    for age_df in list_df:
        list_count_detail_q1_A.append(showData_Q1_A(age_df, code))
    print(list_count_detail_q1_A)
    list_count_q1_A.append(list_count_detail_q1_A)

pie_labels = ["15~19세", "20세", "30세", "40세", "50세", "60세", "70세 이상"]

print(list_count_q1_A)

for i in range(code_list_q1_A.__len__()):
    plt.subplot(3, 3, (i+1))
    plt.title(title_q1_A[i])
    plt.pie(list_count_q1_A[i], labels=pie_labels, autopct='%.1f%%')

plt.show()