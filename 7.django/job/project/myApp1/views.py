from django.shortcuts import render

# Create your views here.
from django.http import  HttpResponse
def index(request):
    return render(request,'myApp1/index.html')

from .models import Students,Grades

def students(request):
    studentsList = Students.stuObj.all()
    return render(request,'myApp1/students.html',{"students":studentsList})

def students2(request):
    studentsList = Students.stuObj2.filter(sgender=True)
    #return render(request,'myApp1/students.html',{"students":studentsList})
    return HttpResponse("CCCCCCCCCCCC")

#显示前五个学生
def students3(request):
    studentsList = Students.stuObj.all()[0:2]
    return render(request,'myApp1/students.html',{"students":studentsList})

#分页显示学生信息
def stupage(request,page):
    page = int(page)
    studentsList = Students.stuObj.all()[(page -1 ) *4 :page *4]
    return render(request,'myApp1/students.html',{"students":studentsList})

#查询包含某个关键字contains
#查询以某个字开头或结尾startswith  endswith
#查询某个值在一定的范围内in
#gt(大于)  gte(大于等于) lt(小于) lte(小于等于)
#关联查询
#日期
# from django.db.models import Max  avg   count   max  min  sum

from django.db.models import Max
def studentsearch(request):
    #studentsList = Students.stuObj2.filter(sname__contains="孙")
    #studentsList = Students.stuObj2.filter(sname__startswith="孙")
    #studentsList = Students.stuObj2.filter(pk__in=[2,4,6,8])
    #studentsList = Students.stuObj2.filter(sage__gt=30)
    #描述中包含孙文波的三个字的数据属于哪个班级的
    studentsList = Grades.objects.filter(students__scontend__contains="孙文波")
    maxAge = Students.stuObj2.aggregate(Max('sage'))
    print(maxAge)
    return render(request,'myApp1/grades.html',{"grades":studentsList})
    #return render(request,'myApp1/students.html',{"students":studentsList})

#F对象  一个对象里面的A属性和B属性的比较
from django.db.models import F
def grades(request):
    g = Grades.objects.filter(ggirlnum__gt=F('gboynum')+40)
    print(g)
    return HttpResponse("abc")

#Q对象   或关系   取反
from django.db.models import Q
def grades1(request):
    #studentsList = Students.stuObj2.filter(Q(pk__lte=4) | Q(sage__gte=50))
    studentsList = Students.stuObj2.filter(~Q(pk__lte=4))
    return render(request,'myApp1/students.html',{"students":studentsList})

def addstudent(request):
    grade = Grades.objects.get(pk=1)
    stu = Students.createStudents("孙悟空",50,True,"我叫孙悟空",grade,"2020-4-11","2020-4-11")
    stu.save()
    return HttpResponse("AAAAAAA")

def addstudent2(request):
    grade = Grades.objects.get(pk=1)
    stu = Students.stuObj2.createStudents("张学友",50,True,"我叫张学友",grade,"2020-4-11","2020-4-11")
    stu.save()
    return HttpResponse("BBBBBB")