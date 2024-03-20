from django.db import models
import oracledb
# Create your models here.


def getConnection():
    try:
        conn = oracledb.connect(user='hr',password='happy',dsn='localhost:1521/xe')
    except Exception as e:
        print(e)
    return conn

def foodListData(page):
    conn=getConnection()
    cursor = conn.cursor()
    rowSize = 12
    start = (rowSize*page)-(rowSize-1)
    end = rowSize*page
    sql = f"""
        SELECT fno,name,poster,num 
        FROM (SELECT fno,name,poster,rownum as num 
        FROM (SELECT fno,name,poster 
        FROM food_menu_house ORDER BY fno)) 
        WHERE num BETWEEN {start} AND {end}
    """
    cursor.execute(sql)
    food_data = cursor.fetchall()

    cursor.close()
    conn.close()
    
    return food_data

def foodTotalPage():
    conn = getConnection()
    cursor = conn.cursor()
    sql = f"""
        SELECT CEIL(COUNT(*)/12.0) FROM food_house
    """
    cursor.execute(sql)
    count = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    return count[0]