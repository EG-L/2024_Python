from django.db import models
import oracledb
# Create your models here.
def getConnection():
    try:
        conn = oracledb.connect(user='hr',password='happy',dsn='localhost:1521/xe')
    except Exception as e:
        print(e)
    return conn

def mainPrintData():
    try:
        conn = getConnection()
        cursor = conn.cursor()

        sql = """
            SELECT no,title,poster,chef,rownum 
            FROM (SELECT no,title,poster,chef 
            FROM recipe ORDER BY no) 
            WHERE rownum<=5
        """

        cursor.execute(sql)
        recipe_list = cursor.fetchall()

        cursor.close()

        cursor = conn.cursor()
        sql = """
            SELECT fno,name,poster,rownum 
            FROM (SELECT fno,name,poster 
            FROM food_menu_house ORDER BY fno) 
            WHERE rownum<=8
        """
        cursor.execute(sql)
        food_list = cursor.fetchall()

        cursor.close()
        conn.close()

    except Exception as e:
        print(e)
    
    return recipe_list,food_list

def chefMainData():
    try:
        conn = getConnection()
        cursor = conn.cursor()
        sql = f"""
            SELECT chef,poster,mem_cont1,mem_cont2,mem_cont3,mem_cont7,rownum 
            FROM chef 
            WHERE rownum<=1
        """
        cursor.execute(sql)
        chef_one = cursor.fetchone()
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)
    
    return chef_one

def todayFoodData():
    try:
        conn = getConnection()
        cursor = conn.cursor()
        sql = f"""
            SELECT 'http://www.menupan.com'||poster,name,address,rownum 
            FROM food_menu_house 
            WHERE rownum<=1
        """
        cursor.execute(sql)
        today_house = cursor.fetchone()
    except Exception as e:
        print(e)
    
    return today_house