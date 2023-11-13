from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.studenthome),
    path('courselist3/',views.courselist3),
    path('batchlist1/',views.batchlist1),
    path('admission/',views.admission),
    path('success/',views.success),
    path('logout1/',views.logout1),
    
]