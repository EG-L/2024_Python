from django.urls import path
from recipe import views

# localhost/8000
urlpatterns = [
    path('',views.main_home)
]
