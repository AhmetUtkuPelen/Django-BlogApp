from django.urls import path
from django.http.response import HttpResponse
from .views import*
from django.contrib import admin


urlpatterns = [
    path('',index,name="home"),
    path('blogs/',blogs,name="blogs"),
    path('blogs/<slug:slug>/',blog_details,name="blog_details"),
    path('category/<slug:slug>/',blogs_by_category,name="blogs_by_category"),
]

admin.site.site_header = "AUP TECH"


admin.site.site_title = "AUP TECH"