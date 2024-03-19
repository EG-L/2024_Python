import oracledb
conn = oracledb.connect(user="hr",password="happy",dsn="localhost:1521/xe")
cursor = conn.cursor()
cursor.execute("SELECT empno,ename,job,sal FROM emp")
emp_data = cursor.fetchmany()
cursor.close()

print(emp_data)
# [] => list , () => tuple

for i in range(len(emp_data)):
    print(emp_data[i][0],emp_data[i][1],emp_data[i][2],emp_data[i][3])