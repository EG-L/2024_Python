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
        # "range":range(startPage,endPage)
    }

    # return render(reqeust,"food/list.html",food_data)
    return JsonResponse(food_data)

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


def food_detail(request):
    try:
        fno = request.GET['fno']
        fd = food_models.foodDetail(int(fno))
        f_detail={
            "poster":fd[0],
            "name":fd[1],
            "type":fd[2],
            "address":fd[3],
            "phone":fd[4],
            "score":fd[5],
            "theme":fd[6],
            "price":fd[7],
            "time":fd[8],
            "seat":fd[9]
        }
    except Exception as e:
        print(e)
    
    return render(request,'food/food_detail.html',f_detail)