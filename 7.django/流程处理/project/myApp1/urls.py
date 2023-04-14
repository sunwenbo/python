#__author:  Administrator
#date:  2020/3/30
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
]