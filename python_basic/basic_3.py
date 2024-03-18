# 연산자
'''
    연산자 => 데이터 처리 (가공)
    1) 산술연산자
         + , - , * , / , % , // , **
         ------------------- 몫   제곱근
         + : 문자열 + 문자열 => 문자열
             문자열 + 정수 => 오류
             문자열 + 실수 => 오류
        4//2 => 2
        5//2 => 2
    2) 비교연산자
        == , !=, < , > , <= , >= ==> 결과값 : True / False
    3) 논리연산자
        &&(X) => and
        ||(X) => or
        !(X) => not
    4) 대입연산자
        복합대입연산자 : += , -=, *= , ...
                      ---------------
    5) 치환연산자(형변환)
        문자열로 변환 => str(변수)
          a="정수:"+str(10)=> "10"
        정수 변환 => int(변수)
        실수 변환 => float(변수)
        논리형 변환 => bool(정수,실수)
                      bool(0)=>false
                      bool(0,0) => false
                      bool([]) = false
'''

a = 10
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**2)
print('홍길동\t'*10)
print('홍길동'+str(10))# 문자열 결합
print(bool(0),bool(0.0))
print(10.5+float(10)) # 같은 데이터형만 연산처리가 된다.

'''
    % 나머지 값은 부호가 왼쪽 편을 따라간다.
    5%2 = 1
    -5%2 = -1
    5%-2 = 1
    -5%-2 = -1
    
    ** : 제곱
    문자열 결합 시에 문자 + 문자 => 정상수행
                    문자 + 정수 => 문자+str
                    문자 + 실수 => 문자+str(실수)
                    문자 + boolean 에러 => 문자+str(boolean)
    
    비교연산자( == , != , < , > , <= , >= )

'''
import copy
a = 10
b = 9
print(a==b) # false
print(id(a),id(b))
print(a==b)
c = copy.deepcopy(b)

print(id(c))

a = 20
b = 20
c = 0
print(not(a<b)) #!(a<b) => False => True
print(not(a)) # bool(20) => True => False
print(not(b)) # bool(20) => True => False
print(bool(c))
'''
    y = 10
    y = y+1
    y = y-1
    y+=1
    y-=1
'''
x = 10
y = 9
print(x<y and x==y+1)
print(f"x={x},y={y}")

