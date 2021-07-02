# 19년 대비 20년 가장 많이 참여한 유형별 여가활동 증가율

import math
import pandas as pd
from pandas.core.dtypes.missing import isna
import matplotlib.pyplot as plt
from matplotlib import rc
from difflib import SequenceMatcher
import my_lib

rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

read_data_2019 = pd.read_spss('./2019_data.sav')
read_data_2020 = pd.read_spss('./data.sav')

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

list_2019_df = my_lib.split_df_of_age(read_data_2019)
list_2020_df = my_lib.split_df_of_age(read_data_2020)

pie_labels = ["15~19세", "20대", "30대", "40대", "50대", "60대", "70세 이상"]

# 각 연령대별 19->20년도 증가값
list_sub = []

for data2019, data2020 in zip(list_2019_df, list_2020_df):
    list_sub.append(my_lib.sub20_19(data2019, data2020, 'q2_1_n2'))

draw_piechart(list_sub)