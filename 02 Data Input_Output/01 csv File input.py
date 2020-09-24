# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 21:40:08 2020

@author: prays
"""

import pandas as pd

#csv파일
#파일 경로를 찾고 변수 file_path에 저장
file_path = './read_csv_sample.csv'

#read_csv()함수로 데이터프레임 변환.
df1 = pd.read_csv(file_path)
print(df1)
print('\n')