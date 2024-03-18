# 한줄 주석
'''여러줄 주석
    1. 파이선 => 인터프리터 (한줄씩 읽어서 출력)
    2 특화된 언어 => 데이터 수집, 데이터 분석 => AI
      애플리케이션 : C/C++ , VC , C# => MS
      웹 , 모바일 : 자바, 코틀린
                   ------------ 스프링 선택 => 자바 - 코틀린
      분석 : 파이썬, R , 스칼라(Spark) => 빅데이터 실시간 분석
      데이터베이스 : DB2(대용량 데이터 베이스) , Oracle, MySQL
                    NoSQL : 몽고DB , 카산드라 ...
    3. 파이썬의 특징
        인터프리터 언어
        문법이 쉽다
        개발속도가 빠르다 (라이브러리가 많이 존재)
    4. 데이터 분석(자연어=> 국문과), 알고리즘 (수학=>이산수학)
    5. 파이썬
       1) 데이터형 (자료구조) => list , set , dict
       2) 변수
       3) 연산처리
       4) 제어문
       5) 함수
       6) 라이브러리
       7) 클래스(객체지향)
       8) 데이터베이스 연동 => orm
       9) 데이터 수집 & 데이터 분석 => numpy , pandas
       10) matplotlib => 시각화
       -------------------------------------------------
       10-1) django(Vue.js , React) , flask (웹 프레임워크)
       11) sklearn , machine Learning , Deep Learning

       1. 자료형 ( 데이터형 )
         => 자바 : 정수형, 실수형 , 문자형 ,논리형 , 참조형
                                                     | [] , class형 => String
                                            |boolean
                                      |char
                            |float,double
                    | byte, int ,long
                => 파이썬의 자료형
                   => 정수 : int
                   => 실수 : float
                   => 문자형 : String
                   => 논리형 : boolean
                   => 집합 자료형
                       리스트형 : 중복 허용 , 값 변경 가능 => [] => ArrayList
                       튜플형 : 데이터베이스 출력 , 중복 데이터 허용 , 한번 정한값은 변경할 수 없다. ()
                       셋형 : 중복을 허용하지 않는다 => {} => set
                       딕셔너리형 : 키,값 => Map
                => 파이썬 : 함수 지향 / 객체 지향 혼합
                            def 함수명:
                               => 주의점 : 들여쓰기
                               for:
                                for:
                1. 변수 : 데이터 저장 => 데이터형이 없다
                a = 10
                    ---
                2. 모든 프로그램은 동일
                   1. 데이터 저장 => 데이터 처리 => 데이터 출력
                                    연산자, 제어문
                                    ------------- 통합 => 모듈화 (함수)
                ------------------------------------------------------ 클래스
                3. 변수 => 변경할 수 있다 => 휘발성(RAM) => 프로그램이 종료가 되면 자동으로 사라진다.
                   => 파이썬에서 변수는 저장값 자체를 기억하지 않고 객체 주소를 기억하고 있다.
                      class 'int' class 'str' class 'bool' => 형변환 => 함수
                   => 모든 변수가 참조형 기억 주소로 되어 있다.
                4. 식별자
                   1) 알파벳으로 시작 (한글 가능=>비권장)
                   2) 대소문자 구분
                   3) 숫자 사용 가능
                   4) 키워드는 사용할 수 없다(import,if,else)
                5. 변수 선언
                   변수명=값
                   a=10
                   b='hello' => string "",''
                   c=True
                   d=10.5

'''
# 변수 선언과 데이터형 확인
age = 30
name='홍길동'
height=180.20
data = False
print(age)
print(type(age))
print(name)
print(type(name))
print(height)
print(type(height))
print(data)
print(type(data))

print([1,2,3]) # 배열형