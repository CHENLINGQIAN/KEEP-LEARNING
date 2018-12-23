# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 10:18:03 2018

@author: Administrator
"""

import os
import numpy as np
import pandas as pd
from collections import Counter
#读入数据
path1 = 'C:\\Users\\Administrator\\Desktop\\数据\\'
filename1 = os.listdir(r'C:\Users\Administrator\Desktop\数据')

sj1 = []
dd1 = []
zt1 = []
rs1 = []
tj1 = []
wc1 = []
wcb1 = []
#表7-总体
bq1 = []
bqb1 = []
#表7-团体
tzrc = []
bqt1 = []
bqbt1 = []
ttrs = []
#表6
zzs1 = []
zzr1 = []
zzbg1 = []
zzwc1 = []
zzwcb1 = []
#表6——团体
ttwc1 = []
ttwcb1 = []
#表10 用excel做了
#表11
zdjs = []
for m in range(len(filename1)):
    temp1 = (pd.read_pickle(path1+'/'+filename1[m]))
    sj1.append(np.mean(temp1['教育ID'].value_counts()))
    dd1.append(len(temp1['活动地址'].value_counts()))
    zt1.append(len(temp1['考核类型'].value_counts()))
    rs1.append(len(temp1['教育ID'].value_counts()))
    tj1.append(len(temp1))
    wc1.append(temp1['是否完成'].value_counts())
    wcb1.append(temp1['是否完成'].value_counts('是'))
    #表7-总的
    bq1.append(temp1['活动区县'].value_counts())
    bqb1.append(temp1['活动区县'].value_counts('filename1[m]'))
    #表7-团体
    t1 = temp1[temp1['活动类型']=='团体预约']
    tzrc.append(len(t1))
    bqt1.append(t1['活动区县'].value_counts())
    bqbt1.append(t1['活动区县'].value_counts('filename1[m]'))
    ttrs.append(len(t1['教育ID'].value_counts()))
    #表6
    t2 = temp1[temp1['活动类型']=='自主选课']
    zzs1.append(len(t2['活动名称'].value_counts()))
    zzr1.append(len(t2['教育ID'].value_counts()))
    zzbg1.append(len(t2))
    zzwc1.append(t2['是否完成'].value_counts())
    zzwcb1.append(t2['是否完成'].value_counts('是'))
    #表6——团体
    ttwc1.append(t1['是否完成'].value_counts())
    ttwcb1.append(t1['是否完成'].value_counts('是'))
    #表11
    zdjs.append(len(temp1['负责教师'].value_counts()))
    
    
