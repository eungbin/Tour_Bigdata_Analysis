import math
import numpy as np
import pandas as pd
from pandas.core.dtypes.missing import isna
import matplotlib.pyplot as plt
from matplotlib import rc
from difflib import SequenceMatcher
import os

pie_labels = ["15~19세", "20대", "30대", "40대", "50대", "60대", "70세 이상"]

read_data_2019 = pd.read_csv('csv/convert_2019.csv')
print(read_data_2019)

# # lower_codebook
# i = 0
# for string_data in read_codebook['변수명']:
#     lower_string = str(string_data).lower()
#     if lower_string != "nan":
#         read_codebook['변수명'][i] = lower_string
#     i += 1
    
# 해당 질의의 해당 답변 삭제
def remove_data(df, q_code, condition):
    idx = df[df[q_code] == condition].index
    new_df = df.drop(idx)

    return new_df

# 19년도 대비 20년도 증가값
def sub20_19(df2019, df2020, q_code):
    list_19to20 = []

    age2019 = df2019[q_code].value_counts(normalize=False, sort=False, ascending=False, dropna=True)
    age2020 = df2020[q_code].value_counts(normalize=False, sort=False, ascending=False, dropna=True)

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

# Dataframe 각 연령별로 분류
def split_df_of_age(df):
    # 각 연령별로 분류된 DataFrame List
    list_df = []

    # 각 연령별로 분류 2019
    df_age_15_19 = df[df['DM2'] == "15-19세"]
    list_df.append(df_age_15_19)

    df_age_20 = df[df['DM2'] == "20대"]
    list_df.append(df_age_20)

    df_age_30 = df[df['DM2'] == "30대"]
    list_df.append(df_age_30)

    df_age_40 = df[df['DM2'] == "40대"]
    list_df.append(df_age_40)

    df_age_50 = df[df['DM2'] == "50대"]
    list_df.append(df_age_50)

    df_age_60 = df[df['DM2'] == "60대"]
    list_df.append(df_age_60)

    df_age_70 = df[df['DM2'] == "70세 이상"]
    list_df.append(df_age_70)

    return list_df

# Q3, Q4
def default_Q(list_df, q_code):
    return_list = []
    for df in list_df:
        return_list.append(df[q_code].value_counts(normalize=False, sort=True, ascending=False, dropna=True).head(5))
    return return_list

def Q9(list_df):
    return_list = []

    for df in list_df:
        return_list.append(df.mean()['q9'])
    return return_list

def drawChart_top(list2019, list2020):
    for i in range(pie_labels.__len__()):
        plt.subplot(1, 2, 1)
        plt.title("2019년도 " + pie_labels[i])
        plt.pie(list2019[i].values, labels=list2019[i].index, autopct='%.1f%%')

        plt.subplot(1, 2, 2)
        plt.title("2020년도 " + pie_labels[i])
        plt.pie(list2020[i].values, labels=list2020[i].index, autopct='%.1f%%')
        plt.show()

def drawChart_sub(list):
    for i, data in zip(range(7), list):
        list_top_value = []
        list_top_key = []
        for j in range(3):
            list_top_value.append(data[j][0])
            list_top_key.append(data[j][1])

        plt.title(pie_labels[i] + " 증가 TOP3")
        plt.pie(list_top_value, labels=list_top_key, autopct='%.1f%%')
        plt.show()

def drawChart_Bar(list2019, list2020, title, xlabel, ylabel):
    bar_width = 0.35
    alpha = 0.5

    p1 = plt.bar(np.arange(pie_labels.__len__()), list2019, 
                bar_width, color='b', alpha=alpha, label='2019')
    
    p2 = plt.bar(np.arange(pie_labels.__len__()) + bar_width, list2020, 
                bar_width, color='r', alpha=alpha, label='2019')
    
    plt.xticks(np.arange(pie_labels.__len__()), pie_labels, fontsize=12)
    plt.xlabel(xlabel, fontsize=18)
    plt.ylabel(ylabel, fontsize=18)
    plt.legend((p1[0], p2[0]), ("2019", "2020"), fontsize=15)
    plt.title(title)
    plt.show()