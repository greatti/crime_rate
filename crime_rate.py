# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 19:20:49 2021

@author: great
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('white') #vamos mudar o estilo

df = pd.read_csv('C:/Users/great/Desktop/piton/matplotlib_seaborn/data.csv')

df= df.rename(columns = {'Invest. Esp' : 'INVEST'})
df.ANO = pd.to_numeric(df.ANO , errors='coerce')
df.INVEST = pd.to_numeric(df.INVEST , errors='coerce')

df = df.set_index('ANO')
print(df)
print(df.columns)