import oracledb
from _overlapped import NULL

class DeptVO:
    deptno = 0
    dname = ''
    loc = ''

class EmpVO:
    empno=0
    ename=''
    job=''
    sal=0
    dvo=NULL
    def __init__(self):
        self.dvo = DeptVO()

class EmpDAO:
    conn = NULL
    cursor = NULL
    def getConnection(self):
        try:
            self.conn = oracledb.connect(user='hr',password='happy',dsn='localhost:1521/xe')
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(e)
    
    def disConnection(self):
        try:
            if(self.cursor!=NULL):
                self.cursor.close()
            if(self.conn!=NULL):
                self.conn.close()
        except Exception as e:
            print(e)
    
    def selectOne(self,empno):
        self.getConnection()
        sql=f"""
            SELECT empno,ename,job,sal,dname,loc,emp.deptno 
            FROM emp,dept WHERE emp.deptno=dept.deptno 
            AND empno={empno}
        """
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        vo = EmpVO()
        vo.empno=int(data[0])
        vo.ename=data[1]
        vo.job=data[2]
        vo.sal = float(data[3])
        vo.dvo.dname = data[4]
        vo.dvo.loc = data[5]
        vo.dvo.deptno = int(data[6])
        self.disConnection()
        return vo

dao = EmpDAO()
vo = dao.selectOne(7788)

print("사번:{}".format(vo.empno))
print("이름:{}".format(vo.ename))
print("급여:{}".format(vo.sal))
print("부서명:{}".format(vo.dvo.dname))
print("근무지:{}".format(vo.dvo.loc))