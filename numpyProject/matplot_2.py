import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno

data = pd.read_csv('pydata\subway.csv',encoding='cp949')

print(data)
print(data.columns)

df2 = data.drop(columns={"작업일자","사용월"},inplace=False,axis=1)
print(df2.groupby("호선명").mean())

# print(df2)
# plt.plot()
# plt.show()
plt.rcParams['font.family'] ='Malgun Gothic'
# plt.plot(df2.groupby("호선명").mean().T)
# plt.legend(df2.groupby("호선명").mean().T)
# plt.xticks(rotation=270)
# plt.show()

print(df2.groupby(["호선명","지하철역"]).mean().T['2호선'].T.mean())
print(df2.groupby(["호선명","지하철역"]).mean().T['2호선'].columns)
# temp = df2.groupby(["호선명","지하철역"]).mean().T['2호선'].T
# print(temp[temp(['승차인원' in i for i in temp.columns]==True)])

plt.bar(list(list(df2.groupby(["호선명","지하철역"]).mean().T['2호선'].columns)),list(df2.groupby(["호선명","지하철역"]).mean().T['2호선'].mean()))
# plt.legend(list(df2.groupby(["호선명","지하철역"]).mean().T['2호선'].columns))
plt.xticks(rotation=270)
plt.show()