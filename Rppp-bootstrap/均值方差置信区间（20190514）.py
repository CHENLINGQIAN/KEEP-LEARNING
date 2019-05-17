# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 08:41:01 2019

@author: 陈玲倩
"""
import numpy as np
import pandas as pd
import os

#选择存放输入数据文件夹的文件夹(本文中例子为RPPP-bootsrtap文件夹)
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
path = filedialog.askdirectory()

filename1 = os.listdir(path+'\\输出的结果\\GEKS')
all_data = []  
all_data = pd.DataFrame(all_data)

#批量读入文件夹中的xlsx文件
for i in filename1[:]:
    temp1 = (pd.read_excel(path+'\\输出的结果\\GEKS\\'+i, sheet_name='Sheet 1'))
    all_data = [all_data,temp1.iloc[:,1:].T]
    all_data = pd.concat(all_data,axis=1)

mean = np.mean(all_data,axis=1)
var = np.var(all_data,axis=1)
inmi = mean - np.std(all_data,axis=1)*1.96
inma = mean + np.std(all_data,axis=1)*1.96
minn = np.min(all_data,axis=1)
maxx = np.max(all_data,axis=1)

result = []  
result = pd.DataFrame(result)
result['均值'] = mean
result['方差'] = var
result['95%下限'] = inmi
result['95%上限'] = inma
result['最小值'] = minn
result['最大值'] = maxx

GEKS = pd.read_excel(path+'\\输入的数据\\原始数据的GEKS.xlsx', sheet_name='Sheet 1')
result1 = pd.concat([result,GEKS.iloc[:,1:].T],axis=1)
result1.rename(columns={0:'原始数据GEKS'},inplace = True)
ifel = (result1['原始数据GEKS'] <= result1['95%上限']) & (result1['95%下限'] <= result1['原始数据GEKS'])
result1['是否在区间内'] = ifel
path2 = path+'\\输出的结果\\均值方差置信\\'
os.makedirs(path2)
result1.to_excel(path2+'随机种子为1-20%.xlsx',sheet_name='Sheet 1')
