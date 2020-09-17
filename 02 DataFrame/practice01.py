# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 01:23:26 2020

@author: prays
"""

import pandas as pd

#열 이름을 key로 하고 리스트를 value 로 받는 딕셔너리 정의 
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

# pandas dataFrame()함수로 딕셔너리를 데이터프레임으로 변환. 변수 df에 저장
df = pd.DataFrame(dict_data)

#df의 자료형 출력
print (type(df))
print('\n')

#df에 저장되어있는 데이터프레임 객체를 출력
print(df)
