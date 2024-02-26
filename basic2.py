a = 100
print(a)
# a는 100이다.
print("a는 {}이다.".format(a))
b=10
c=20.0
d="홍길동"
print("a는 {0}이고, b={1}이고 c={2}이다.".format(a,b,c))

print(f"b={b},c는{c},d는{d}")
# SQL => f"SELECT * FROM emp WHERE empno={empno}"

print(id(b),id(c),id(d))
# 같은 값을 가지고 있는 경우에는 변수의 주소가 동일
a1 = 3
b1 = 3
print(a1 is b1)
print(a1 == b1)

c1 = "Hello "
print("c1:%s"%c1,end="Python\n")
# end => \t , \n
# end => seq(구분자)
print("a:%d" %a,"b:%f" %b,"c:%s" %c,sep="-")

