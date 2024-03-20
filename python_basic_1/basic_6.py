'''
    상속(is-a) : 재사용 목적 => 수정 / 추가 => 상속없이 (***POJO)
    단점 : 단일 상속 => 다중 상속 지원 => 복잡하다 , 속도가 느려진다.
    장점 : 기존에 클래스를 전체 사용이 가능 => 수정할 수 있다.
'''

class Animal:
    def move(self):
        print("움직이는 동물")

class Dog(Animal):
    def eat(self):
        print("먹는다.")

class Pig(Animal):
    pass #정의할 내용이 없는 경우 => Animal이 가지고 있는 move만 사용
'''
    has-a(포함) => 클래스의 기능을 변경없이 사용
    is-a(상속) => 클래스의 기능을 변경해서 사용
               ------------------------------ 오버라이딩
'''
dog = Dog()

dog.move()