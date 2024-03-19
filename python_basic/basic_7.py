'''
    for문
    print => sep="구분자" , end="\n"
'''

print("hello ")
print("Java")

for i in range(1,10):
    print("i={}".format(i))

'''
    range(stop) => range(10) => 0~9 (stop-1)
    range(start,stop) => range(1,10)
    range(start,stop,step) => (1,10,2) => 1 3 5 7 9
'''
for i in range(10): # 0~9
    print(i)

print("----------------------------")

for i in range(1,10):
    print(i,end="\t")
print("\n----------------------------")

for i in range(1,11,2):
    print(i,end=" ")
print("\n-----------------------------")

#for응용
#1~100까지의 합, 짝수합, 홀수합
sum=even=odd=0
for i in range(1,101):
    if(i%2==0):
        even+=i
    else:
        odd+=i
    sum+=i

print("1~100까지 짝수의 합 :{}".format(even))
print("1~100까지 홀수의 합 :{}".format(odd))
print("1~100까지 전체 합:{}".format(sum))

for i in range(1,6):
    print("★"*i)
print("")
for i in range(5,0,-1):
    print("★"*i)

for i in range(1,6):
    print((" "*(6-i-1))+"★"*i)
print("")
for i in range(5,0,-1):
    print((" "*(6-i-1))+"★"*i)

list = ["홍길동","심청이","이순신","강감찬"]

for i in range(len(list)):
    print(list[i])

msg = "Hello Python"

print(msg[0]) # 첫번째 문자열
print(f"msg[-1]={msg[-1]}") # 마지막 문자열
print(msg[:3])
print(msg[1:])
print(msg[-3:-1])

import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/youtube.csv",index_col=0)
print(df.head())

answer =list(df.loc[df.channelId.isin(df.channelId.value_counts().head(10).index)].channelTitle.unique())
print(answer)
