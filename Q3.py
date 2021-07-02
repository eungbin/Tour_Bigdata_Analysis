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

