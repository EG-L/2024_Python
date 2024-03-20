from django.urls import path
from food import views

#사이트 주소에 따라서 화면 이동 => React (Router)

urlpatterns = [
    path('',views.food_list),
    path('detail/',views.food_detail)
]
