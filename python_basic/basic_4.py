import random

'''
    1. 변수 설정
    2. 초기값 설정
    2. 필요한 연산처리
    4. 제어문 = 필요한 데이터만 출력
    ------------------------------- 함수
    ------------------------------- 함수가 여러개 (클래스) = 컴포넌트
    라이브러리 함수나 클래스 읽기 => import 사용
'''
random.seed(100)
a = random.randrange(0,100)
print(f"a={a}")
'''
    제어문
    1. 조건문
        if 제어문:
            처리문장
        => 선택 조건문
        if 조건문
            처리문장
        else:
            처리문장
        => 다중조건문
        if 조건문:
            처리문장
        elif 조건문:
            처리문장
        else:
            처리문장
    2. 반복문
        while
        for
    3. 반복제어문
        break
        continue
'''
if a%2==0:
    print(f"{a}는 짝수입니다.")
    print("프로그램 종료")