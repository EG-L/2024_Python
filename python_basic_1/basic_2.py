'''
    클래스 구성 요소
    ---------------
    class
    ===============
       변수 설정
       name = ''
       age = 0
    ===============
       생성자
       => 메모리 할당
       => 멤버변수 초기화
       => def __init__(self) => this 대신 self 사용
    ===============
       소멸자
       => def __del__(self)
    ===============
       멤버 함수
       => def 함수명():
    ===============

'''
class Member:
    #변수 설정
    name = ''
    age = 0
    def __init__(self):
        self.name = '홍길동'
        self.age = 20
    def __del__(self):
        print("객체 소멸 : 소멸자 함수 ")#finalize()
    #멤버함수
    def memberPrint(self):
        print("이름 :{}".format(self.name))
        print("나이 :{}".format(self.age))

saram=Member() # new는 사용하지 않는다.
saram.memberPrint()
