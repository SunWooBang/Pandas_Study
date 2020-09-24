# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 21:49:35 2020

@author: prays
"""

import pandas as pd

#read_json() 을 사용
df = pd.read_json('./read_json_sample.json')
print(df)
print('\n')
print(df.index)