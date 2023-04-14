#__author:  Administrator
#date:  2020/5/10

'''
定义模板
    变量：视图传递给模板的数据,要遵守标识符规则
        语法： {{var}}
        注意：如果使用的变量不存在，则插入的空字符串,
        在模板中使用点语法：字典查询，属性或者方法，数字索引
        在模板中调用对象的方法：  <h1>{{stu.getName}}</h1>
            注意：不能传入参数

    标签：
        语法：{% tag %}
        作用：
            1）在输出中创建一些文本
            2）控制逻辑和循环

        if：
            格式：{% if 表达式 %}         {% if 表达式 %}        {% if 表达式 %}
                    语句                     语句1                  语句1
                  {% endif %}               {% else 表达式 %}      {% elif 表达式 %}
                                             语句2                  语句2
                                          {% endif %}              ……
            示例：                                               {% endif %}
                {% if num %}
                    <h1>sunwenbo is a nice man </h1>
                {% endif %}
        for：
            格式：{% for 变量 in 列表 %}           {% for 变量 in 列表 %}
                    语句                              语句1
                  {% endfor %}                     {% empty %}
                                                      语句2
                                                   {% endfor %}     注意：列表为空或者列表不存在时执行语句2
                    {{forloop.counter}}   不是标签，类似变量，表示当前循环的次数
            示例：
                        {%for student in students%}
                            <li>
                                <a href="student.id">{{forloop.counter}}--{{student.id}}--{{student.sname}}--{{student.sage}}--{{student.scontend}}--{{student.sgrade}}--{{student.lastTime}}--{{student.createTime}}</a>
                            </li>
                        {% empty %}
                            <li>目前没有学生</li>
                        {%endfor%}
        comment：
            作用：注释多行
            格式：{% comment %}
                    注释的内容
                  {% endcomment %}
            示例：
                {% comment %}
                    <h1>sunwenbo is a nice man </h1>
                    <h1>{{stu.sname}}</h1>
                {% endcomment %}
        ifequal/ifnotequal：
            作用：判断是否相当或者不相等
            格式：{% ifequal 值1 值2 %}
                    语句
                  {% endifequal %} #如果值1等于值2显示语句
            示例：  {% ifequal  1 2  %}
                            <li> 相等 </li>
                    {% else %}
                            <li> 不相等 </li>
                    {% endifequal %}
        include：
            作用：加载模板并以标签内的参数渲染
            格式：{% 模板目录 参数1 参数2 %}
    过滤器：
        语法：{{ var|过滤器}}
        作用：在变量被显示前修改该变量
        格式：<h1>{{str|upper}}</h1>
        lower  小写   upper   大写
        过滤器可以传入参数，参数用引号引起来
            join
            格式：列表|join:"#"
            示例：<h1>{{list|join:"#"}}</h1>
            如果一个变量没有被提供，或者值为false，none可以使用默认值
                格式：{{ var|default'good'}}
                示例：
            根据给定格式转换日期为字符串 date
                格式：{{ dateVar|date:'y-m-d'}}
                示例：<h1>{{time1|date:'Y-m-d'}}</h1>

            url：
                作用：反向解析，解析到url为good的url，通过视图展现出html页面
                格式：{% url 'namespace:name' p1 p2 %}
                示例：url(r'^',include('myApp1.urls',namespace="app")),
                      url(r'^good/(\d+)/$', views.good,name="good"),
                      <a href="{% url 'app:good' 1 %}">链接</a>

            block/extends：
                作用：用于模板的继承，可以减少页面的内容的重复定义，实现页面的重用
                block标签：在父模板中预留区域，字模板去填充
                    语法：{% block 标签名 %}
                          {% endblock 标签名 %}
                extends标签：继承模板，需要写在模板文件的第一行
                    语法： {% extends 父模板路径 %}
                示例：定义个父模板
                      定义子模板

            csrf_token：
                作用：用于跨站请求伪造保护
                    某些恶意的网站包含链接、表单、按钮、js利用登录用户在浏览器中认证，从而攻击服务
                格式：{% csrf_token %}
                防止CSRF：在settings文件中MIDDLEWARE增加"django.middleware.csrf.CsrfViewMiddleware" 但是把自己也阻止了
                <form action="/showinfo/" method="post">
                     {% csrf_token %}
            验证码：
                 作用：在用户注册、登录页面的时候使用，为了防止暴利请求，减轻服务器的压力，防止csrf的一种方式


            autoescape：
                作用：用于HTML转义 {{code}}
                    return render(request,'myApp1/index.html',{"code":"<h1>sunwenbo is a very good man </h1>"})
                问题：直接将接收到的code当普通的字符串渲染
                处理：将接收到的字符串当成HTML代码渲染
                语法：
                    {% autoescape off %}
                    {{code}}
                    {% endautoescape %}
                escape:转换为字符串
                safe：转换为HTML代码
                autoescape:批量转义

            加减乘除取余：
                示例：
                    <h1>{{num|add:10}}</h1>
                    <h1>{{num|add:-10}}</h1>
                    <!--num/1*5-->
                    <h1>{% widthratio num 1 5 %}</h1>
                    <!--num/5*1-->
                    <h1>{% widthratio num 5 1 %}</h1>
                    <!--{% var|divisibleby:2 %}-->
                    {% if forloop.counter|divisibleby:2 %}
                        <li style="color:red">
                            {{forloop.counter}}--{{student.id}}--{{student.sname}}
                        </li>
                    {% else %}
                        <li style="color:bule">
                            {{forloop.counter}}--{{student.id}}--{{student.sname}}
                        </li>
                    {% endif %}
    注释：
        单行注释：
            语法：{# 注释内容 #}
            示例：{# <h1>sunwenbo is a nice man </h1> #}
        多行注释：
            格式：
                   {% comment %}
                    注释的内容
                  {% endcomment %}



'''