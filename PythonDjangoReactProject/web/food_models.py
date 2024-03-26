# from django.db import models
from web.models import getConnection
import oracledb

# def getConnection():
#     try:
#         conn = oracledb.connect(user='hr',password='happy',dsn='localhost:1521/xe')
#     except Exception as e:
#         print(e)
#     return conn

def foodListData(page):
    try:
        conn = getConnection()
        cursor = conn.cursor()

        rowSize = 20
        start = (rowSize*page)-(rowSize-1)
        end = (rowSize*page)

        sql = f"""
            SELECT fno,name,poster,num 
            FROM (SELECT fno,name,poster,rownum as num 
            FROM (SELECT fno,name,poster 
            FROM food_menu_house ORDER BY fno)) 
            WHERE num BETWEEN {start} AND {end}
        """
        cursor.execute(sql)
        food_list = cursor.fetchall()
        cursor.close()

        sql = """
            SELECT CEIL(COUNT(*)/20) 
            FROM food_menu_house
        """
        cursor = conn.cursor()
        cursor.execute(sql)
        totalpage = cursor.fetchone()

        cursor.close()
        conn.close()

    except Exception as e:
        print(e)
    
    return food_list,totalpage[0]

def foodCount():
    try:
        conn = getConnection()
        cursor = conn.cursor()

        sql = """
            SELECT COUNT(*) 
            FROM food_menu_house
        """
        cursor = conn.cursor()
        cursor.execute(sql)
        totalpage = cursor.fetchone()
    except Exception as e:
        print(e)
    
    return totalpage[0]

def foodFindData(page,address):
    try:
        conn = getConnection()
        cursor = conn.cursor()

        rowSize = 20
        start = (rowSize*page)-(rowSize-1)
        end = (rowSize*page)

        sql = f"""
            SELECT fno,name,poster,num 
            FROM (SELECT fno,name,poster,rownum as num 
            FROM (SELECT fno,name,poster 
            FROM food_menu_house WHERE address LIKE '%'||'{address}'||'%' ORDER BY fno)) 
            WHERE num BETWEEN {start} AND {end}
        """
        cursor.execute(sql)
        food_list = cursor.fetchall()
        cursor.close()

        sql = f"""
            SELECT CEIL(COUNT(*)/20) 
            FROM food_menu_house WHERE address LIKE '%'||'{address}'||'%'
        """
        cursor = conn.cursor()
        cursor.execute(sql)
        totalpage = cursor.fetchone()

        cursor.close()

        cursor = conn.cursor()

        sql = f"""
            SELECT COUNT(*) 
            FROM food_menu_house WHERE address LIKE '%'||'{address}'||'%'
        """
        cursor = conn.cursor()
        cursor.execute(sql)
        count = cursor.fetchone()

        cursor.close()
        conn.close()

    except Exception as e:
        print(e)
    
    return food_list,totalpage[0],count[0]

def foodDetail(fno):
    try:
        conn = getConnection()
        cursor = conn.cursor()
        sql = f"""
            SELECT 'http://www.menupan.com'||poster,name,type,address,phone,score,theme,price,time,seat 
            FROM food_menu_house 
            WHERE fno={fno}
        """
        cursor.execute(sql)
        food_detail = cursor.fetchone()
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)
    
    return food_detail