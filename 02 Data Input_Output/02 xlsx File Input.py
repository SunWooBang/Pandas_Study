# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 21:40:52 2020

@author: prays
"""

import pandas as pd

#excel파일 읽기
df1 = pd.read_excel('./남북한발전전력량.xlsx')
df2 = pd.read_excel('./남북한발전전력량.xlsx', header=None)

#
print(df1)
print('\n\n\n\n')
print(df2)