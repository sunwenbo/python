#coding:utf-8
# Create your views here.
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from  codis_mon_app.function_model import cluster_status,proxy_status


def index(request):
    return HttpResponse("sunwenbo is a good man")

class ClusterStatus(APIView):
    def post(self, request,*args, **kwargs,):
        response_data = request.query_params
        if request.method == "POST":
            print("post请求")
        zkaddr = str(response_data['zkaddr'])
        cname = str(response_data['cname'])
        print("zkaddr:%s,cname:%s"% (zkaddr,cname))
        nodeexists = cluster_status.NodeExists()
        cluster_data = nodeexists.checkPath(cname,zkaddr)
        return Response(cluster_data,status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            print("get请求")
        request_data = request.query_params
        zkaddr = str(request_data["zkaddr"])
        cname = str(request_data["cname"])
        cluster_info = cluster_status.NodeExists()
        cluster_data = cluster_info.checkPath(cname,zkaddr)
        return Response(cluster_data,status=status.HTTP_200_OK)

class ProxyStatus(APIView):

    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            print("get请求")
        request_data = request.query_params
        zkaddr = str(request_data["zkaddr"])
        cname = str(request_data["cname"])
        proxy_info = proxy_status.CodisProxyinfo()
        proxy_data = proxy_info.SelectProxy(cname,zkaddr)
        return Response(proxy_data, status=status.HTTP_200_OK)

    def post(self, request,*args, **kwargs,):
        response_data = request.query_params
        if request.method == "POST":
            print("post请求")
        zkaddr = str(response_data['zkaddr'])
        cname = str(response_data['cname'])
        print("zkaddr:%s,cname:%s"% (zkaddr,cname))
        proxy_info = proxy_status.CodisProxyinfo()
        proxy_data = proxy_info.SelectProxy(cname,zkaddr)
        return Response(proxy_data,status=status.HTTP_200_OK)

