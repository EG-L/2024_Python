from bs4 import BeautifulSoup
import requests
import sqlite3
url = 'https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp'
data = requests.get(url)
xml = data.text
# print(xml)
#database
conn = sqlite3.connect('weather.db')
# cursor = conn.cursor()
# sql = "DROP TABLE IF EXISTS weather"
# cursor.execute(sql)
# cursor.close()
# conn.close()
# print("테이블 삭제 완료")
# cursor = conn.cursor()
# sql = """
#         CREATE TABLE IF NOT EXISTS weather(
#             city text,
#             mode text,
#             wf text,
#             tmn Integer,
#             tmx Integer
#         )
# """
# cursor.execute(sql)
# conn.commit()
# cursor.close()
# conn.close()

#사이트 읽기
# soup=BeautifulSoup(xml,'html.parser')

# for location in soup.find_all("location"):
# #     print(location)
#     try:
#         city=location.find("city").string
#         mode = location.find("mode").string
#         wf = location.find("wf").string
#         tmn = location.find("tmn").string
#         tmx = location.find("tmx").string
#         print(city,mode,wf,tmn,tmx)
#         conn = sqlite3.connect("weather.db")
#         cursor = conn.cursor()
#         sql="INSERT INTO weather VALUES(?,?,?,?,?)"
#         data = (city,mode,wf,tmn,tmx)
#         cursor.execute(sql,data)
#         conn.commit()
#         cursor.close()
#         conn.close()
#     except Exception as e:
#         print(e)
conn = sqlite3.connect("weather.db")
cursor = conn.cursor()
city = input("지역 입력 :")
sql = f"SELECT * FROM weather WHERE city='{city}'"
cursor.execute(sql)
data = cursor.fetchone()
print("지역:{}".format(data[0]))
print("날씨:{}".format(data[2]))
print("온도:{}/{}".format(data[3],data[4]))
