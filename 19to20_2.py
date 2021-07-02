# 19년 대비 20년 가장 많이 참여한 유형별 여가활동 증가율

# -- 아래 5개 항목 제외 --
# 57. 홈페이지/블로그 관리
# 58. 인터넷 검색/1인 미디어 제작/SNS
# 59. 게임(온라인/모바일/콘솔게임 등)
# 74. TV시청(IPTV 포함)
# 75. 모바일 컨텐츠, 동영상, VOD 시청
# ---------------------

import math
import pandas as pd
from pandas.core.dtypes.missing import isna
import matplotlib.pyplot as plt
from matplotlib import rc
from difflib import SequenceMatcher
import my_lib

rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

def draw_piechart(list):
    for i, data in zip(range(7), list):
        list_top_value = []
        list_top_key = []
        for j in range(3):
            list_top_value.append(data[j][0])
            list_top_key.append(data[j][1])

        plt.title(pie_labels[i] + " 증가 TOP3[스마트기기 이용 내부활동 제외]")
        plt.pie(list_top_value, labels=list_top_key, autopct='%.1f%%')
        plt.show()

read_data_2019 = pd.read_spss('./2019_data.sav')
read_data_2020 = pd.read_spss('./data.sav')

remove_q_code = 'q2_1_n2'

remove_list_2020 = ['57. 홈페이지/블로그 관리',
                    '58. 인터넷 검색/1인 미디어 제작/SNS',
                    '59. 게임(온라인/모바일/콘솔게임 등)',
                    '74. TV시청(IPTV 포함)',
                    '75. 모바일 컨텐츠, 동영상, VOD 시청']

remove_list_2019 = ['57.홈페이지/블로그 관리',
                    '58.인터넷 검색/1인 미디어 제작/SNS',
                    '59.게임(온라인/모바일/콘솔게임 등)',
                    '74.TV시청(IPTV 포함)',
                    '75.모바일 컨텐츠, 동영상, VOD 시청']

for remove_2019 in remove_list_2019:
    read_data_2019 = my_lib.remove_data(read_data_2019, remove_q_code, remove_2019)
for remove_2020 in remove_list_2020:
    read_data_2020 = my_lib.remove_data(read_data_2020, remove_q_code, remove_2020)

print(read_data_2020[remove_q_code])

# 각 연령별로 분류된 DataFrame List
list_df_2019 = my_lib.split_df_of_age(read_data_2019)
list_df_2020 = my_lib.split_df_of_age(read_data_2020)

pie_labels = ["15~19세", "20대", "30대", "40대", "50대", "60대", "70세 이상"]

# 각 연령대별 19->20년도 증가값
list_sub = []

for data2019, data2020 in zip(list_df_2019, list_df_2020):
    list_sub.append(my_lib.sub20_19(data2019, data2020, 'q2_1_n2'))

draw_piechart(list_sub)