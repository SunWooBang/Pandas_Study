# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 01:36:20 2020

@author: prays
"""

import pandas as pd

dict_a = {'이름': ['선우','용학','지영','민희'], '성별': ['남','남','여','여'], '키': [164,173,162,165]}
df = pd.DataFrame(dict_a)

#DataFrame의 index변경!
df.index=['안녕','으하','반갑','우효']
print(df)
print('\n')

#DataFrame의 columns 변경!
df.columns=['성명','성별','자존감']
print(df)
print('\n')

#rename
df.rename(index={'안녕':'랄라','으하':'룰루','반갑':'릴로','우효':'크큐'}, inplace=True)
print(df)
print('\n')

#drop
df2 = df[:]
df2.drop('크큐',inplace=True)
df2.drop('랄라',inplace=True)
print(df2)
print('\n')

#행 선택
df3 = df[:]
print(df3.loc[['룰루','랄라']])
print('\n')
print(df3.iloc[0])
print('\n')

#열 선택
df4 = df[:]
print(df4.성명)
print('\n')
