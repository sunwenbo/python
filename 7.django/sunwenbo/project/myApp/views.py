from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("sunwenbo is a good man")
def detail(request,num,nums):
    return HttpResponse("detail-%s-%s" % (num,nums))

from . models import Grades,Students
def grades(request):
    #去模型里取数据
    gradesList = Grades.objects.all()
    #将数据传递给模板,疤再渲染页面，将渲染好的页面返回给浏览器
    return render(request,'myApp/grades.html',{"grades":gradesList})

def students(request):
    #去模型里取数据
    studentsList = Students.objects.all()
    print(studentsList)
    #将数据传递给模板,模板再渲染页面，将渲染好的页面返回给浏览器
    return render(request,'myApp/students.html',{"students":studentsList})

#点击班级显示对应班级所有学生
def gradesStudents(request,num):
    #获得对应的班级对象
    grade= Grades.objects.get(pk=num)
    print("####",grade)
    # 获得对应的班级下的所有学生列表
    studentsList = grade.students_set.all()
    return render(request,'myApp/students.html',{"students":studentsList})

def studentsInfo(request,num):
    #获得对应的班级对象
    student= Students.objects.get(pk=num)
    # 获得对应的班级下的所有学生列表
    studentsList = student.students_set.all()
    return render(request,'myApp/grades.html',{"students":studentsList})


