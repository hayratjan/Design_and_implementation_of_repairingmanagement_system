from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('register/', views.register, name="register"),
    path('password_update/', views.password_update, name="password_update"),
    path('add_repair/', views.add_repair, name="add_repair"),
    path('record/', views.record, name="record"),
]
