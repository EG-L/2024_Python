from django.http import JsonResponse
from django.shortcuts import render,redirect
from web import goods_models
# 연결 => 요청처리

def goods_list(request):
    try:
        page = request.GET['page']
    except Exception as e:
        page = "1"
    type = request.GET['type']
    tname_data = ['goods_all','goods_best','goods_new','goods_special']
    tname = tname_data[int(type)]

    goods_data,count = goods_models.goodsListData(int(page),tname)

    goods={
        "gd":goods_data,
        "count":count,
        "curpage":int(page)
    }

    return JsonResponse(goods)

def goods_detail(request):
    try:
        no = request.GET['no']
    except Exception as e:
        print(e)
    
    type = request.GET['type']
    tname_data = ['goods_all','goods_best','goods_new','goods_special']
    tname = tname_data[int(type)]

    g_detail = goods_models.goodsDetailData(int(no),tname)

    return JsonResponse(g_detail)
