from importlib import import_module
from django.contrib import admin
from django.urls import path

from django.conf.urls import url,include
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    url(r'^chat', views.chat, name='chat'),
    url(r'^home', views.homepage,name="index"),
]
