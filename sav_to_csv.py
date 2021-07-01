import pandas as pd
from difflib import SequenceMatcher

read_data_2019 = pd.read_spss('./2019_data.sav')
read_data_2020 = pd.read_spss('./data.sav')

read_data_2019.to_csv('./convert_2019.csv')
read_data_2020.to_csv('./convert_2020.csv')