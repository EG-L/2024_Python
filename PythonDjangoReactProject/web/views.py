from django.shortcuts import render,redirect
from django.http import JsonResponse
'''
    render(request,"url",값) => forward
    redirect("url") => sendRedirect
    JsonResponse({}) => JSON만 전송 ==> Vue / React => Rest(다른 시스템과 연결시 필요한 시스템)
    => CrossOrigin
'''
from web import models
# Create your views here.
def main_page(request):
    try:
        recipe_data,food_data = models.mainPrintData()
        rd = []
        for r in recipe_data:
            rdata = {
                "no":r[0],
                "title":r[1],
                "poster":r[2],
                "chef":r[3]
            }
            rd.append(rdata)
        fd = []
        for f in food_data:
            fdata = {
                "fno":f[0],
                "name":f[1],
                "poster":f[2]
            }
            fd.append(fdata)
        cdata = models.chefMainData()
        print(cdata)
        tdata = models.todayFoodData()
        print(tdata)
        foodhouse = models.newsData('맛집','O7cbEP6pS73QClRY45Hd','NADfUc10JR')
        print(foodhouse['items'])
        main_data={
            "rd":rd,
            "fd":fd,
            "cd":cdata,
            "td":tdata,
            "nd":foodhouse['items']
        }
    except Exception as e:
        print(e)
    # return render(request,'main/home.html',main_data)
    return JsonResponse(main_data)

