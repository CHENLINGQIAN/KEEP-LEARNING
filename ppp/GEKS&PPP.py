# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:03:11 2018

@author: Administrator
"""
import numpy as np
import pandas as pd
path = 'C:\\Users\\Administrator\\Desktop\\表\\'
temp_p = pd.read_excel(path + 'price.xlsx')
temp_w = pd.read_excel(path + '各地区权重.xlsx', sheet_name = '中类权重')
temp_BigW = pd.read_excel(path + '各地区权重.xlsx', sheet_name = '大类权重')
p_gro = temp_p.groupby(temp_p['大类'])
w_pro = temp_w.groupby(temp_w['大类'])
p = []
w = []
for i,j in zip(p_gro, w_pro):
    e, g = i
    t, k = j
    p.append(g.values.tolist())
    w.append(k.values.tolist())
#计算中类
gge = []
for m in range(12):
    temp_p = np.array(p[m])
    temp_w = np.array(w[m])
    temp_pw = temp_p[:,1:] * temp_w[:,1:]
    sum_pw = np.sum(temp_pw,axis = 0)
    ppp = []
    gg = []
    for n in range(11):
        priceaa = []
        for a in range(11):
            temp_fm1 = temp_p[:,n+1] * temp_w[:,a+1]
            temp_sum = np.sum(temp_fm1)
            temp_fz1 = temp_w[:,n+1] * temp_p[:,a+1]
            temp_sum2 = np.sum(temp_fz1)
            city_fz = sum_pw[a]
            city_fm2 = sum_pw[n]
            citya = pow(city_fz / temp_sum, 1/2)
            cityb = pow(temp_sum2 / city_fm2, 1/2)
            pricea = citya * cityb
            priceaa.append(pricea)
        geks = pow(np.prod(priceaa),1/11)
        gg.append(geks)
        ppp.append(priceaa)
    gge.append(gg)
    ggee = np.array(gge)
    ggee = pd.DataFrame(ggee)
    pppm = np.array(ppp)
    pppm = pd.DataFrame(pppm)
    ggee.to_excel(path+'中类ppp\\'+'中类GEKS.xlsx',sheet_name='Sheet 1')
    pppm.to_excel(path+'中类ppp\\'+str(m+1)+'.xlsx',sheet_name='Sheet 1')

#计算大类
temp = temp_BigW.drop(['分类'], axis = 1)
Big_w = np.array(temp)
Big_p = np.array(ggee)
Big_pw = Big_p * Big_w
sum_Big_pw = np.sum(Big_pw, axis = 0)
bigppp = []
geksgg = []
for b in range(11):
    big = []
    for c in range(11):  
        fz1 = sum_Big_pw[c]
        fm2 = sum_Big_pw[b]
        fm1f = Big_p[:,b] * Big_w[:,c]
        fm1 = np.sum(fm1f)
        fz2f = Big_p[:,c] * Big_w[:,b]
        fz2 = np.sum(fz2f)
        big_city1 = pow(fz1 / fm1, 1/2)
        big_city2 = pow(fz2 / fm2, 1/2)
        big_city = big_city1 * big_city2
        big.append(big_city)
    geksb = pow(np.prod(big),1/11)
    geksgg.append(geksb)
    GEKS = np.array(geksgg)
    GEKS = pd.DataFrame(GEKS)
    bigppp.append(big)    
    bppp = np.array(bigppp) 
    bppp = pd.DataFrame(bppp)
    bppp.to_excel(path+'大类ppp.xlsx',sheet_name='Sheet 1')
    GEKS.to_excel(path+'大类GEKS.xlsx',sheet_name='Sheet 1')