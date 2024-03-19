from django.contrib import admin
from django.urls import path
from myFirstProject import views

urlpatterns = [
    path('', views.index),
    path('second/', views.second_page),
    path('1/', views.index1),
    path('2/', views.index2),
    path('3/', views.index3),
    path('4/', views.index4),
    path('5/', views.index5)
]
