#__author:  Administrator
#date:  2020/4/12

"""
概述：
    作用：视图接受web请求并响应web请求。
    本质：视图就是一个python中的函数
    响应：网页（重定向和错误视图404，500）  json数据

url配置：
    配置流程：
        1）指定根级url路径，settings.py 文件中的 ROOT_URLCONF='project.urls'
    urlpatterns：一个url实例的列表
        url对象：正则表达式，视图名称，名称（反向解析）
    url匹配正则的注意事项：
        如果想要从url中获取一个值，需要对正则加小括号
        匹配正则前方不需要加反斜杠
        正则前需要加r表示不转义
    引入其他url配置
        在应用中创建urls.py文件，定义本应用的url配置，在工程urls.py文件中使用incloud方法引入

    url的反向解析：
        概述：如果在视图、模板中使用了硬编码的链接，在url配置发生变化是，动态生成链接的地址
        解决：在使用链接时，通过url配置的名称，动态生成url地址
        作用：
            使用url模板

视图函数：
    定义视图：
        本质：一个函数
        视图参数：
            一个HttpRequests的实例    request
            通过正则表达式获取的参数
        位置：一般在views.py文件下定义
    错误视图：
        404视图   找不到网页，url配置不成时返回
            在templates 目录下定义404.html
            request_path 导致错误的网址
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>404页面</title>
            </head>
            <body>
                <h1>页面丢失</h1>
                <h2>{{request_path}}</h2>
            </body>
            </html>
            在settings.py文件中配置404页面
                DEBUG = True    等于true时永远不用调用404页面
                ALLOWED_HOSTS = ['*']

        500视图   在视图代码出现错误，服务器代码
        400视图   错误出现在客户端的操作

HttpRequest对象    获取浏览器给我们的数据
    概述：
        服务器接收http请求后，会根据报文创建一个HttpRequest对象
        视图的第一个参数就是HttpRequest的参数
        django创建的httprequest对象，之后调用视图时传递给视图
    属性：
        path    请求的完整路径，不包括域名和端口号
        methed      表示请求的方式，常用的get，post
        encoding     表示浏览器提交的数据的编码方式一般为utf-8
        GET      类似字典的对象，包含了get请求的所有参数
        POST     类似字典的对象，包含了post请求的所有参数
        FILES    类似字典的对象，包含了所有上传的文件
        COOKIES    字典，包含所有的cookie
        session     类似字典的对象，表示当前会话
    方法：
        is_ajax()
            如果是通过XMLHTTPRequests发起的，返回True.一般返回json数据
        QueryDict对象：
            request对象中的get，post都属于QueryDict对象
            方法：
                get()   根据键获取值   注意：如果有相同键，只能取第一个键的值。
                getlist()       将键的值以列表形式返回，可以获取多个值

    GET 获取浏览器传递过来给服务器的数据
        http://localhost:8000/sunwenbo/get1?a=1&b=2&c=3
        def get1(request):
            a = request.GET.get('a')
            b = request.GET.get('b')
            c = request.GET.get('c')
            return HttpResponse(a + "  " +  "  "+ b + "  " + c)
        http://localhost:8000/sunwenbo/get2?a=1&a=2&c=3
        def get2(request):
            a = request.GET.getlist('a')
            a1 = a[0]
            a2 = a[1]
            c =request.GET.get('c')
            return HttpResponse(a1 + "  " +  "  "+ a2 + "  " + c)
    POST    使用表单提交post请求
        def showregistry(request):
            return render(request,'myApp1/registry.html')
        def registry(request):
            name = request.POST.get("name")
            gender = request.POST.get("gender")
            age = request.POST.get("age")
            hobby=request.POST.getlist("hobby")
            print(name)
            print(gender)
            print(age)
            print(hobby)
            return HttpResponse("aaaa")

            关闭  settting.py  #'django.middleware.csrf.CsrfViewMiddleware',

HttpResponse对象
    概述：
        作用：给浏览器返回数据
        HttpRequest 是由Django创建的，HttpResponse对象由程序猿自己创建
        用法：
            不调用模板，直接返回数据        return HttpResponse("CCCCCCCCCCCC")

            返回数据，调用模板   使用reden方法
            reden：
                原型：reden(request,templateName[context])
                作用：结合数据和模板，返回完整的HTML页面
                参数：
                    request   请求体对象
                    templateName    模板路径
                    context     传递给需要在渲染模板上的数据
                实例：
                    def index(request):
                        return render(request,'myApp1/index.html')
        属性：
            content     表示返回的内容的内容
            charset     编码格式
            status_code     响应状态码   200  304  404
            contend-type    指定输出的MIME类型

        方法：
            init        使用页面内容实例化HttpResponse对象
            write(contend)      以文件的形式写入
            flush()     以文件的形式输出缓冲区
            set_cookie(key.value,max_age=None,exprise=None)
            delete_cookie(key)      删除cookie 注意：如果删除一个不存在的key，就当什么也没操作。

        子类：
            HttpResponseRedirect
                功能：可以重定向
                    from django.http import HttpResponseRedirect
                    def redirect1(request):
                        return HttpResponseRedirect('/sunwenbo/redirect2')
                    def redirect2(request):
                        return HttpResponse("我是重定向后的视图")
                简写：redriect(to) 推荐使用
                        return redirect('/sunwenbo/redirect2')

            JsonResponse
                功能：返回json数据，一般用于异步请求
                __init__(self,data)
                data  字典对象
                注意：Content-type类型为application/json

session（会话保持）
    概述：http协议是无状态的，每次请求都是一次新的请求，不记得以前的请求
    客户端与服务器端的一次通话就是一次会话
    实现状态保持，在客户端或者是服务端存储有关会话的数据
    存储的方式：
        cookie      所有的数据都存在客户端，不要存储敏感的数据
        session     所有的数据存储在服务端，在客户端用cookie存储session_id
    状态保持的目的：在一段时间内，跟踪请求者的状态，可以实现跨页面访问当前的请求者的数据
    注意：不同的请求者之间不会共享这个数据，与请求者是一一对应的
    启用session：
        settings.py 文件中启用  默认是启用session的
            'django.contrib.sessions',
            'django.contrib.sessions.middleware.SessionMiddleware',
    使用session：
        启用session后，每个HttpRequest对象都有一个session数据，就是一个类似字典的对象。
        getkey.default=None    根据键获取session值
        clear()        清空所有的会话
        flush()        删除当前的会话，并删除会话的cookie
    设置session过期时间：
        set_expriy(value)   默认为秒
        如果不设置，两个星期后过期
        整数，
        时间对象
        0    关闭浏览器时失效
        None   永不过期

    存储session的位置
        数据库：
            默认存储在数据库中
        缓存：
            只存储在本地内存中，如果丢失不能找回，比数据库快
        数据库和缓存：
            优先从本地缓存中读取，读取不到再次去数据库中取

    使用redis缓存session
        pip install jdango-redis-sessions
        设置：
            SESSION_ENGINE = 'redis_sessions.session'
            SESSION_REDIS_HOST = 'localhost'
            SESSION_REDIS_PORT = '6379'
            SESSION_REDIS_DB = 0
            SESSION_REDIS_PASSWORD = 'Ssunwenbo'
            SESSION_REDIS_PREFIX = 'session'
"""