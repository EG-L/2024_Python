import oracledb

def getConnection():
    try:
        conn=oracledb.connect(user="hr",password="happy",dsn="localhost:1521/xe")
    except Exception as e:
        print(e)
    
    return conn

def studentListData():
    conn = getConnection()
    cursor = conn.cursor()
    sql = """
        SELECT hakbun,name,kor,eng,math 
        FROM student
    """
    cursor.execute(sql)
    std_data = cursor.fetchall()
    cursor.close()
    conn.close()
    return std_data

def studentInsert():
    name = input("이름 입력 :")
    kor = int(input("국어점수 입력 :"))
    eng = int(input("영어점수 입력 :"))
    math = int(input("수학점수 입력 :"))
    conn = getConnection()
    sql = f"""
            INSERT INTO student VALUES(std_hak_seq.nextval,:1,:2,:3,:4)
    """
    data = (name,kor,eng,math)
    cursor = conn.cursor()
    cursor.execute(sql,data)
    conn.commit()

    cursor.close()
    conn.close()

def studentFind(hakbun):
    conn = getConnection()
    cursor = conn.cursor()
    sql = f"""
        SELECT * FROM student 
        WHERE hakbun={hakbun}
    """
    cursor.execute(sql)
    find_data = cursor.fetchone()

    cursor.close()
    conn.close()
    return find_data

def studentDelete(hakbun):
    conn = getConnection()
    cursor = conn.cursor()
    sql = f"""
        DELETE FROM student 
        WHERE hakbun={hakbun}
    """
    cursor.execute(sql)

    conn.commit()

    cursor.close()
    conn.close()

def studentUpdate(stdData):
    conn = getConnection()
    cursor = conn.cursor()

    sql = """
        UPDATE student SET 
        name=:1,kor=:2,eng=:3,math=:4 
        WHERE hakbun=:5
    """

    cursor.execute(sql,stdData)
    conn.commit()

    cursor.close()
    conn.close()

# studentInsert()
std_data = studentListData()
for row in std_data:
    print(row)

# find_data = studentFind(input("학번 입력 :"))
# cols = ["학번","이름","국어","영어","수학"]
# for i in range(len(find_data)):
#     print("{}:{}".format(cols[i],find_data[i]))

# print("총점 : {}".format(sum(find_data[2:])))
# print("평균 : %.2f"%(sum(find_data[2:])/3))

print("=============================")
# studentDelete(input("학번 입력 :"))
stdData = ('을지문덕',80,90,50,2)
studentUpdate(stdData)

std_data = studentListData()
for row in std_data:
    print(row)
