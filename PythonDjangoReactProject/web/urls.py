from django.urls import path,include
from web import views,food_views,recipe_views
'''
                    어노테이션을 찾아서 메소드를 호출
    사용자 요청 ===> DispatchServlet ===> Model(@Controller) ==> ViewResolver
                                                                      |
    사용자 요청 ===> urls ===> 함수 ===> HTML
                     |     -----------
                                   |Views <==> models(DAO)
                    요청 사이트 => 어떤 함수를 호출 => 지정
    manage.py => 서버 동작(실행) python manage.py runserver
    urls.py   => 함수 호출 => @RequestMapping
    ---------------------------------------------
    views.py  => @Controller
    models.py => @Repository
    ---------------------------------------------
    => 서버로만 이용? => JSON 송신 => React, Vue.js()
                                            => {{}} => [[]]
    => 파일까지 제어?
    => 한가지만 명확하게 사용이 가능 => ORM
    1. Python => 자료구조 : 코딩테스트
       => List == []
       => Dict == {} => JSON ==> 웹 전송
       => tuple == () => 데이터베이스
'''
urlpatterns = [
    path('',views.main_page),
    path('food/list',food_views.food_list),
    path('food/find',food_views.food_find),
    path('recipe/list',recipe_views.recipeList),
    path('recipe/list_vue',recipe_views.recipe_rest_List),
    path('recipe/find',recipe_views.recipeFind),
    path('recipe/find_vue',recipe_views.recipeFind_vue),
    path('recipe/chef',recipe_views.recipe_chef_view),
    path('recipe/chef_vue',recipe_views.recipe_chef),
    path('food/food_detail',food_views.food_detail),
    path('recipe/detail',recipe_views.recipeDetailView),
    path('recipe/detail_vue',recipe_views.recipeDetail)
]