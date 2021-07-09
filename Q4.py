# Q9. 가장 만족스러운 여가활동 1순위

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

remove_q_code = 'q4'

remove_list_2020 = ['57. 홈페이지/블로그 관리',
                    '58. 인터넷 검색/1인 미디어 제작/SNS',
                    '59. 게임(온라인/모바일/콘솔게임 등)',
                    '74. TV시청(IPTV 포함)',
                    '75. 모바일 컨텐츠, 동영상, VOD 시청']

remove_list_2019 = ['57.홈페이지/블로그 관리',
                    '58.인터넷 검색/1인 미디어 제작/SNS',
                    '59.게임 (온라인/모바일/콘솔게임 등)',
                    '74.TV시청 (IPTV 포함)',
                    '75.모바일 컨텐츠, 동영상, VOD 시청']

# Read .sav files
read_data_2019 = pd.read_spss('./2019_data.sav')
read_data_2020 = pd.read_spss('./data.sav')

for remove_2019 in remove_list_2019:
    read_data_2019 = my_lib.remove_data(read_data_2019, remove_q_code, remove_2019)
for remove_2020 in remove_list_2020:
    read_data_2020 = my_lib.remove_data(read_data_2020, remove_q_code, remove_2020)

list_2019_df = my_lib.split_df_of_age(read_data_2019)
list_2020_df = my_lib.split_df_of_age(read_data_2020)

# Q4 TOP 5
q4_list_2019_top5 = my_lib.default_Q(list_2019_df, 'q4')
q4_list_2020_top5 = my_lib.default_Q(list_2020_df, 'q4')
# -------

list19to20 = []
for data2019, data2020 in zip(list_2019_df, list_2020_df):
    list19to20.append(my_lib.sub20_19(data2019, data2020, "q4"))

my_lib.drawChart_top(q4_list_2019_top5, q4_list_2020_top5)
my_lib.drawChart_sub(list19to20)