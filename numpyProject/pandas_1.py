import pandas as pd
import numpy as np
import csv
# 파일 읽기

file = open('pydata\EMP.csv')
emp = csv.reader(file)

for i in emp:
    print(i[1]+'의 직위는 '+i[2])

file.close()

"""
    1. 파일 읽기
    2. 데이터 추출 : merge(join) , groupby , 조건 검색 ...
                                  ------- mean() , sum()
"""

file = open('pydata\EMP.csv')
emp = csv.reader(file)
for i in emp:
    print(i[1].title())
file.close()

file = open('pydata\EMP.csv')
emp = csv.reader(file)
for i in emp:
    print(i[1],'\t',len(i[1]))
file.close()

file = open('pydata\EMP.csv')
emp = csv.reader(file)
for i in emp:
    print("{}의 월급은 {}입니다.".format(i[1],i[5]))
file.close()

"""
    between ~ and => 데이터프레임[컬럼].between
    in            => 데이터프레임[컬럼].isin([])
    is null       => 데이터프레임[컬럼].isnull()
    like          => 데이터프레임[컬럼].apply(lmabda x:x[0])
"""
emp = pd.read_csv('pydata\EMP.csv')
print(emp)
print(emp[['EMPNO','ENAME','DEPTNO']][emp['DEPTNO'].isin([10,20])])
print(emp[['EMPNO','ENAME','DEPTNO']][emp['SAL'].between(1000,3000)])
print(emp[['EMPNO','ENAME','DEPTNO','COMM']][emp['COMM'].isna()])

# import pandas as pd
# import numpy as np

# import matplotlib.pyplot as plt
# import seaborn as sns

# print(emp.columns)
# plt.plot(emp['SAL'])
# plt.show()

data = pd.read_csv('pydata\seoul.csv',encoding='cp949')
print(data.head())
print(data.columns)
print("가장 기온이 높은 날 : {}".format(data[data['최고기온(℃)']==data['최고기온(℃)'].max()]['날짜']))
print("가장 높은 온도 : {}".format(data['최고기온(℃)'].max()))
print(data.isna().sum())

print("가장 기온이 낮은 날 : {}".format(data[data['최저기온(℃)']==data['최저기온(℃)'].min()]['날짜']))
print("가장 낮은 온도 : {}".format(data['최저기온(℃)'].min()))

print(data[(data['날짜'].str.split("-").str[1]=='04')&(data['날짜'].str.split("-").str[2]=='05')].mean())

print(data[(data['날짜'].str.split("-").str[1]=='04')&(data['날짜'].str.split("-").str[2]=='05')].std())

import matplotlib.pyplot as plt
plt.plot(data['최고기온(℃)'])
plt.plot(data['최저기온(℃)'])
plt.show()