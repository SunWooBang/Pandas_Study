# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 23:03:20 2020

@author: prays
"""

import pandas as pd

#csv 파일로 저장.
data = {'name' : ['Kane','Egith','pole'],
        'algol' : ["A","A+","B"],
        'basic' : ["C", "B", "B+"],
        'C++' : ["B+","C","C+"]
        }

df = pd.DataFrame(data)

#name을 인덱스로 저장
df.set_index('name', inplace=True)
print(df)

df.to_csv("./df_sample.csv")