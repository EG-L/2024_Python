#if 조건문 = 들여쓰기 => 파이썬 , yml
# yml => application.properties => yml
'''

'''
import random

num = random.randrange(1,101)
print(num)
if num%2 ==0:
    print("{}는 짝수입니다.".format(num))
else:
    print("{}는 홀수입니다.".format(num))

# 다중 if문
# kor = input("국어점수 :")
# eng = input("영어점수 :")
# math = input("수학점수 :")
# print("국어점수:%s,영어점수:%s,수학점수:%s"%(kor,eng,math))
# print("국어점수:{},영어점수:{},수학점수:{}".format(kor,eng,math))
# total = int(kor)+int(eng)+int(math)
# avg = total/3
# print("총점:%d"%total)
# print("평균:%.3f"%avg)

# print(type(avg))

# avg = int(avg)
# if avg>=90:
#     print("A학점")
# elif avg>=80:
#     print("B학점")
# elif avg>=70:
#     print("C학점")
# elif avg>=60:
#     print("D학점")
# else:
#     print("F학점")
    
money = 1000
age = 25
if (money>=500):
    item='사과'
    if(age<=30):
        msg="new"
    else:
        msg="old"

print(msg+" "+item)

com = random.randrange(0,3)

user = int(input("0(가위),1(바위),2(보):"))

if com==0:
    print("컴퓨터:가위")
    if user==0:
        print("사용자:가위")
        print("비겼다.")
    elif user==1:
        print("사용자:바위")
        print("사용자가 이겼다.")
    else:
        print("사용자:보")
        print("사용자가 졌다.")
elif com==1:
    print("컴퓨터:바위")
    if user==0:
        print("사용자:가위")
        print("사용자가 졌다.")
    elif user==1:
        print("사용자:바위")
        print("비겼다.")
    else:
        print("사용자:보")
        print("사용자가 이겼다.")
else:
    print("컴퓨터:보")
    if user==0:
        print("사용자:가위")
        print("사용자가 이겼다.")
    elif user==1:
        print("사용자:바위")
        print("사용자가 졌다.")
    else:
        print("사용자:보")
        print("비겼다.")
       
result = com-user

if(result==-1 or result==2):
    print("사용자 win")
elif (result==1 or result==-2):
    print("컴퓨터 win")
else:
    print("비겼다.")