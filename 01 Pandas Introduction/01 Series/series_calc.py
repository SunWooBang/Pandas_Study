# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 18:55:25 2020

@author: prays
"""

import pandas as pd
import numpy as np

std1 = pd.Series({'사격':90,'격투':60,'근력':70})
std2 = pd.Series({'사격':40, '격투':80,'근력':80})
std3 = pd.Series({'격투':80,'근력':80})
print(std1)
print('\n')
print(std2)
print('\n\n')


#series객체게 연산을 하게 되면 각 원소를 연산하여 결과를 series객체로 반환.
avg = std1/100
print(avg)
print('\n')


#series객체끼리의 연산. 시리즈 객체 안 인덱스를 참고하여 원소간 연산 후 반환한다.
#인덱스가 다르거나 원소의 개수가 다르면 결과는 NaN값이 된다.
total1 = std1 + std2
print(total1)
print('\n')


# 
add = std1+std3
minu = std1-std3
mul = std1*std3
div = std1/std3

total = pd.DataFrame([add,minu,mul,div],
                     index=['덧셈','뺄셈','곱셈','나눗셈'])
print(total)