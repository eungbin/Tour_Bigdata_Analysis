import math
import pandas as pd
from pandas.core.dtypes.missing import isna
import matplotlib.pyplot as plt
from matplotlib import rc
from difflib import SequenceMatcher

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

# Q3. 여가활동 주 목적

import pandas as pd
from pandas.core.dtypes.missing import isna

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

def Q3(list_df):
    return_list = []
    for df in list_df:
        return_list.append(df['q3'].value_counts(normalize=False, sort=True, ascending=False, dropna=True).head(5))
    return return_list