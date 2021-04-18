#__author:  Administrator
#date:  2020/5/16
from django.utils.deprecation import MiddlewareMixin

#自定义中间件
class MyMiddle(MiddlewareMixin):
    def process_request(self,request):
        print("get 参数为：",request.GET.get("a") )