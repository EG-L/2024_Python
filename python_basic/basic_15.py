import oracledb

conn = oracledb.connect(user="hr",password="happy",dsn="localhost:1521/xe")

cursor = conn.cursor()

page = int(input("페이지 입력 :"))
rowSize = 10
start = (rowSize*page)-(rowSize-1)
end = (rowSize*page)
sql = f"""
    SELECT fno,name,address,type,num
    FROM (SELECT fno,name,address,type,rownum as num 
    FROM (SELECT fno,name,address,type 
    FROM food_house ORDER BY fno)) 
    WHERE num BETWEEN {start} AND {end}
"""

cursor.execute(sql)

for row in cursor:
    print(row)

cursor.close()
conn.close()