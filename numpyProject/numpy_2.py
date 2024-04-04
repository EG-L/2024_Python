score = (90)
score1 = (90,)
score2 = 90,

print(type(score),type(score1),type(score2))

nums = [1,2,3,4,5,6,7]
print(nums)

import numpy as np

a = [[1,2,3],[4,5,6]]
b = np.array(a)

print(b)
print(b.shape)

print(np.arange(5,10,3))

print(np.ones((2,3)))

import numpy as np
import pandas as pd

df = pd.read_csv('pydata\EMP.csv')
dept_df = pd.read_csv('pydata\DEPT.csv')
print(df)
print(dept_df)

empcp = df[df['DEPTNO']==30]

print(empcp)

seoul_df = pd.read_csv('pydata\seoul.csv',encoding='cp949')

print(seoul_df)

print(df[((df['DEPTNO']==30)&(df['JOB']=='SALESMAN'))])

pf_join = pd.merge(df,dept_df,on="DEPTNO",how="inner")

print(pf_join)

#ORDER BY 
print(pf_join.sort_values(by=["SAL"],ascending=True))