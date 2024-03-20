from django.shortcuts import render,redirect
from food import models
# @Controller
# Create your views here.
'''
    urls.py => Router(화면이동)
    models.py => DAO(데이터베이스 연결)
    views.py => Controller(사용자 요청 처리 => 화면 이동)
'''

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

    send_data = {
        'curpage':curpage,
        'totalpage':totalpage,
        'endPage':endPage,
        'startPage':startPage,
        'food_list':food_list,
        'range':range(startPage,endPage)
    }

    return render(request,'food/list.html',send_data)

def food_detail(request):
    return render(request,"food/detail.html",{"msg":"맛집 상세보기"})