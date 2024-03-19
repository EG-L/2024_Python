'''
    1. import
    2. def 함수() ==> class
                     ======
                      객체 지향 프로그램
       ========== 함수지향 프로그램
                  변수선언
                  연산처리 / 제어문 처리
                  라이브러리 함수 호출
    3. 호출
    = 객체지향 프로그램 (OOP)
        = 크롤링
        = CSV => 읽기 , 쓰기 => 공공포털,
        = CSV 제어
        = Pandas => 통계 데이터 출력 (Numpy , Matplotlib)
        = 머신러닝 = 맛집 댓글
        ===================== 브라우저 : React(웹 프로그램 : 쟝고)
    
    = 1. 객체지향의 객체란?
      2. 구성요소
        1. 멤버변수 => state (상태)
        2. 멤버메소드 => 동작 , 요청에 대한 처리
           ========= 다른 클래스와 통신을 해주는 역할 (소프트웨어 : 메시지)
        ***3. 생성자 : 객체 생성 (멤버변수 초기화) 
        4. 소멸자 : 객체 소멸 (객체 메모리 해제) => gc
      3. 클래스 선언
        = 클래스명 식별자
          1) 알파벳으로 시작 + 대소문자 구분 , _ , 한글시작 가능(비권장) ( _ :임시파일 제작)
          2) 숫자사용 가능 (맨 앞자리 사용 불가능)
          3) 키워드 사용 불가능
      4. 재사용기법
        = 상속
        = 오버로딩 / 오버라이딩
        = 캡슐화
      5. 클래스의 종류
        = 추상클래스
        = 인터페이스
      6. 예외처리
      7. 라이브러리 사용법 : 크롤링, IO, CSV

      class Member:
        id=''
        name=''
        sex=''
        addr=''
        tel=''
      => 메모리 할당
      mem = Member()
      mem.id=''
'''
class Student:
    hakbun=0
    name=''
    kor=0
    eng=0
    math=0

std = Student()
#멤버변수 초기화
std.hakbun = 1
std.name = "홍길동"
std.kor = 90
std.eng = 70
std.math = 80

print("학번:{}".format(std.hakbun))
print("이름:{}".format(std.name))
print("국어:{}".format(std.kor))
print("영어:{}".format(std.eng))
print("수학:{}".format(std.math))

# 생성자 : 객체 생성시에 호출 => 멤버변수에 대한 초기화
'''
    C/C++(C With Class)
    생성자 / 소멸자
    class A{
        A(){}
        ~A(){}
    }

    자바 : 생성자 , 가비지컬렉션
    Class A{
        A(){}
    }
    파이썬 : 생성자, 소멸자
    class A:
        def __init__(self):
        
        def __del__(self):
    
    class Member:
        name=''
        def __init__(self,name):
            self.name = name
        
        def __del__(self):
            del self.name
'''

class Member:
    name = '홍길동'
    sex = '남자'
    def __init__(self,name,sex) -> None:
        self.name = name
        self.sex = sex
        print("객체 생성자 메모리 함수 호출")
    
    def __del__(self):
        print("객체 메모리 해제")

    def memberPrint(self):
        print(self.name+" "+self.sex)

# name = input("이름 입력 :")
# sex = input("성별 입력 :")

# Member(name,sex).memberPrint()
'''
    1) 생성자 호출 시에는 new를 사용하지 않는다.

    ==> 객체 지향 프로그램
        재사용 기법
            => 상속
            => 포함
        변경 / 추가
            => 오버라이딩
            => 오버로딩
        데이터보호
            => 캡슐화
'''
class Sawon:
    def __init__(self,name,dept) -> None:
        self._name = name
        self._dept = dept
    def getName(self):
        return self._name
    def getDept(self):
        return self._dept
    def setName(self,name):
        self._name = name
    def setDept(self,dept):
        self._dept = dept

sawon = Sawon('홍길동','개발부')
print("이름 : {}".format(sawon.getName()))
print("부서 : {}".format(sawon.getDept()))

'''
    1. 변수는 데이터형을 사용하지 않는다. => 확인 시에는 타입을 이용한다.
        =정수형 => int
        =실수형 => float
        =문자형 => str
        =논리형 => boolean
    2. 연산자
        // , ** , / (실수)
        and , or , not
        => ++ , --는 존재하지 않는다.

    3.
        for 변수 in 리스트,튜플
        for 변수 in range(1,10) => 10-1 => 1~9
    4. 함수
        def 함수명():
            처리문장
    5. 예외처리
        try:
            처리
        except Exception as e:
            오류 처리
'''