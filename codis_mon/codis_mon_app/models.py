from django.db import models
# Create your models here.

class Clusters(models.Model):
    cid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=50)
    zkaddr = models.CharField(max_length=20)
    dashboardurl = models.CharField(max_length=50)
    proxy_list = models.CharField(max_length=200,default=None)
    group_num = models.IntegerField()
    sentinel_list = models.CharField(max_length=100)
    start_time = models.CharField(max_length=20)
    sent_sync = models.BooleanField(default=True)
    ishealth = models.BooleanField(default=True)
    def __str__(self):
        return self.cname

class Proxys(models.Model):
    pid = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=50)
    proxy_addr =  models.CharField(max_length=100)
    proxy_max_clients = models.CharField(max_length=6,default=None)
    admin_addr =  models.CharField(max_length=40,default=None)
    product_name =  models.CharField(max_length=30)
    start_time = models.CharField(max_length=20)
    proxy_status = models.BooleanField(default=True)
    def __str__(self):
        return self.pname

class Groups(models.Model):
    gid = models.AutoField(primary_key=True)
    gname = models.CharField(max_length=30)
    server_num = models.IntegerField()
    server_ip = models.CharField(max_length=30)
    replica_group = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    action_state = models.BooleanField(default="synced")
    def __str__(self):
        return self.action_state


class topom(models.Model):
    admin_addr =  models.CharField(max_length=50)
    product_name =  models.CharField(max_length=50)
    start_time = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    def __str__(self):
        return self.admin_addr