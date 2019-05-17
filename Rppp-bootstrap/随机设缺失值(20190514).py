# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 17:24:44 2019

@author: 陈玲倩
"""
#批量读入表格
import os
import pandas as pd
import numpy as np
import re
#选择存放输入数据文件夹的文件夹(本文中例子为RPPP-bootsrtap文件夹)
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
path = filedialog.askdirectory()
#######
filename = os.listdir(path+'\\输入的数据')
#暂时过滤各地区权重表（命名仅需包含权重两字）
str_convert =','.join(filename)
pattern = re.compile(r'\w*权重\w*',flags=0)
weight = re.findall(pattern,str_convert)
weight = ''.join(weight+['.xlsx'])
filename.remove(weight)

#暂时过滤原始数据的GEKS表（命名仅需包含GEKS）
str_convert =','.join(filename)
pattern1 = re.compile(r'\w*GEKS\w*',flags=0)
ordigeks = re.findall(pattern1,str_convert)
ordigeks = ''.join(ordigeks+['.xlsx'])
filename.remove(ordigeks)

#将各地区数据表融合（示例中为11张表）
all = []
for i in range(len(filename)):
    temp = (pd.read_excel(path+'\\输入的数据\\'+filename[i], sheet_name='规格品汇总'))
    temp = temp.iloc[3:, 0:3]
    temp = temp.rename(columns={'Unnamed: 2':filename[i][:-5], 'Unnamed: 1':'规格'})
    all.append(temp) 

data_all = pd.DataFrame(all[0])
for i in range(1,len(all)):
    data_all = pd.concat([data_all,all[i].iloc[:,2]], axis=1)  
    
#修改行名
ID = [x[0:7] for x in data_all.iloc[:,0]]
data_all.iloc[:,0] = ID

#将0值替换为缺失值
data_all = data_all.replace(0,np.nan)
#删除缺失值所在行
data = data_all.dropna(axis = 0)

#对价格取对数（先取完对数后设随机缺失，因为取对数不能存在缺失值nan）
def log_col(city_name):
    data[city_name] = data.apply(lambda x:np.log(x[city_name]),axis=1)
for city_name in data.columns[2:13]:
    log_col(city_name)
data.head()
    
std = []
std = pd.DataFrame(std)

p = []
p = pd.DataFrame(p)

df = []
df = pd.DataFrame(df)

suma = []

###观察做了缺失之后的数据分布
#idata = []
#idata = pd.DataFrame(idata)
#for group in data.groupby(data['表2. 各规格品汇总表']):
#    groupi = group[1]
#     #设缺失值，缺失值记为-1
#    np.random.seed(10)
#    matrix = np.random.rand(groupi.shape[0],groupi.shape[1]-2)
#    matrix = pd.DataFrame(matrix)
#    whe = np.where(matrix<0.03)#百分之x的数据设为缺失值
#    for i in range(len(whe[0])):
#        groupi.iloc[whe[0][i],whe[1][i]+2] = -1
#    #idata.append(groupi)
#    idata = [idata,groupi]
#    idata = pd.concat(idata,axis=0)        
#####

base_city = input("请输入基准地区:")   
for group in data.groupby(data.iloc[:,0]):
    groupi = group[1]
     #设缺失值，缺失值记为-1
    np.random.seed(1)
    matrix = np.random.rand(groupi.shape[0],groupi.shape[1]-2)
    matrix = pd.DataFrame(matrix)
    whe = np.where(matrix<0.20)#百分之x的数据设为缺失值
    for i in range(len(whe[0])):
        groupi.iloc[whe[0][i],whe[1][i]+2] = np.nan
    b = pd.melt(group[1],id_vars=[data.columns[1]],value_vars = [x for x in data.columns[2:]])#融合数据
    b = b.dropna(axis = 0)  #去掉缺失值  
    e = pd.get_dummies(b[data.columns[1]])#将变量变为哑变量
    e = e.drop(e.columns[0],axis=1)
    f = pd.get_dummies(b.iloc[:,1])
    f = f.drop([base_city],axis=1)
    x = [e,f]
    x = pd.concat(x,axis=1)
    y = b.iloc[:,2]
    X = pd.concat([x,y],axis=1)
    
    #回归
    from statsmodels.formula.api import ols
    lm_s = ols('value ~ x',data = X).fit()
    lm_s.params
    lm_s.summary()
    suma.append(lm_s.summary())#回归结果    
    #提出回归结果中的标准误
    #cov_params是参数的协方差矩阵
    pcov = lm_s.cov_params()
    pcov = np.array(pcov)
    #读取后取对角线上的方差然后开方
    pse = np.zeros(len(pcov))
    for o in range(len(pcov)):
        pse [o] = pcov[o,o]
    pse = np.sqrt(pse)#pse就是提取出的标准误
    pse = pd.DataFrame(pse).iloc[-10:,0]
    pse = pd.DataFrame(pse)
    pse = pse.reset_index(drop = True)
    #90个回归标准误合并输出
    std = [std,pse]
    std = pd.concat(std,axis=1)
    
    #90个回归系数合并输出
    coef = pd.DataFrame(pd.DataFrame(lm_s.params).iloc[-10:,0]).reset_index(drop = True)
    p = [p,coef]
    p = pd.concat(p,axis=1)
    
    
    df_g = sum(group[1].count())-2*len(group[1])-len(X.columns[:])+1
    df_gv = np.repeat(df_g,len(p.index))
    df_gv = pd.DataFrame(df_gv)
    df_gv = df_gv.reset_index(drop = True)
    df = [df,df_gv]
    df = pd.concat(df,axis=1)

temp_w = pd.read_excel(path + '\\输入的数据\\'+weight)
   
path2 = path+'\\输出的结果\\最终ppp\\'
os.makedirs(path2)
path3 = path+'\\输出的结果\\GEKS\\'
os.makedirs(path3)

for z in range(30):        
    np.random.seed(z)
    s = np.random.standard_t(df)
    s = pd.DataFrame(s)
    #e为误差，e=t(alpha/2)*se，s为t(alpha/2)，se为pse
    e = std.as_matrix()*s.as_matrix()
    #随机r等于期望+误差，期望为原系数p。
    r = p+e
    #再进行指数运算
    rexs = np.exp(r).T
    rexs[base_city]=1
    rexs.columns = [x for x in f.columns]+[base_city]
    
    #以下计算基本分类以上ppp
    #最终ppp为11*11的表格，并且对角线为1，GEKS为1*11的表格
    ppp = []
    geks = [] 
    temp_p = np.array(rexs)
    temp_w = np.array(temp_w)
    #这两层循环是基准地区相对于剩下几个地区的费雪理想双边价格指数
    for j in range(len(rexs.columns)):
        price = []     
        for k in range(len(rexs.columns)):
            pjqj = np.sum(temp_p[:,j] * temp_w[:,j])
            pkqj = np.sum(temp_p[:,k] * temp_w[:,j])
            p_l = pjqj/pkqj
            pjqk = np.sum(temp_p[:,j] * temp_w[:,k])
            pkqk = np.sum(temp_p[:,k] * temp_w[:,k])
            p_p = pjqk/pkqk
            pricec = pow(p_l*p_p,1/2)        
            price.append(pricec)
        #计算geks
        geksc = pow(np.prod(price),1/len(rexs.columns))
        geks.append(geksc)
        #将每次循环输出的ppp合并
        ppp.append(price)
    geks = np.array(geks)
    geks = pd.DataFrame(geks)
    ppp = np.array(ppp)
    ppp = pd.DataFrame(ppp)
    ppp.insert(0,'地区',([x for x in rexs.columns]))
    ppp.columns=['地区']+[x for x in rexs.columns]
    ppp.to_excel(path2+str(z+1)+'最终ppp.xlsx',sheet_name='Sheet 1',index = False)
    geks = geks.T
    geks.columns=[x for x in rexs.columns]
    geks.insert(0,'地区',('GEKS'))
    geks.to_excel(path3+str(z+1)+'GEKS.xlsx',sheet_name='Sheet 1',index = False)
    
    