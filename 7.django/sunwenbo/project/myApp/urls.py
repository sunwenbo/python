#__author:  Administrator
#date:  2020/3/29
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^(\d+)/(\d+)$',views.detail),
    url(r'^grades/$',views.grades),
    url(r'^students/$',views.students),
    url(r'^grades/(\d+)$', views.gradesStudents),
    url(r'^students/(\d+)$', views.studentsInfo)
]