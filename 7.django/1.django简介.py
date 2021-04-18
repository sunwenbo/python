#__author:  Administrator
#date:  2020/3/23
"""
MVC：让每一个模块独立，解耦，将业务逻辑聚集到一个部件里，在改进和个性化定制界面及用户交互的同时，不需要重新编写业务逻辑
优点：降低各功能模块之间的耦合性，方便变更，更容易重构代码，最大程度上实现代码的重用

Model   模型  管理数据，通常模型对象负责在数据库中存取数据
View    视图   展示数据，通常视图依据模型数据创建的
Controller  控制器  处理用户交互的部分，通常控制器负责从视图读取数据，控制用户输入，并向模型发送数据

Client发起http请求  --->Controller ---->Model（取数据）-----> 返回Controller----> View (向用户展示)---->Client

MTV：本质上和MVC没有什么差别，也是各组件之间为了保持耦合关系，只是定义是有些不同
Model   模型  管理数据，通常模型对象负责在数据库中存取数据
Template  模板  负责将页面展示给用户
View    视图   负责业务逻辑，并适当的调用Model和Template

Client发起http请求  --->View ---->Model（取数据）-----> View----> Template (向用户展示)---->Client

Django还有一个url分发器，他的作用是将一个url的页面请求，分发给不同的view处理，view再调用相应的Model和Template

创建一个项目：
django-admin startproject project


E:\PYTHON笔记\7.DJANGO\SUNWENBO
└─project
    │  manage.py      一个命令行工具，可以使我们用多种方式对Django项目进行交互
    │
    └─project
            settings.py     项目的配置文件
            urls.py         项目的URL声明
            wsgi.py         项目与wsgi兼容的web服务器入口
            __init__.py    一个空文件，它告诉python这个目录应该被看作一个python包
1.
__init__.py 导入一下两行代码
import pymysql
pymysql.install_as_MySQLdb()

2.
settings,py 修改成以下
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "sunwenbo",
        'USER': "root",
        'PASSWORD': "1qaz2wsx",
        'HOST': "localhost",
        'PORT': "3306",
    }
}
3.
黑名终端到相应的目录下，执行以下命令 创建应用
python manage.py startapp myApp

将应用添加到settings.py INSTALLED_APPS 后面

4.定义模型：
概述：有一个数据库，就对应有一个模型
在modeis.py文件中定义模型， 引入from django.db import models  模型类要继承models.Model


class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateField()
    ggirlnum = models.IntegerField()
    bboynum = models.IntegerField()
    isDelete = models.BooleanField()

class Students(models.Model):
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    #关联外键
    sgrade = models.ForeignKey("Grades")
    说明：不需要定义主键，主键会在生成时自动添加，并且值为自动增加

5.
生成数据表：
     1）生成迁移文件   在migrations生成了一个迁移文件，此时数据库还没有数据表
        E:\python笔记\7.django\sunwenbo\project>python manage.py makemigrations
     2）执行迁移   相当于执行了sql语句创建数据表
        E:\python笔记\7.django\sunwenbo\project>python manage.py migrate

6.
测试数据操作：
      1）进入python shell 环境
      E:\python笔记\7.django\sunwenbo\project>python manage.py shell
      2）from myApp.models import Grades,Students
        from django.utils import timezone
        from datetime import *
    3) 查询所有数据  格式：类名.objects.all()
         Grades.objects.all()
    4) 添加数据 本质：创建一个模型类的对象实例
        grade1 = Grades()
        grade1.gname = "python04"
        grade1.gdate = datetime(year=2020,month=7,day=17)
        grade1.ggirlnum = 3
        grade1.bboynum = 30
        grade1.save()
        grade2 = Grades()
        grade2.gname = "python05"
        grade2.gdate = datetime(year=2020,month=6,day=20)
        grade2.ggirlnum = 5
        grade2.bboynum = 40
        grade2.save()

    5) 查看某个对象 格式类名.方法(条件)
        Grades.objects.get(pk = 2)
        g =  Grades.objects.get(pk = 2)

    6) 修改数据  模型对象.属性 = 新值
        grade2.bboynum = 50
        grade2.save()
    7）删除数据 模型对象.delete()  注意：物理删除，数据库中的表里面的数据被删除
        grade2.delete()
    8) 关联对象(外键)
        stu = Students()
        stu.sname = "孙文波"
        stu.sgender = True
        stu.sage = 20
        stu.scontend = "我是孙文波"
        sut.sgrade = grade1    #关联对象
        获取python04班级中所有的学生  格式：对象名.关联的类名小写_set.all()
        grade1.students_set.all()
        创建,属于python04班级
        stu2 = grade1.students_set.create(sname=u'曾志伟',sgender = True,scontend='我叫曾志伟',sage = 45)
        直接添加到数据库中

7.
启动服务器
    1) python manage.py runserver ip:port
    ip 可以不写，默认是本机
    端口号默认是8000
    说明：这是一个纯python写的轻量级web服务器，仅仅在开发测试中使用

"""










