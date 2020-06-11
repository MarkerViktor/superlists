from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from lists import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^lists/personal-list/$', views.view_lists, name='view_lists')
]
