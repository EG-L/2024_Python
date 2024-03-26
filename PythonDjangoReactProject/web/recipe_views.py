from django.shortcuts import render,redirect
from web import recipe_models
from django.http import JsonResponse

def recipeList(request):
    try:
        page = request.GET['page']
    except:
        page = "1"
    
    curpage = int(page)
    recipe_list,totalpage = recipe_models.recipeList(curpage)
    rd = []
    for recipe in recipe_list:
        rd.append({"no":recipe[0],"title":recipe[1],"poster":recipe[2]})
    
    BLOCK = 10
    if(curpage<10):
        startPage=1
        endPage=9
    else:
        startPage = (curpage//10)*10
        endPage = startPage+9
    if(endPage>totalpage):
        endPage=totalpage

    data = {
        "list":rd,
        "startPage":startPage,
        "endPage":endPage,
        "curpage":curpage,
        "totalpage":totalpage,
        # "range":range(startPage,endPage)
    }

    # return render(request,'recipe/list.html',data)
    return JsonResponse(data)

def recipeFind(request):
    try:
        page = request.GET['page']
    except:
        page = "1"
    try:
        title = request.GET['title']
    except:
        title = ''
    
    curpage = int(page)
    print(title)
    recipe_list,totalpage = recipe_models.recipeSearch(curpage,title)

    rd = []
    for recipe in recipe_list:
        rd.append({"no":recipe[0],"title":recipe[1],"poster":recipe[2]})
    BLOCK = 10
    if(curpage<10):
        startPage=1
        endPage=9
    else:
        startPage = (curpage//10)*10
        endPage = startPage+9
    if(endPage>totalpage):
        endPage=totalpage

    data = {
        "list":rd,
        "startPage":startPage,
        "endPage":endPage,
        "curpage":curpage,
        "totalpage":totalpage,
        "title":title,
        "range":range(startPage,endPage)
    }

    return render(request,'recipe/find.html',data)

def recipe_rest_List(request):
    try:
        page = request.GET['page']
    except:
        page = "1"
    
    curpage = int(page)
    recipe_list,totalpage = recipe_models.recipeList(curpage)
    rd = []
    for recipe in recipe_list:
        rd.append({"no":recipe[0],"title":recipe[1],"poster":recipe[2]})
    
    BLOCK = 10
    if(curpage<10):
        startPage=1
        endPage=9
    else:
        startPage = (curpage//10)*10
        endPage = startPage+9
    if(endPage>totalpage):
        endPage=totalpage

    data = {
        "list":rd,
        "startPage":startPage,
        "endPage":endPage,
        "curpage":curpage,
        "totalpage":totalpage,
        # "range":range(startPage,endPage)
    }

    # return render(request,'recipe/list.html',data)
    return JsonResponse(data)

def recipeFind_vue(request):
    try:
        page = request.GET['page']
    except:
        page = "1"
    try:
        fd = request.GET['fd']
    except:
        fd = ''
    
    curpage = int(page)
    recipe_list,totalpage = recipe_models.recipeSearch(curpage,fd)

    rd = []
    for recipe in recipe_list:
        rd.append({"no":recipe[0],"title":recipe[1],"poster":recipe[2]})
    BLOCK = 10
    if(curpage<10):
        startPage=1
        endPage=9
    else:
        startPage = (curpage//10)*10
        endPage = startPage+9
    if(endPage>totalpage):
        endPage=totalpage

    data = {
        "list":rd,
        "startPage":startPage,
        "endPage":endPage,
        "curpage":curpage,
        "totalpage":totalpage,
        "fd":fd
    }

    return JsonResponse(data)

def recipe_chef_view(request):


    return render(request,'recipe/chef.html')

def recipe_chef(request):
    try:
        page=request.GET['page']
    except:
        page="1"
    
    curpage = int(page)
    chef_list,totalpage = recipe_models.recipeChefList(curpage)
    cd = []
    for chef in chef_list:
        cd.append({"cno":chef[0],"chef":chef[1],"poster":chef[2],"mem_cont1":chef[3],"mem_cont2":chef[4],"mem_cont3":chef[5]
                   ,"mem_cont7":chef[6]})
    
    BLOCK = 10
    if(curpage<10):
        startPage=1
        endPage=9
    else:
        startPage = (curpage//10)*10
        endPage = startPage+9
    if(endPage>totalpage):
        endPage=totalpage

    data = {
        "list":cd,
        "startPage":startPage,
        "endPage":endPage,
        "curpage":curpage,
        "totalpage":totalpage,
    }

    return JsonResponse(data)

def recipeDetailView(request):
    no=request.GET['no']
    return render(request,"recipe/recipe_detail.html",{"no":no})

def recipeDetail(request):
    no = request.GET['no']
    rd,rdata,stuff = recipe_models.recipe_detail(int(no))
    re_detail={
        "no":int(rd[0]),
        "poster":rd[1],
        "title":rd[2],
        "chef":rd[3],
        "chef_poster":rd[4],
        "chef_profile":rd[5],
        "info1":rd[6],
        "info2":rd[7],
        "info3":rd[8],
        "content":rd[9]
    }
    print(rdata)
    stuff=stuff.split(",")
    rdata=rdata.split("\n")
    print(rdata)
    make=[]
    posters=[]

    for data in range(len(rdata)-1):
        temp = rdata[data].split("^")
        print(temp)
        make.append(temp[0])
        posters.append(temp[1])

    detail={
        "detail":re_detail,
        "posters":posters,
        "make":make,
        "stuff":stuff
    }

    # return render(request,'recipe/recipe_detail',detail)
    return JsonResponse(detail)
    