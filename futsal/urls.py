from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('bb/', views.homepage),
    path('aibaan/', views.aibaan, name = 'khele'),
    path('mainkaam/', views.inputpage),
    path('countpage/', views.countpage, name = 'count'),
]
