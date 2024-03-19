import sqlite3

class db:
    def getConnection():
        try:
            conn = sqlite3.connect("memberdb.db")
        except Exception as e:
            print(e)
        
        return conn

    '''
        함수
        def 함수명:
            처리기능
            return 값
    '''

    def createDB():
        conn = db.getConnection()
        cursor = conn.cursor()
        sql="""
            CREATE TABLE member(
                id text,
                name text,
                sex text,
                address text,
                phone text
            )
        """
        cursor.execute(sql)
        print("테이블 완료")

        cursor.close()
        conn.close()

    def insert():
        conn = db.getConnection()
        cursor = conn.cursor()
        id = input("아이디 입력 :")
        name = input("이름 입력 :")
        sex = input("성별 입력 :")
        addr = input("주소 입력 :")
        phone = input("번호 입력 :")
        data = (id,name,sex,addr,phone)

        sql = "INSERT INTO member VALUES(?,?,?,?,?)"
        
        cursor.execute(sql,data)

        conn.commit()
        
        cursor.close()
        conn.close()
    
    def selectList():
        conn = db.getConnection()
        cursor = conn.cursor()
        sql = """
            SELECT * FROM member
        """
        cursor.execute(sql)

        return cursor
    
    def find(id):
        conn = db.getConnection()
        cursor = conn.cursor()
        sql = f"""
            SELECT * FROM member 
            WHERE id='{id}'
        """
        cursor.execute(sql)
        find_data = cursor.fetchone()
        cursor.close()
        conn.close()

        return find_data
    
    def memberDelete(id):
        conn = db.getConnection()
        cursor = conn.cursor()
        sql = f"""
            DELETE FROM member WHERE id='{id}'
        """

        cursor.execute(sql)
        conn.commit()

        cursor.close()
        conn.close()
        print("데이터 삭제 완료!")
    
    def memberUpdate(memberVO):
        print(memberVO)
        conn = db.getConnection()
        cursor = conn.cursor()
        sql="UPDATE member SET name=?,sex=?,address=?,phone=? WHERE id=?"
        cursor.execute(sql,memberVO)
        conn.commit()

        cursor.close()
        conn.close()

        print("데이터 업데이트 완료!")
# createDB()
        