#__author:  Administrator
#date:  2020/5/16

'''
一、静态文件
    css、js、图片 、json文件 、字体文件等
        <link rel="stylesheet" type="text/css" href="/static/myApp1/css/style.css">
        <script type="text/javascript" src="/static/myApp1/js/test.js"></script>
        <img src="/static/myApp1/image/123.png">
    普通文件用
    配置settings.py文件
        STATICFILES_DIRS = [
            os.path.join(BASE_DIR,'static')
        ]

二、中间件

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
    概述：一个轻量级、底层的插件，可以介入Django请求和响应
    本质：一个Python类
    方法：
        __init__：不需要传参数，服务器响应第一个请求的时候自动调用，用于确定是否启用该中间件
        process_request(self,request):在执行视图之前被调用（分配url匹配视图之前），每个请求上都会调用，返回None或者HttpReponse对象
        process_view(self,request,view_func,view_args,view_kwargs)：调用视图之前执行，每个请求都会调用，返回None或者HttpReponse对象
        process_template_response(self,request,response)：在视图刚好执行完后调用，每个请求都会调用，返回None或者HttpReponse对象，使用render返回模板
        process_response(self,request,response)：返回浏览器之前调用，每个请求都会调用，返回HttpReponse对象
        process_execption(self,request,exception)：当视图跑出异常时调用，返回HttpReponse对象
    自定义中间件：工程middleare目录下创建myapp1目录下
    创建一个Python文件，
    使用自定义中间件，配置settings.py文件  MIDDLEWARE[ + ]
    测试中间件：http://localhost:8000/?a=1
三、上传图片
    概述：文件上传时，文件数据存储在request.FILES属性中,
    注意：form表单要上文件需要加enctype="multipart/form-data"，上传文件必须是post请求
    储存路径：在static目录下创建一个upfile目录下用于存储接收上传文件，配置settings.py文件  MDEIA_ROOT=os.path.join(BASE_DIR,r'static\upfile')
    示例：
        def upfile(request):
        return render(request,'myApp1/upfile.html')
        def savefile(request):
            if request.method == "POST":
                f = request.FILES["file"]
                filePath = os.path.join(settings.MDEIA_ROOT,f.name)
                with open(filePath,'wb') as fp:
                    #chunks 文件分段接收
                    for info in f.chunks():
                        fp.write(info)
                return HttpResponse("上传成功")
            else:
                return HttpResponse("上传失败")
四、分页
    Paginator对象：
        创建对象：
            格式：Paginator[列表，整数]
            返回值：返回一个分页对象
        属性：
            count 对象总数
            num_pages  页面总数
            page_range  页码列表 [1,2,3,4,5]  页码从1开始

        方法：page{num}
            作用：获得一个page对象，如果提供的页码不存在会抛出一个异常'invalidPage'异常
        异常：
            invalidPage:当page()传递时一个无效的页码时触发这个异常
            pageNotAnInteger：当向page{}传递的不是一个整数时触发
            EmptyPage：当向page{}传递一个有效值，但是该页面上没有数据时触发

    Paginator对象与Page对象的关系：查询数据库返回查询结果，paginator对象接收，设置每页接收数据的条数，来决定共有多少页，创建page对象用于存储对应页数的数据
    Page对象：
        创建对象：Paginator对象的page()方法返回Page对象，不需要手动创建
        属性：
            object_list：当前页所有的数据{对象}列表
            number：当前页的页码值
            paginator：当前page对象关联的paginator对象
        方法：
            has_next()：判断是否有下一页，如果有返回True
            has_previous()：判断是否有上一下，如果有返回True
            has_other_pages：判断是否有上一页或者下一页，如果有返回True
            next_number()：返回下一页的页码，如果下一页不存在，抛出invalidPage异常
            previous_number()：返回上一页的页码，如果上一页不存在，抛出invalidPage异常
            len()：返回当前页的数据{对象}个数

五、ajax
    概述：网页需要动态生成，返回json数据
    步骤1：
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>学生列表</title>
            <script type="text/javascript" src="/static/myApp1/js/jquery-1.4.4.min.js"></script>
        </head>
        <body>
            <h1>学生信息列表</h1>
            <button id ="btn">显示学生信息</button>
            <script type="text/javascript" src="/static/myApp1/js/students.js"></script>
        </body>
        </html>
    步骤2：
        console.log("##############")
        $(document).ready(function() {
            document.getElementById("btn").onclick = function(){
                $.ajax({
                    type:"get",
                    url:"/studentsinfo/",
                    dataType:"json",
                    success:function(data,status){
                        console.log(data)
                        var d = data["data"]
                        for(var i = 0; i < d.length;i++)
                        document.write('<p>'+d[i][0]+'</p>')
                    }
                })
            }
        })
    步骤3：
        配置url及创建对应视图
            url(r'^ajaxstudents/$',views.ajaxstudents),
            url(r'^studentsinfo/$', views.studentsinfo),

            def ajaxstudents(request):
                return render(request,'myApp1/ajaxstudents.html')
            from django.http import JsonResponse
            def studentsinfo(request):
                stus = Students.stuObj2.all()
                list = []
                for stu in stus:
                    list.append([stu.sname,stu.sage])
                return JsonResponse({"data":list})
六、富文本：
    概述：
    pip install django-tinymce
    1) 在站点中使用
        1.配置settings.py文件，INSTALLED_APPS 中添加  'tinymce',
        #富文本
        TINYMCE_DEFAULT_CONFIG = {
            'theme':'advanced',
            'width':600,
            'height':400,
        }
        2.创建一个模型类，models
        from tinymce.models import HTMLField
        class Text(models.Model):
            str = HTMLField
        3.配置站点
        from .models import Text
        admin.site.register(Text)
        4.生成迁移文件
        python manage.py makemigrations
        5.执行迁移文件
        python manage.py migrate

    2）在自定义视图中使用
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>富文本</title>
            <script type="text/javascript" src="/static/tiny_mce/tiny_mce.js"></script>
            <script type="text/javascript">
                tinyMCE.init({
                    'mode':'textareas',
                    'theme':'advanced',
                    width:'800',
                    'height':600,
                })
            </script>
        </head>
        <body>
            <form action="/savefile/" method="post">
                <textarea name="str">sunwenbo is a good man</textarea>
                <input type="submit" value="提交"/>
            </form>
        </body>
        </html>

七、celery
Celery 是什么?

Celery 是一个由 Python 编写的简单、灵活、可靠的用来处理大量信息的分布式系统,它同时提供操作和维护分布式系统所需的工具。

Celery 专注于实时任务处理，支持任务调度。

说白了，它是一个分布式队列的管理工具，我们可以用 Celery 提供的接口快速实现并管理一个分布式的任务队列。


    相关文档：http://docs.jinkan.org/docs/celery/
    问题：
        用户发起request，并且要等待response返回，但是在视图中有一些耗时的操作，导致用户可能会等待很长时间才能接收response，会影响用户体验
        网站每隔一段时间要同步一次数据，但是http请求是需要触发的
    解决：celery
        方式1，将耗时的操作放到celery中执行
        方式2，使用celery定时执行
    celery：
        任务task：本质是一个python函数，将耗时操作封装成一个函数
        队列queue：将要执行的任务放到队列里
        工人worker：负责执行队列中的任务
        代理broker：负责调度，在部署环境中使用redis
    安装celery：
        pip install celery
        pip install celery-with-redis
        pip install django-celery
    配置settings.py：
        1.INSTALLED_APPS = [] 中添加 'djcelery',
        2.新增
        #celery配置
        import djcelery
        djcelery.setup_loader() #初始化
        BROKER_URL='redis://39.106.133.114:6379/0'
        #BROKER_URL='redis://:sunwenbo@127.0.0.1:6379/0'
        #              格式：  密码@IP:端口号/库
        CELERY_IMPORTS={'myApp1.task'}

        3.在应用目录（myApp1）下创建task.py文件

        4.迁移，生产celery需要的数据库表

        5.在工程目录下project目录下创建celery.py文件
            from __future__ import absolute_import
            import os
            from celery import Celery
            from django.conf import settings
            os.environ.setdefault('DJANGO_SETTINGS_MODULE','whthas_home.settings')

            app = Celery('portal')

            app.config_from_object('django.conf:settings')
            app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

            @app.task(bin=True)
            def debug_task(self):
                print('Request: {0!r}'.format(self.request))

        6.在工程目录(project)下的__init__.py文件中添加
            from .celery import app as celery_app


'''