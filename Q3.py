# Q3. 여가활동 주 목적

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

# Q3 TOP 5
q3_list_2019_top5 = my_lib.Q3(list_2019_df)
q3_list_2020_top5 = my_lib.Q3(list_2020_df)
# -------

print("Q3 2019 TOP 5")
print(q3_list_2019_top5)

print("Q3 2020 TOP 5")
print(q3_list_2020_top5)

list19to20 = []
for data2019, data2020 in zip(list_2019_df, list_2020_df):
    list19to20.append(my_lib.sub20_19(data2019, data2020, "q3"))
print(list19to20)