# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 01:50:24 2018

@author: 陈玲倩
"""
#批量读入表格
import os
import pandas as pd
import numpy as np
path = 'C:\\Users\\Administrator\\Desktop\\陈·算法'
filename = os.listdir(r'C:\Users\Administrator\Desktop\陈·算法')[2:]
all = []

#将11张表融合
for i in range(len(filename)):
    temp = (pd.read_excel(path+'/'+filename[i], sheet_name='规格品汇总'))
    temp = temp.iloc[3:, 0:3]
    temp = temp.rename(columns={'Unnamed: 2':filename[i][:-5], 'Unnamed: 1':'规格'})
    all.append(temp) 

data_all = pd.DataFrame(all[0])
for i in range(1,len(all)):
    data_all = pd.concat([data_all,all[i].iloc[:,2]], axis=1)  
    
#存入名字为合并的表中
ID = [x[0:7] for x in data_all.iloc[:,0]]
data_all.iloc[:,0] = ID
data_all.to_excel(r'C:\Users\Administrator\Desktop\表\合并.xlsx',index=False)

#读取合并数据表
data = pd.read_excel(r'C:\Users\Administrator\Desktop\表\合并.xlsx','Sheet1')
data.head()

#删除0值所在行
data[data['南昌'].isin([0])]
idata = data.drop([325,420,453,692,767]) 

#对价格求对数并写入新表
def log_col(city_name):
    idata[city_name] = idata.apply(lambda x:np.log(x[city_name]),axis=1)
for city_name in idata.columns[2:13]:
    log_col(city_name)
idata.head()
idata.to_excel(r'C:\Users\Administrator\Desktop\表\对数.xlsx',index=False)

#分类输出表格
for group_name,group in idata.groupby(idata['表2. 各规格品汇总表']):
    group.to_excel(r'C:\Users\Administrator\Desktop\表\各种表\group'+str(group_name)+'.xlsx',sheet_name='Sheet1')
   
#融合数据
path = 'C:\\Users\\Administrator\\Desktop\\表\\各种表'
filename1 = os.listdir(r'C:\Users\Administrator\Desktop\\表\各种表')
#批量读入文件夹中的xlsx文件
for i in range(len(filename1)):
    temp1 = (pd.read_excel(path+'/'+filename1[i], sheet_name='Sheet1'))
    #melt数据，并批量生成表
    meda = pd.melt(temp1,id_vars=['规格'],value_vars=['上饶','九江','南昌','吉安','宜春','抚州','新余','景德镇','萍乡','赣州','鹰潭'])
    meda.to_excel('C:\\Users\\Administrator\\Desktop\\表\\各种表2\\'+str(i+1)+'.xlsx',sheet_name='Sheet 1')
    
#整理生成的表格，将变量变为哑变量
path = 'C:\\Users\\Administrator\\Desktop\\表\\各种表2'
filename = os.listdir(r'C:\Users\Administrator\Desktop\表\各种表2')
for i in range(len(filename)):
    b = pd.read_excel('D:\\学习文件\\xm\\陈·算法\\各种表2\\'+str(i+1)+'.xlsx', sheet_name='Sheet 1')
    e = pd.get_dummies(b['规格'])
    e = e.drop(e.columns[0],axis=1)
    f = pd.get_dummies(b['variable'])
    f = f.drop(['南昌'],axis=1)
    x = [e,f]
    x = pd.concat(x,axis=1)
    y = np.array(b.iloc[:,4].values.tolist())
    #回归
    from sklearn.linear_model import LinearRegression
    reg = LinearRegression()
    reg.fit(x,y)
    coef = reg.coef_
    intercept = reg.intercept_
    coef = pd.DataFrame(coef)
    coef.to_excel(r'C:\Users\Administrator\Desktop\表\系数表\110111'+str(i+1)+'.xlsx',sheet_name='Sheet1')
#读入系数表，对各个地区的系数进行指数运算
#取每个表的后十行数，指数运算，然后放到一张表里，90行*10列
path = 'C:\\Users\\Administrator\\Desktop\\表\\系数表'
filename = os.listdir(r'C:\Users\Administrator\Desktop\表\系数表')
c0 = pd.read_excel(r'C:\Users\Administrator\Desktop\表\系数表\1101111.xlsx',sheet_name='Sheet1')
area0 = c0.iloc[-10:,0]
d0 = np.exp(area0)
d0 = d0.reset_index(drop=True)
for i in range(len(filename)-1):
    c = pd.read_excel(r'C:\Users\Administrator\Desktop\表\系数表\110111'+str(i+2)+'.xlsx',sheet_name='Sheet1')
    area = c.iloc[-10:,0]
    d = np.exp(area)
    d = d.reset_index(drop=True)
    d0 = pd.concat([d0,d],axis=1)
d0 = d0.T
d0.to_excel(r'C:\Users\Administrator\Desktop\表\ppp.xlsx',sheet_name='Sheet1')

