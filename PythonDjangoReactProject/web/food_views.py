from django.shortcuts import render,redirect
from web import food_models
from django.http import JsonResponse

def food_list(reqeust):
    try:
        page = reqeust.GET['page']
    except Exception as e:
        page = "1"
    
    curpage = int(page)
    food_list,totalpage = food_models.foodListData(curpage)
    count = food_models.foodCount()
    fd = []
    for data in food_list:
        fd.append({"no":data[0],"name":data[1],"poster":data[2]})

    BLOCK = 10
    if(curpage<=10):
        startPage=1
        endPage=10
    else:
        startPage=(curpage//10)*10
        endPage=startPage+10

    if(endPage>totalpage):
        endPage = totalpage

    food_data = {
        "food_list":fd,
        "curpage":curpage,
        "totalpage":totalpage,
        "endPage":endPage,
        "startPage":startPage,
        "count":count,
        "range":range(startPage,endPage)
    }

    return render(reqeust,"food/list.html",food_data)
    # return JsonResponse(food_data)

def food_find(request):
    try:
        page=request.GET['page']

    except:
        page="1"
    try:
        address=request.GET['address']
    except:
        address="마포"
    
    curpage = int(page)
    food_list,totalpage,count = food_models.foodFindData(curpage,address)
    fd = []
    for data in food_list:
        fd.append({"no":data[0],"name":data[1],"poster":data[2]})

    BLOCK = 10
    if(curpage<=10):
        startPage=1
        endPage=10
    else:
        startPage=(curpage//10)*10
        endPage=startPage+10

    if(endPage>totalpage):
        endPage = totalpage
    print(startPage,endPage)
    food_data = {
        "food_list":fd,
        "curpage":curpage,
        "totalpage":totalpage,
        "endPage":endPage,
        "startPage":startPage,
        "count":count,
        "range":range(startPage,endPage),
        "address":address
    }

    return render(request,"food/find.html",food_data)