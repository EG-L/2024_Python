from django.db import models
import pymysql

def goodsListData(page,tname):
    try:
        conn = pymysql.connect(host='localhost',user='root',password='root',db='mydb',charset='utf8')
        cursor = conn.cursor()
        rowSize = 20
        start = (rowSize*page)-(rowSize-1)
        end = (rowSize*page)
        sql = f"""
            SELECT no,goods_name,goods_price,goods_poster
            FROM {tname}
            ORDER BY no 
            LIMIT {start},20
        """
        cursor.execute(sql)
        header = [row[0] for row in cursor.description]
        goods_data = cursor.fetchall()
        data = [dict(zip(header,goods_data[i])) for i in range(len(goods_data))]
        cursor.close()

        cursor = conn.cursor()
        sql = f"""
            SELECT COUNT(*) FROM {tname}
        """
        cursor.execute(sql)
        count = cursor.fetchone()
        print(count)
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)

    return data,count[0]

def goodsDetailData(no,tname):
    try:
        conn = pymysql.connect(host='localhost',user='root',password='root',db='mydb',charset='utf8')
        cursor = conn.cursor()
        sql = f"""
            SELECT no,goods_name as name,goods_sub as sub,goods_price as price,goods_discount as discount,goods_first_price,goods_delivery as delivery,goods_poster as poster,hit
            FROM {tname} 
            WHERE no={no}
        """
        cursor.execute(sql)
        goods_detail = cursor.fetchone()
        print(cursor.description)
        header = [row[0] for row in cursor.description]
        data = dict(zip(header,goods_detail))

    except Exception as e:
        print(e)
    
    return data