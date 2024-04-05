import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
from wordcloud import WordCloud,STOPWORDS
# STOPWORDS : 문법적인 조사, 형용사 ... 배제하고 저장 => XX적인 ..
# 지정한다 ..

data = pd.read_csv('pydata\car_recall.csv',encoding="cp949")

print(data.columns)

print(data.head)

print(sns.__version__)
# 결과치 시각화
plt.rcParams['font.family'] ='Malgun Gothic'
# msno.matrix(data)
# plt.show()
data = data.drop_duplicates(keep=False)
print(data.isna().sum())
print(len(data))
print(data['생산기간(부터)'])
print(data['생산기간(까지)'])
print(data[['생산기간(부터)','생산기간(까지)']])
print(data['생산기간(부터)'].str.split('-').str[1])
data['start_year'] = data['생산기간(부터)'].str.split('-').str[0]
data['start_month'] = data['생산기간(부터)'].str.split('-').str[1]
data['start_day'] = data['생산기간(부터)'].str.split('-').str[2]

data['end_year'] = data['생산기간(까지)'].str.split('-').str[0]
data['end_month'] = data['생산기간(까지)'].str.split('-').str[1]
data['end_day'] = data['생산기간(까지)'].str.split('-').str[2]

data['recall_year'] = data['리콜개시일'].str.split('-').str[0]
data['recall_month'] = data['리콜개시일'].str.split('-').str[1]
data['recall_day'] = data['리콜개시일'].str.split('-').str[2]
print(data)
df2 = data.drop(columns=['생산기간(부터)','생산기간(까지)','리콜개시일'],axis=1,inplace=False).rename(columns={"제작자":"makes","차명":"model","리콜사유":"case"})

print(df2.columns)

print(df2[df2['recall_year']=='2022'])

print(df2.groupby(by='makes').count()['model'])
print(df2.groupby(by='makes').count().index)

# sns.countplot(x="makes",data=df2)
# plt.xticks(rotation=270)
# plt.show()

print(df2.groupby('model').count()['makes'].sort_values(ascending=False)[:50])

# sns.countplot(x='model',data=df2)
# plt.xticks(rotation=270)
# plt.show()

# sns.countplot(x='recall_month',data=df2)
# plt.show()

# print(df2.groupby('start_year').count()['model'])
# sns.lineplot(df2.groupby('start_year').count()['model'])
# plt.show()

# sns.countplot(x='makes',data=df2[df2.recall_month.isin(['10','11','12'])])
# plt.xticks(roatation=270)
# plt.show()

# sns.countplot(x='makes',data=df2[df2.recall_month.astype('int64')>=7])
# plt.xticks(roatation=270)
# plt.show()
from konlpy.tag import Okt
from konlpy.utils import pprint
koma = Okt()

data = [" ".join(koma.nouns(i)) for i in df2['case']]
print(data)
wc1 = WordCloud(font_path='pydata/NanumGothic.ttf',background_color='white')
wc1.generate(data[0])
plt.figure(figsize=(10, 8))
plt.axis('off')
plt.imshow(wc1)
plt.show()