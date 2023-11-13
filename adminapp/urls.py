from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.adminhome),
    path('addcourse/',views.addcourse),
    path('courselist1/',views.courselist1),
    path('editcourse/',views.editcourse),
    path('addbatch/',views.addbatch),
    path('addcourse1/',views.addcourse1),
    path('studentlist/',views.studentlist),
    path('logout2/',views.logout2),
]