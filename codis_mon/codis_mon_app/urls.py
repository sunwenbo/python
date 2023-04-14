from django.conf.urls import url
from . import views
from rest_framework import routers,serializers,viewsets


urlpatterns = [
    url(r'^$',views.index),
    url(r'^cluster_status$',views.ClusterStatus.as_view()),
    url(r'^proxy_status$', views.ProxyStatus.as_view()),

    #url(r'^(\d+)/(\d+)$',views.detail),
    # url(r'^students/$',views.students),
]