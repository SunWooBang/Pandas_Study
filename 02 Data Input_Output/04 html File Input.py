# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 21:44:35 2020

@author: prays
"""

import pandas as pd

#url 변수에 주소 저장
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%99%98%EC%9C%A8%EC%A1%B0%ED%9A%8C"

#웹페이지의 표를 가져와서 데이터프레임으로 변환
tables = pd.read_html(url)

#table개수 파악
print("테이블 개수:"+str(len(tables)))
print('\n')

#table의 원소를 출력
for i in range(len(tables)):
    print("tables[%s]"%i)
    print(tables[i])
    print('\n')

#table의 두번째 정보를 가져옴    
df = tables[1]
    
#"통화명"열을 인덱스 지정.
df.set_index(['통화명'], inplace=True)
print(df)
