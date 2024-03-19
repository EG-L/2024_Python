import oracledb
# 오라클 연결
conn = oracledb.connect(user="hr",password="happy",dsn="localhost:1521/xe")
# 커서 생성
cursor = conn.cursor()
# SQL 문장 제작
sql = """SELECT empno,ename,job,hiredate,sal,dname,loc 
FROM emp,dept
WHERE emp.deptno=dept.deptno
"""
# 결과값 받기
cursor.execute(sql)
# 출력
emp_data = cursor.fetchall()

for i in emp_data:
    for j in range(len(i)):
        print(i[j],end=" ")
    print(" ")

# 닫기
cursor.close()

"""
    오라클
        SQL 종류
        DML
            SELECT , INSERT , DELETE, UPDATE 
        내장함수
            문자: substr, length, rpad, instr
            숫자 : ceil, round, trunc
            날짜 : sysdate, month_between
                  => now()
            변환 : to_char
                  => datetime.format()
            기타 : nvl
                  => isnull()
            그룹함수 : count , max , sum , avg
        서브 쿼리
            => 일반 서브쿼리
                WHERE (subquery)
            => 스칼라 서브쿼리
                SELECT (subquery)
            => 인라인뷰
                FROM (subqeury)
        조인
            => INNER JOIN
                = Oracle 조인
                = ANSI 조인
            => OUTER JOIN
                = LEFT OUTER JOIN
                = RIGHT OUTER JOIN
        DDL 
            CREATE , DROP, ALTER , RENAME, TRUNCATE
            |제약조건
              CHECK / PRIMARY KEY / FOREIGN KEY/ UNIQUE / NOT NULL
        DCL
            GRANT / REVOKE
        TCL
            COMMIT, ROLLBACK

"""