# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 09:13:08 2018

@author: Administrator
"""

import os
import numpy as np
import pandas as pd
from collections import Counter
#读入数据
path = 'C:\\Users\\Administrator\\Desktop\\2017-2018学年社会实践活动数据20181017\\'
filename = os.listdir(r'C:\Users\Administrator\Desktop\2017-2018学年社会实践活动数据20181017')
import datetime#导入时间戳

#教师平均指导人数
max1 = []
min1 = []
me = []
m = []
for i in range(len(filename)):
    temp = (pd.read_excel(path+'/'+filename[i], sheet_name='Sheet1'))
    #indexs = list(temp[np.isnan(temp['自主负责教师'])].index)
    #temp = temp.drop(indexs)
    count = Counter(temp['负责教师'])
    len(count)
    teamean = sum (count.values())/len(count)
    m.append(teamean) 
    max1.append(max(temp['负责教师'].value_counts()))
    min1.append(min(temp['负责教师'].value_counts()))
    me.append(temp['负责教师'].value_counts())

#去除nan
#indexs = list(temp[np.isnan(temp['自主负责教师'])].index)
#temp1 = temp.drop(indexs)
#from collections import Counter
#count = Counter(temp1['自主负责教师'])
#len(count)
#teamean = sum (count.values())/len(count)    

#指导老师在活动主题上的分布
th = [] 
for n in range(len(filename)):
    temp = (pd.read_excel(path+'/'+filename[n], sheet_name='Sheet1'))
    a = temp.groupby(temp['考核类型'])
    temp['考核类型'].value_counts()
    th.append(temp['考核类型'].value_counts())
    
#自评分数平均分
tzv = []
tz = []
hd = []
zp = []
js = []
zp2 = []
js2 = []
#表10

out = pd.DataFrame()
for n in range(len(filename)):
    temp = (pd.read_excel(path+'/'+filename[n], sheet_name='Sheet1'))
    #存为pickle文件
    cj = []
    #temp['自评分数'].replace(np.nan,0)
    #temp['教师评分'].replace(np.nan,0)
    #zp.append(np.mean(temp['自评分数']))
    #js.append(np.mean(temp['教师评分']))
    #zp2.append(temp['自评分数'].value_counts()/len(temp['自评分数']))
    #js2.append(temp['教师评分'].value_counts()/len(temp['自评分数']))
    
    #活动创建时间
    #表10
    iff = temp['活动开始时间'] - temp['活动创建时间']
    cj.append((iff > '0 days 00:00:00').value_counts('True').ix[True,0])
    cj.append(1 - (iff == '0 days 00:00:00').value_counts('True').ix[False,0])
    cj.append((iff < '0 days 00:00:00').value_counts('True').ix[True,0])
    out = pd.concat([out,pd.DataFrame(np.array(cj).reshape(-1,3))])

    #团体、自主 不同活动主题差异  
    #ttzz = temp.groupby(temp['活动类型'])
    #tz.append(ttzz['考核类型'].value_counts('团体预约'))
    #tzv.append(ttzz['考核类型'].value_counts())
    
    
    
#一、基本测度框架
#B丰富度    
#活动时间丰富度
#活动地点丰富度
#活动主题丰富度
sj = []
dd = []
zt = []
rs = []
tj = []
wc = []
wcb = []
for m in range(len(filename)):
    temp = (pd.read_excel(path+'/'+filename[m], sheet_name='Sheet1'))
    sj.append(np.mean(temp['教育ID'].value_counts()))
    dd.append(len(temp['活动地址'].value_counts()))
    zt.append(len(temp['考核类型'].value_counts()))
    rs.append(len(temp['教育ID'].value_counts()))
    tj.append(len(temp))
    wc.append(temp['是否完成'].value_counts())
    wcb.append(temp['是否完成'].value_counts('是'))







   

    