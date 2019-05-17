# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 12:53:49 2019

@author: Administrator
"""
import numpy as np
from scipy.stats import t
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)
df = 16
var = 0.0004
mean, var, skew, kurt = t.stats(df, moments='mvsk')
x = np.linspace(t.ppf(0.01, df),t.ppf(0.99, df), 100)
ax.plot(x, t.pdf(x, df),'r-', lw=5, alpha=0.6, label='t pdf')



fig, ax = plt.subplots(1, 1)
df = 1600
var = 50000
mean, var, skew, kurt = t.stats(df, moments='mvsk')
x = np.linspace(t.ppf(0.01, df),t.ppf(0.99, df), 100)
ax.plot(x, t.pdf(x, df),'r-', lw=5, alpha=0.6, label='t pdf')



rv = t(df)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')
vals = t.ppf([0.001, 0.5, 0.999], df)
np.allclose([0.001, 0.5, 0.999], t.cdf(vals, df))
r = t.rvs(df, size=1000)
ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
plt.show()



import numpy as np
from numpy.linalg import cholesky
import matplotlib.pyplot as plt

sampleNo = 30;
# 从特定t分布中循环取30遍，取出随机数
for i in range(29):
    np.random.seed(i)
    s = np.random.standard_t(16,size=1)

#画图
plt.subplot(100)
plt.hist(s, 30, normed=True)

