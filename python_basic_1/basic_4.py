from _overlapped import NULL

"""
    has-a => 포함 클래스  , is-a => 상속
    class Emp{
        private Dept dvo = new Dept()
    }
    class Dept{
    
    }
"""

class Dept:
    deptno=0
    dname=''
    loc=''
    def __init__(self,deptno,dname,loc):
        self.deptno = deptno
        self.dname = dname
        self.loc = loc

    def setDeptno(self,deptno):
        self.deptno = deptno
    
    def getDeptno(self):
        return self.deptno
    
    def setDname(self,dname):
        self.dname = dname
    
    def getDname(self):
        return self.dname
    
    def setLoc(self,loc):
        self.loc = loc
    
    def getLoc(self):
        return self.loc

class Emp:
    empno=0
    ename=''
    dvo=NULL
    def __init__(self,empno,ename):
        self.empno = empno
        self.ename = ename
        self.dvo = Dept(1,"개발부","서울")

    def show(self):
        print("사번:{}".format(self.empno))
        print("이름:{}".format(self.ename))
        print("부서번호:{}".format(self.dvo.getDeptno()))
        print("부서명:{}".format(self.dvo.getDname()))
        print("근무지:{}".format(self.dvo.getLoc()))

emp = Emp(100,'홍길동')

emp.show()