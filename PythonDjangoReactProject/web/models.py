from django.db import models
import oracledb
import os
import sys
import urllib.request
import json
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
        a = [row[0] for row in cursor.description]
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)

    return dict(zip(a,chef_one))

def todayFoodData():
    try:
        conn = getConnection()
        cursor = conn.cursor()
        sql = f"""
            SELECT poster,name,address,jjimcount,hit,theme,rownum 
            FROM food_menu_house 
            WHERE rownum<=1
        """
        cursor.execute(sql)
        today_house = list(cursor.fetchone())
        a = [row[0] for row in cursor.description]

        today_house[0] = 'http://www.menupan.com'+today_house[0]

    except Exception as e:
        print(e)
    
    return dict(zip(a,today_house))

def newsData(fd,client_id,client_secret):
    encText = urllib.parse.quote(fd)
    url = "https://openapi.naver.com/v1/search/news.json?query=" + encText # JSON 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        # print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)
        
    return json.loads(response_body.decode('utf-8'))