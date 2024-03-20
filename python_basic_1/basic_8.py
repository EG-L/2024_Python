from _overlapped import NULL
from basic_7 import Human

class Sawon(Human):
    dept = ''
    loc = ''
    def __init__(self,dept,loc):
        self.dept = dept
        self.loc = loc
    
    def run(self):
        print("학생이 달린다.")
    def eat(self):
        print("학생이 먹는다.")

sa = Sawon('sist','개발부')
sa.name='심청이'
sa.age=20
sa.sex='여자'
print("이름:{}".format(sa.name))
print("나이:{}".format(sa.age))
print("성별:{}".format(sa.sex))

sa.run()
sa.eat()

'''
    class A
    class B
    class C
    class D(A,B,C)
    추상 클래스 : 미완성 클래스
        def 함수명():
            pass
'''
from abc import *
class Board(metaclass=ABCMeta):
    @abstractmethod
    def wrtie(self):
        pass
    @abstractmethod
    def detail(self):
        pass
    @abstractmethod
    def find(self):
        pass

class FreeBoard(Board):
    def write(self):
        print("aaaa")
    def detail(self):
        print("bbbbb")
    def find(self):
        print("cccc")
