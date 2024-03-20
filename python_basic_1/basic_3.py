import oracledb

class Emp:
    
    #멤버함수
    def getConnection(self):
        try:
            conn = oracledb.connect(user='hr',password='happy',dsn='localhost:1521/xe')
        except Exception as e:
            print(e)
        return conn

    #생성자 생성
    def empListData(self):
        #Connection
        conn = self.getConnection()
        #Statement
        cursor = conn.cursor()
        sql = """
            SELECT empno,ename,job,TO_CHAR(hiredate,'YYYY-MM-DD') as hiredate,
            mgr,sal,comm,deptno 
            FROM emp
        """
        cursor.execute(sql)
        emp_list = cursor.fetchmany()

        cursor.close()
        conn.close()

        return emp_list
    def empDetailData(self,empno):
        conn=self.getConnection()
        cursor = conn.cursor()
        sql = f"""
            SELECT * FROM emp 
            WHERE empno={empno}
        """
        cursor.execute(sql)
        find_data = cursor.fetchone()

        cursor.close()
        conn.close()
        return find_data

emp = Emp()
emp_list = emp.empListData()
for j in range(len(emp_list)):
    for i in range(len(emp_list[j])):
        print(emp_list[j][i],end=" ")
    print()
'''
    [] => list
    () => tuple
    (key,value) => 딕셔너리(dict)
'''
print("=================================")
find_data = emp.empDetailData(int(input("사번 입력 :")))
print(find_data)