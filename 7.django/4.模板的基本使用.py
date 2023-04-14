#__author:  Administrator
#date:  2020/3/29
'''
概述：模板是HTML页面，可以根据视图中传递过来的数据进行填充
创建模板目录： 创建templates 目录，在目录下创建对应项目的模板(\sunwenbo\project\templates) 和项目平级
配置路径：修改settings.py文件
    TEMPLATES = [
            'DIRS': [os.path.join(BASE_DIR,'templates')],

定义grades.html和students.html两个模板
    模板语法：{{输出值，可以是变量，也可以是对象属性}}
              {%执行代码段%}

需求：http://localhost:8000/grades
    1)在settings.py文件中新增模板路径，
    2）创建templates目录 ，再创建myApp  ，接着再创建两个模板.html
    3）在urls.py中新增url路径
    写grades.html模板
                <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>班级信息</title>
            </head>
            <body>
                <h1>班级信息列表</h1>
                <ul>
                    <!--[python04,python05,python06]-->
                    {%for grade in grades%}
                    <li>
                        <a href="#">{{grade.gname}}</a>
                    </li>
                    {%endfor%}
                </ul>
            </body>
            </html>
    定义视图：
        def grades(request):
        #去模板里取数据
        gradesList = Grades.objects.all()
        #将数据传递给模板,疤再渲染页面，将渲染好的页面返回给浏览器
        return render(request,'myApp/grades.html',{"grades":gradesList})


#点击班级显示对应班级所有学生
定义urls： url(r'^grades/(\d+)$', views.gradesStudents)

和新建视图： def gradesStudents(request,num):
                grade= Grades.objects.get(pk=num)
                studentsList = grade.students_set.all()
                return render(request,'myApp/students.html',{"students":studentsList})


'''
