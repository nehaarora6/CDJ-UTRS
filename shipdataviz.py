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

import pandas as pd

def count_unique_vessel_names(file_path):
    # Set the chunk size according to memory availability
    chunk_size = 50000
    unique_names = set()  # Use a set to store unique names
    
    # Read the dataset in chunks
    for chunk in pd.read_excel(file_path, chunksize=chunk_size, usecols=['VesselName']):
        # Update the set with unique names from this chunk
        unique_names.update(chunk['VesselName'].dropna().unique())
    
    # The number of unique names
    return len(unique_names)
