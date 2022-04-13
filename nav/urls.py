from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='nav-home'),
    path('helloWorld/', views.hello,name='nav-home')
]