'''
    반복문 => while, for (이중for문)

    while : 반복횟수가 없는 경우
    형식)
        초기값 ---------1
        while 조건:  ---2 ==> false면 종료
            실행문장  --3
            증가식 -----4
    for : 반복횟수가 있는 경우
    형식)
        for 받는 변수 in 범위 => for-each => list , tuple
             실행문장
        => for(데이터 변수 : 배열 , 컬렉션 )
        for(int i = 0 ;i <10;i++)
        => for i in range(0,10) => 10은 제외

        이중for문
        for 조건 :
            for 조건:
                처리문장
        -------------------------------------
'''
i = 1
while i<=10:
    print(i)
    i+=1
print("========================================")# end="\n"
i=1

# # 입력값을 받아서 구구단을 출력
# dan = int(input("2~9사이의 정수 입력:"))
# for i in range(1,10):
#     print("{}*{}={}".format(dan,i,dan*i))

import random

com = random.randrange(1,101)
print("난수값:{}".format(com))

while True:
    user=int(input("1~100 사이의 정수 입력 :"))
    if(com==user):
        print("정답입니다.")
        break

    if user<1 or user>100:
        print("잘못된 입력입니다.")
        continue
    else:
        if user>com:
            print("user의 값이 더 큽니다.")
        else:
            print("com의 값이 더 큽니다.")

'''
    프로그램 언어
    변수 : 프로그램에 필요한 데이터를 저장할 목적 = 재사용
            변수명 = 값(데이터형을 사용하지 않는다.)
            => 데이터를 사용자가 요청한 내용으로 가공(연산자,제어문)
    모듈화 : 명령문 (함수,메소드)
            ------ 변수선언 ,연산자 ,제어문
    
    자바
    C/C++
    C#
    Kotlin
    Python
    스칼라
    GO
'''