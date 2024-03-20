from django.urls import path
from food import views

#사이트 주소에 따라서 화면 이동 => React (Router)

urlpatterns = [
    path('',views.food_list),
    path('detail/',views.food_detail),
    path('before/',views.food_before),
    path('emp/',views.emp_list)
]
