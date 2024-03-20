from django.shortcuts import render
from recipe import models
# Create your views here.
'''
    프로젝트 생성() django-admin startproject config .
    
    python manage.py migrate

    슈퍼유저 생성 python manage.py createsuperuser

    앱 생성 (python manage.py startapp recipe)

    python manage.py runserver 서버 실행

    urls.py 설정

    setting.py => INSTALL_APPS => recipe

    config 폴더 내 urls에 include 추가

    static / templates를 만들어서 html을 저장

'''

def main_home(request):

    return render(request,"main/home.html")