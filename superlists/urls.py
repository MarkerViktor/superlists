from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from lists import views

urlpatterns = [
    url(r'^$', views.home_page, name='home')
]
