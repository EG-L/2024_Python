from web.models import getConnection
import oracledb

def recipeList(page):
    try:
        conn = getConnection()
        cursor = conn.cursor()
        rowSize= 12
        start = (page*rowSize)-(rowSize-1)
        end = (page*rowSize)
        sql = f"""
            SELECT no,title,poster,num 
            FROM (SELECT no,title,poster,rownum as num 
            FROM (SELECT no,title,poster 
            FROM recipe ORDER BY no)) 
            WHERE num BETWEEN {start} AND {end}
        """
        cursor.execute(sql)
        recipe_list = cursor.fetchall()

        cursor.close()

        cursor = conn.cursor()

        sql = """
            SELECT CEIL(COUNT(*)/12) 
            FROM recipe
        """
        cursor.execute(sql)
        totalpage = cursor.fetchone()

        cursor.close()

    except Exception as e:
        print(e)
    
    return recipe_list,totalpage[0]

def recipeSearch(page,title):
    try:
        conn = getConnection()
        cursor = conn.cursor()
        rowSize= 12
        start = (page*rowSize)-(rowSize-1)
        end = (page*rowSize)
        sql = f"""
            SELECT no,title,poster,num 
            FROM (SELECT no,title,poster,rownum as num 
            FROM (SELECT no,title,poster 
            FROM recipe WHERE title LIKE '%'||'{title}'||'%' ORDER BY no)) 
            WHERE num BETWEEN {start} AND {end}
        """
        cursor.execute(sql)
        recipe_list = cursor.fetchall()

        cursor.close()

        cursor = conn.cursor()

        sql = f"""
            SELECT CEIL(COUNT(*)/12) 
            FROM recipe WHERE title LIKE '%'||'{title}'||'%'
        """
        cursor.execute(sql)
        totalpage = cursor.fetchone()

        cursor.close()

    except Exception as e:
        print(e)
    
    return recipe_list,totalpage[0]

def recipeChefList(page):
    try:
        conn = getConnection()
        cursor = conn.cursor()
        rowSize= 20
        start = (page*rowSize)-(rowSize-1)
        end = (page*rowSize)
        '''
            CNO                                       NOT NULL NUMBER
            CHEF                                      NOT NULL VARCHAR2(100)
            POSTER                                    NOT NULL VARCHAR2(500)
            MEM_CONT1                                          NUMBER
            MEM_CONT2                                          NUMBER
            MEM_CONT3                                          NUMBER
            MEM_CONT7                                          NUMBER
        '''
        sql = f"""
            SELECT cno,chef,poster,mem_cont1,mem_cont2,mem_cont3,mem_cont7,num
            FROM (SELECT cno,chef,poster,mem_cont1,mem_cont2,mem_cont3,mem_cont7,rownum as num 
            FROM (SELECT cno,chef,poster,mem_cont1,mem_cont2,mem_cont3,mem_cont7 
            FROM chef ORDER BY cno)) 
            WHERE num BETWEEN {start} AND {end}
        """
        cursor.execute(sql)

        chef_list = cursor.fetchall()
        cursor.close()

        cursor = conn.cursor()

        sql = """
            SELECT CEIL(COUNT(*)/20) 
            FROM chef
        """

        cursor.execute(sql)

        totalpage = cursor.fetchone()
        cursor.close()
        conn.close()
        

    except Exception as e:
        print(e)
    
    return chef_list,totalpage[0]

def recipe_detail(no):
    try:
        conn = getConnection()
        cursor = conn.cursor()
        print(no)
        sql = f"""
            SELECT * 
            FROM recipeDetail WHERE no={no}
        """
        cursor.execute(sql)
        dt = cursor.fetchone()
        stuff,rdata = ''.join(dt[-1].read()),''.join(dt[-2].read())
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)
    return dt,rdata,stuff