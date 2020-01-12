from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('bb/', views.homepage),
    path('', views.inputpage),
    path('aibaan/', views.aibaan, name = 'khele'),
    path('mainkaam/', views.inputpage),
    path('wtf/', views.notvalid),
    path('countpage/', views.countpage, name = 'count'),
]
