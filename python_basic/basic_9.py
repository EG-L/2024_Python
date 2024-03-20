'''
    예외처리
    형식)
        try:
            정상실행문장
        except: 여러개 사용이 가능
        finally:
            try/except와 상관없이 수행하는 문장 => 서버,데이터베이스 종료

        python에서 지원하는 예외처리
        --------------------------
            BaseException (Throwable)
              |
            --------------------------
            |                           |
        SystemExit KeyBoardInterrupt   Exception
        -----------------------------  ---------
            |                                 |
          Error (수정이 불가능한)             ArithmeticError(0으로 나눌 경우)
                                            OverflowError
                                            FloatingError

            
'''

def div(a,b):
    return a/b

try:
    c=div(5,0)# 에러 발생시 except로 이동
except ZeroDivisionError as e:
    print(0)

'''
    문법 : 프로그래머의 실수 ( 들여쓰기 )
    예외 : 사용자의 입력값, 프로그래머의 실수
'''

try:
    e=[2,3]
    print(e[0])
    print(e[1])
    print(e[2]) #IndexError
except Exception as e:
    print(e)
finally:
    print("무조건 수행")