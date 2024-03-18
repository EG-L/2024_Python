# 변수 사용법 => 출력 형식
# 변수 선언

a = 100
print(a)
print("a는 %d이다."%a)
b=10
c=20.0
d='홍길동'
print("b=%d,c=%f,d=%s"%(b,c,d))
'''
    정수 : %d
    실수 : %f
    문자열 : %s

'''
print("b={},c={},d={}".format(b,c,d))
print(f"b는 {b},c는{c}d는{d}")
print(id(b),id(c),id(d)) # 저장된 메모리 주소 => id()
# id값이 같을 경우 => 변수값이 동일할 때
m=3
n=3
print(id(m),id(n)) # 변수의 값이 같을 경우 동일한 주소를 가지고 있다.

print(m==n)
n=10
print(m==n)
k='hello'
print("k:%s"%k,end=" python\n")
print("k:{}".format(k))
print("k:%s-k:s"%k,sep="-")

# name = input("이름 입력 :")
# print(name+"님이 로그인 되었습니다.")

# num = input("숫자 :")
# print(f"num={num}")

story = '''앞서 속보로 전해드렸죠. 북한이 동해상으로 탄도미사일을 발사했다고 합동참모본부가 발표했습니다. 미사일 발사 시간과 비행거리 등은 한미 정보당국이 분석하고 있는데요. 배경과 전망 등을 전문가 연결해 알아보겠습니다. 박원곤 이화여대 북한학과 교수 전화로 연결돼있습니다. 교수님, 나와 계시죠?'''
print(story)
