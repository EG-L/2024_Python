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