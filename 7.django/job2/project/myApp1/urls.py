#__author:  Administrator
#date:  2020/3/30
from django.conf.urls import url
from . import views
app_name = 'myApp1'
urlpatterns = [
    url(r'^$',views.index),
    url(r'^students/$',views.students),
    url(r'^students2/$', views.students2),
    url(r'^students3/$', views.students3),
    url(r'^stu/(\d+)/$', views.stupage),
    url(r'^studentsearch/$', views.studentsearch),
    url(r'^addstudent/$',views.addstudent),
    url(r'^addstudent2/$',views.addstudent2),
    url(r'^grades/$',views.grades),
    url(r'^grades1/$',views.grades1),

    url(r'index1.html',views.index1),
    url(r'^attribles/$',views.attribles),
    url(r'^get1/$',views.get1),
    url(r'^get2/$', views.get2),
    url(r'^showregistry/$', views.showregistry),
    url(r'^showregistry/registry/$', views.registry),
    url(r'^showresponse/$', views.showresponse),
    url(r'^cookietest/$',views.cookietest),
    url(r'^redirect1/$', views.redirect1),
    url(r'^redirect2/$', views.redirect2),
    url(r'^main/$', views.main),
    url(r'^login/$', views.login),
    url(r'^showmain/$', views.showmain),
    url(r'^quit/$', views.quit),
    url(r'^good/(\d+)/(\d+)/$', views.good,name="good"),
    url(r'^main1/$', views.main1),
    url(r'^main2/$', views.main2),
    url(r'^postfile/$', views.postfile),
    url(r'^showinfo/$', views.showinfo),
    url(r'^verifycode/$', views.verifycode),
    url(r'^verifycodefile/$', views.verifycodefile),
    url(r'^verifycodefilecheck/$', views.verifycodefilecheck),
    url(r'^upfile/$', views.upfile),
    url(r'^savefile/$', views.savefile),
    url(r'^studentpage/(\d+)/$', views.studentpage),
    url(r'^ajaxstudents/$',views.ajaxstudents),
    url(r'^studentsinfo/$', views.studentsinfo),
    url(r'^edit/$', views.edit),
    url(r'^celery/$', views.celery),

]