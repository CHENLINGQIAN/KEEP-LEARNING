# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 00:32:11 2019

@author: Administrator
"""

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

path = 'C:\\Users\\Administrator\\Desktop\\表\\方差'
filename1 = sorted(os.listdir(r'C:\Users\Administrator\Desktop\表\方差'))
filename1.sort(key=lambda x:int(x[:-8]))#倒着数第四位'.'为分界线，按照‘.’左边的数字从小到大排序
all_data = []

#批量读入文件夹中的xlsx文件
for i in filename1:
    temp1 = (pd.read_excel(path+'/'+i, sheet_name='Sheet 1'))
    all_data.append(temp1)


    
#计算方差
for i in range(temp1.shape[0]):
    for j in range(temp1.shape[1]):
        add = []
        for k in all_data:
            add.append(k.iloc[i,j])
        #画散点图
        x = np.arange(1,8)  
        y = add  
        # 关键是调用scatter函数来画画
        plt.scatter(x, y, c="m", marker="x")
        plt.xlabel('Area')
        plt.ylabel('Price')
        # 最后显示出来就可以了
        plt.show()
        