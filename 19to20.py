import math
import pandas as pd
from pandas.core.dtypes.missing import isna
import matplotlib.pyplot as plt
from matplotlib import rc
from difflib import SequenceMatcher

rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

def sub20_19(df2019, df2020):
    list_19to20 = []

    age2019 = df2019['q2_1_n2'].value_counts(normalize=False, sort=False, ascending=False, dropna=True)
    age2020 = df2020['q2_1_n2'].value_counts(normalize=False, sort=False, ascending=False, dropna=True)

    key2019 = age2019.keys()
    key2020 = age2020.keys()

    # 중복되는 key list [새로 생긴 문항 삭제]
    real_key_2019 = []
    real_key_2020 = []

    # 문자열의 유사도를 측정하여 85%이상의 유사도를 가지는 key 매치
    for key20 in key2020:
        for key19 in key2019:
            ratio = SequenceMatcher(None, key20, key19).ratio()
            if ratio > 0.85:
                real_key_2019.append(key19)
                real_key_2020.append(key20)
                break

    for i in range(real_key_2020.__len__()):
        list_key_value = []
        try:
            first = age2020[real_key_2020[i]]
            second = age2019[real_key_2019[i]]
            list_key_value.append(first - second)
            list_key_value.append(real_key_2020[i])
        except KeyError:
            list_key_value.append(first)
            list_key_value.append(real_key_2020[i])
        except IndexError:
            list_key_value.append(first)
            list_key_value.append(real_key_2020[i])
        list_19to20.append(list_key_value)

    list_19to20.sort(reverse=True)
    return list_19to20

def draw_piechart(list):
    for i, data in zip(range(7), list):
        list_top_value = []
        list_top_key = []
        for j in range(3):
            list_top_value.append(data[j][0])
            list_top_key.append(data[j][1])

        plt.title(pie_labels[i] + " 증가 TOP3")
        plt.pie(list_top_value, labels=list_top_key, autopct='%.1f%%')
        plt.show()

read_data_2019 = pd.read_spss('./2019_data.sav')
read_data_2020 = pd.read_spss('./data.sav')
column_list = [] # columns name list


# 각 연령별로 분류된 DataFrame List
list_df_2019 = []

# 각 연령별로 분류 2019
df_age_15_19_2019 = read_data_2019[read_data_2019['DM2'] == "15-19세"]
age_15_19_count_all = df_age_15_19_2019.__len__()
list_df_2019.append(df_age_15_19_2019)

df_age_20_2019 = read_data_2019[read_data_2019['DM2'] == "20대"]
age_20_count_all = df_age_20_2019.__len__()
list_df_2019.append(df_age_20_2019)

df_age_30_2019 = read_data_2019[read_data_2019['DM2'] == "30대"]
age_30_count_all = df_age_30_2019.__len__()
list_df_2019.append(df_age_30_2019)

df_age_40_2019 = read_data_2019[read_data_2019['DM2'] == "40대"]
age_40_count_all = df_age_40_2019.__len__()
list_df_2019.append(df_age_40_2019)

df_age_50_2019 = read_data_2019[read_data_2019['DM2'] == "50대"]
age_50_count_all = df_age_50_2019.__len__()
list_df_2019.append(df_age_50_2019)

df_age_60_2019 = read_data_2019[read_data_2019['DM2'] == "60대"]
age_60_count_all = df_age_60_2019.__len__()
list_df_2019.append(df_age_60_2019)

df_age_70_2019 = read_data_2019[read_data_2019['DM2'] == "70세 이상"]
age_70_count_all = df_age_70_2019.__len__()
list_df_2019.append(df_age_70_2019)

list_df_2020 = []

# 각 연령별로 분류 2020
df_age_15_19_2020 = read_data_2020[read_data_2020['DM2'] == "15-19세"]
age_15_19_count_all = df_age_15_19_2020.__len__()
list_df_2020.append(df_age_15_19_2020)

df_age_20_2020 = read_data_2020[read_data_2020['DM2'] == "20대"]
age_20_count_all = df_age_20_2020.__len__()
list_df_2020.append(df_age_20_2020)

df_age_30_2020 = read_data_2020[read_data_2020['DM2'] == "30대"]
age_30_count_all = df_age_30_2020.__len__()
list_df_2020.append(df_age_30_2020)

df_age_40_2020 = read_data_2020[read_data_2020['DM2'] == "40대"]
age_40_count_all = df_age_40_2020.__len__()
list_df_2020.append(df_age_40_2020)

df_age_50_2020 = read_data_2020[read_data_2020['DM2'] == "50대"]
age_50_count_all = df_age_50_2020.__len__()
list_df_2020.append(df_age_50_2020)

df_age_60_2020 = read_data_2020[read_data_2020['DM2'] == "60대"]
age_60_count_all = df_age_60_2020.__len__()
list_df_2020.append(df_age_60_2020)

df_age_70_2020 = read_data_2020[read_data_2020['DM2'] == "70세 이상"]
age_70_count_all = df_age_70_2020.__len__()
list_df_2020.append(df_age_70_2020)

pie_labels = ["15~19세", "20대", "30대", "40대", "50대", "60대", "70세 이상"]

# 각 연령대별 19->20년도 증가값
list_sub = []

list_sub.append(sub20_19(df_age_15_19_2019, df_age_15_19_2020))
list_sub.append(sub20_19(df_age_20_2019, df_age_20_2020))
list_sub.append(sub20_19(df_age_30_2019, df_age_30_2020))
list_sub.append(sub20_19(df_age_40_2019, df_age_40_2020))
list_sub.append(sub20_19(df_age_50_2019, df_age_50_2020))
list_sub.append(sub20_19(df_age_60_2019, df_age_60_2020))
list_sub.append(sub20_19(df_age_70_2019, df_age_70_2020))

draw_piechart(list_sub)