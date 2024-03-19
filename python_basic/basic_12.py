'''
    변수 / 연산자 / 제어문 / 배열
    ---------------------------- 함수
    변수 :
            변수명=값 => 값에 따라서 자동 저장
            문자열 => "" . ''
            숫자 => 10,10.5
            boolean => True / False
    연산자 :
        산술 => + - * / // % **
        비교 => == , !=, < , > ,<= , >=
        논리 => and , or , not
        대입 => += , -=
    제어문 :
        if
            if 조건문:
                처리문장
        if~else
            if 조건문:
                처리문장
            else:
                처리문장
        if ~ elif ~ elif ~ else
            if 조건문:
                처리문장
            elif 조건문:
                처리문장
            else:
                처리문장
    반복문 :
        while
            초기값
        
        while 조건문:
            반복처리문장
            증가식
        for
            for 변수 in 배열:
                처리문장
            for 변수 in range(1,10): => 마지막은 제외
                처리문장
    
    함수 / 클래스
    1. 함수
        => 한개의 기능을 수행
        => 명령문을 모아서 처리 (재사용)
            =>변수 선언 / 제어문 처리/ 연산 처리

    형식)
        def 함수명(*args): *=> pointer
        => 함수명(1)
        => 함수명(1,2)
        => 함수명(1,2,3,4..)
'''
from random import randrange

# 함수 (리턴형이 없고 매개변수가 없는 함수)
def gugudan():
    for i in range(2,10):
        for j in range(2,10):
            print("{}*{}={}".format(i,j,i*j),end="\t")
        print("\n")

gugudan()

def sort():
    data=[30,40,10,50,20]
    print("======= 변경 전 =======")
    print(data)
    print("======= 변경 후 =======")
    print(sorted(data))
    print(sorted(data,reverse=True))

sort()

# 리턴형(X) ,매개변수(O)
'''
    def func(매개변수...):
        처리문장
'''
def gugudan2(dan):
    for i in range(2,10):
        print("{}*{}={}".format(dan,i,dan*i),end="\t")

# gugudan2(int(input("단 입력:")))
        
# 리턴형 존재 , 매개변수 x

def getName():
    return '홍길동'

print(getName())

'''
    형식)
        def func(매개변수):
            처리문장
            return 값
'''
def plus(a,b):
    c = a+b
    return c

print(plus(5,10))

# default 매개변수
'''
    형식)
        def func(a,b,c):
            처리문장
        def func(a,b=10,c=20):
            처리문장
        =>호출
        func(100,200,300) => a = 100, b= 200, c = 300
        func(100) => a = 100, b= 10, c = 20

        def func(a=10,b=20):
            func() => a= 10, b = 20
            func(100) => a= 100, b= 20
            func(100,200) => a = 100, b = 200
'''
def func(a,b,c=100):
    print("a={},b={},c={}".format(a,b,c))

func(10,20,30)
func(100,200)

def func2(*args):
    print(args)
    print(list(args))
    print("총 합은 "+str(sum(args))+"입니다.")

func2(10,20,30,40)