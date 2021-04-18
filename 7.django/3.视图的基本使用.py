#__author:  Administrator
#date:  2020/3/29
'''
概述：在Django中，视图对web请求进行回应
      视图就是一个python函数，在views.py中创建

定义视图：
from django.http import HttpResponse

def index(request):
    return HttpResponse("sunwenbo is a good man")

配置url：
    修改project下的url.py 文件
    urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('myApp.urls')),
    ]

    修改myApp下的urls.py
    from django.conf.urls import url
    from . import views

    urlpatterns = [
        url(r'^$',views.index)
    ]
'''