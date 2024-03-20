import urllib.request as req
from bs4 import BeautifulSoup
import requests

def request(url):
    response=req.urlopen(url)
    byte_data = response.read()
    text_data = byte_data.decode('UTF-8')

    return text_data

for page in range(1,6):

    url = 'https://www.10000recipe.com/recipe/list.html?order=reco&page='+str(page)
    webpage = request(url)
    # print(webpage)
    #Document doc = Jsoup.connection(url).get()
    res = req.urlopen(url)
    soup = BeautifulSoup(res,'html.parser')
    aTitle = soup.select('div.common_sp_caption div.common_sp_caption_tit')
    aChef = soup.select('div.common_sp_caption div.common_sp_caption_rv_name a')
    aImage = soup.select('div.common_sp_thumb img[src*="/recipe/"]')
    '''

    '''
    for i in range(len(aTitle)):
        print(aTitle[i].text)
        print(aChef[i].text)
        print(aImage[i]['src'])
    print("============================================================")