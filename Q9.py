# Q9. 여가활동을 위한 지출액(월 평균)

import math
import pandas as pd
from pandas.core.dtypes.missing import isna
import matplotlib.pyplot as plt
from matplotlib import rc
from difflib import SequenceMatcher
import my_lib

rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

# Read .sav files
read_data_2019 = pd.read_spss('./2019_data.sav')
read_data_2020 = pd.read_spss('./data.sav')

list_2019_df = my_lib.split_df_of_age(read_data_2019)
list_2020_df = my_lib.split_df_of_age(read_data_2020)

list_2019_q9 = my_lib.Q9(list_2019_df)
list_2020_q9 = my_lib.Q9(list_2020_df)

my_lib.drawChart_Bar(list_2019_q9, list_2020_q9, "연령별 여가활동을 위한 지출액(월 평균)", "AGE", "단위 : (원)")