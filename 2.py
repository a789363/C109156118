# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 23:27:04 2021

@author: 123
"""

du = float(input("輸入度數:"))
s =0 #夏月電費
ns = 0 #非夏月的電費


if du<=120:
    s=du*2.10
    ns=du*2.10
elif du>120 and du<=330: #大於120 小於330
    s=120*2.10+(du-120)*3.02
    ns=120*2.10+(du-120)*2.68
    
elif du>330 and du<=500:
    s=120*2.10+210*3.02+(du-330)*4.39
    ns=120*2.10+210*2.68+(du-330)*3.61
    
elif du>500 and du<=700:
    s=120*2.10+210*3.02+170*4.39+(du-500)*4.97
    ns=120*2.10+210*2.68+170*3.61+(du-500)*4.01
    
elif du>700:
    s=120*2.10+210*3.02+170*4.39+200*4.97+(du-700)*5.63
    ns=120*2.10+210*2.68+170*3.61+200*4.01+(du-700)*4.50
    
print(s,ns)