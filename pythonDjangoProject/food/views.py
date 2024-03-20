from django.shortcuts import render,redirect
from food import models
import os
# @Controller
# Create your views here.
'''
    urls.py => Router(화면이동)
    models.py => DAO(데이터베이스 연결)
    views.py => Controller(사용자 요청 처리 => 화면 이동)
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def food_list(request):
    try:
        page = request.GET['page']
    except Exception as e:
        page="1"
    curpage = int(page)
    food_data = models.foodListData(curpage)

    BLOCK = 10
    startPage = int(((curpage-1)/BLOCK*BLOCK))+1
    endPage = int(((curpage-1)/BLOCK*BLOCK))+BLOCK
    totalpage = models.foodTotalPage()
    
    if(endPage>totalpage):
        endPage = totalpage
    
    food_list = []
    for food in food_data:
        r={"fno":food[0],"name":food[1],"poster":food[2]}
        food_list.append(r)

    # 쿠키 읽기
        '''
            request.session['id']=id
            => request.session.clear()=> invalid = logout
        '''
    cookie_data = []
    food_cookie = request.COOKIES
    if food_cookie:
        for key in food_cookie:
            if('food' in key):
                data=request.COOKIES.get(key)
                #DB
                db_data = models.foodInfoData(int(data))
                cd = {"fno":db_data[0],"name":db_data[1],"poster":db_data[2]}
                cookie_data.append(cd)
    send_data = {
        'curpage':curpage,
        'totalpage':totalpage,
        'endPage':endPage,
        'startPage':startPage,
        'food_list':food_list,
        'range':range(startPage,endPage),
        'food_cookie':cookie_data[::-1][:5]
    }

    return render(request,'food/list.html',send_data)
def food_before(request):
    fno = request.GET['fno']
    response = redirect(f"/food/detail/?fno={fno}")
    response.set_cookie(key=f"food{fno}",value=str(fno),max_age=60*60*24,path="/")
    return response

def food_detail(request):
    fno = request.GET['fno']
    # request.getParameter("fno")
    fd = models.foodDetailData(int(fno))
    '''
        list : [] => 배열
        dict : {} => Map (JSON)
        tuple : () => 데이터베이스
        set : []
    '''
    detail_data = {
        "fno":int(fno),
        "name":fd[1],
        "poster":fd[2],
        "address":fd[3],
        "phone":fd[4],
        "type":fd[5],
        "time":fd[6],
        "theme":fd[7],
        "seat":fd[8],
        "score":float(fd[9])
    }
    return render(request,"food/detail.html",detail_data)

def emp_list(request):
    emp = pd.read_csv(os.path.join(os.path.dirname(__file__),'EMP.csv'))
    colors_type = ["#CCCCFF","#CCFFCC","#FF73BB"]
    colors=sns.color_palette(colors_type)
    sns.set_palette(colors)
    sns.barplot(x="DEPTNO",y='SAL',data=emp)
    # print(os.path.join(os.path.dirname(__file__)))
    plt.savefig(os.path.join(os.path.dirname(__file__),'static/images/emp.png'))
    plt.switch_backend('agg')
    plt.close()
    return render(request,"emp/list.html")