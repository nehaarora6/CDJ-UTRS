import pandas as pd 
import numpy as np
import matplotlib as plt

df_2018 = pd.read_csv('2018.csv')
df_2019 = pd.read_csv('2019.csv')
df_2020 = pd.read_csv('2020.csv')
df_2021 = pd.read_csv('2021.csv')

print(df_2019.head()) #print dataframe example! 

""" TODO: count the number of ships for each year
which is the number of unique names in the VesselName column
"""

