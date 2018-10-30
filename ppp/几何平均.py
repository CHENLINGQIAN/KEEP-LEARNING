# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 09:47:45 2018

@author: 13750
"""
#读入表格
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

#以南昌为基准，算各个区域的相对价格
for i in range(2,4):
    idata[i]=idata.apply(lambda x:x[i]/x[4],axis=1)
for j in range(5,13):  
    idata[j]=idata.apply(lambda x:x[j]/x[4],axis=1)
idata[13]=idata.apply(lambda x:x[4]/x[4],axis=1)
idata = idata.rename(columns={2:'上饶1',3:'九江1',5:'吉安1',6:'宜春1',7:'抚州1',8:'新余1',9:'景德镇1',10:'萍乡1',11:'赣州1',12:'鹰潭1',13:'南昌1'
})
idata.to_excel(r'C:\Users\Administrator\Desktop\几何平均\表格.xlsx',index=False)  
#定义计算几何平均数函数
def geo_mean(iterable):
    a = np.array(iterable)
    return a.prod()**(1.0/len(a))
#计算不同分类，不同地区的几何平均
group = idata.iloc[:,13:24].groupby(idata['表2. 各规格品汇总表'])
for g,h in group:
    aaa = []
    aaa.append(g)
    for j in h:
        gm = geo_mean(h[j].values)
        aaa.append(gm) 
        print(g,gm)
    aaa = np.array(aaa).reshape(-1,12)
    df = pd.DataFrame(aaa)
    df.columns = list(idata.columns)[12:24]
    df = df.rename(columns = {'鹰潭' : '规格'})
    df.to_excel(r'C:\Users\Administrator\Desktop\几何平均\几何'+str(g)+'.xlsx',index=False)   
        
        
  