from django.shortcuts import render
import datetime
# Create your views here.
from django.http import  HttpResponse,HttpResponseRedirect
from .models import Students,Grades
def index1(request):
    return HttpResponseRedirect('')
def index(request):
    student = Students.stuObj2.get(pk = 3)
    student1 = Students.stuObj2.get(pk=1)
    time1 = datetime.datetime.now()
    return render(request,'myApp1/index.html',{"stu":student,"num":10,"str":"sunwenbo is a good man","list":["good","nice"],"test":None,"time1":time1,"code":"<h1>sunwenbo is a very good man </h1>"})

def students(request):
    studentsList = Students.stuObj.all()
    return render(request,'myApp1/students.html',{"students":studentsList})

def students2(request):
    studentsList = Students.stuObj2.filter(sgender=True)
    #return render(request,'myApp1/students.html',{"students":studentsList})
    return HttpResponse("CCCCCCCCCCCC")

#显示前五个学生
def students3(request):
    studentsList = Students.stuObj.all()[0:4]
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

def attribles(request):
    print(request.path)
    print(request.method)
    print(request.encoding)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)
    return HttpResponse("attribles")

#获取get从传递的数据
def get1(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    return HttpResponse(a + "  " +  "  "+ b + "  " + c)
def get2(request):
    a = request.GET.getlist('a')
    a1 = a[0]
    a2 = a[1]
    c =request.GET.get('c')
    return HttpResponse(a1 + "  " +  "  "+ a2 + "  " + c)
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
#response
def showresponse(request):
    res = HttpResponse()
    res.content = b'good    '
    print(res.content)
    print(res.charset)
    print(res.status_code)
    print(res.content-type)
    return res

#cookie
def cookietest(request):
    res = HttpResponse()
    cookie = request.COOKIES
    res.write("<h1>"+cookie["sunwenbo"]+"</h1>")
    cookie = res.set_cookie("sunwenbo","good")
    return res

#重定向
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
def redirect1(request):
    #return HttpResponseRedirect('/sunwenbo/redirect2')
    return redirect('/sunwenbo/redirect2')
def redirect2(request):
    return HttpResponse("我是重定向后的视图")


#session使用
def main(request):
    #取session
    username = request.session.get('name',"游客")
    return render(request,'myApp1/main.html',{'username':username})
def login(request):
    return render(request,'myApp1/login.html')
def showmain(request):
    username = request.POST.get('username')
    #存储session
    request.session['name'] = username
    #设置session的保存时间为10秒
    request.session.set_expiry(10)
    return redirect('/sunwenbo/main')
from django.contrib.auth import logout
def quit(request):
    #清除session
    #request.session.clear()
    #request.session.flush()
    logout(request)
    return redirect('/sunwenbo/main')

def good(request,id,id2):
    return render(request, 'myApp1/good.html',{"num":id},{"num2":id2})
def main1(request):
    return render(request,'myApp1/main1.html')
def main2(request):
    return render(request,'myApp1/main2.html')
def postfile(request):
    return render(request,'myApp1/postfile.html')
def showinfo(request):
    name = request.POST.get('username')
    pwd = request.POST.get('password')
    return render(request,'myApp1/showinfo.html',{"username":name,"password":pwd})
from PIL import Image,ImageDraw,ImageFont
import random
def verifycode(request):
    #引入绘图模块
    from PIL import Image,ImageDraw,ImageFont
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20,100),random.randrange(
        20,100),random.randrange(20,100))
    width = 100
    height = 50
    #创建画面对象
    im = Image.new('RGB',(width,height),bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数回执噪点
    for i in range(0,100):
        xy = (random.randrange(0,width),random.randrange(0,height))
        fill = (random.randrange(0,255),255,random.randrange(0,255))
        draw.point(xy,fill=fill)
    #定义验证码的备选值
    str="1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
    #随机选取4个值为验证码
    rand_str = ''
    for i in range(0,4):
        rand_str += str[random.randrange(0,len(str))]
    #构造字体对象
    font = ImageFont.truetype(r'C:\Windows\Fonts\CENTURY.TTF',40)
    #构造字体颜色
    fontcolor1 = (255,random.randrange(0,255),random.randrange(0,255))
    fontcolor2 = (255,random.randrange(0,255),random.randrange(0,255))
    fontcolor3 = (255,random.randrange(0,255),random.randrange(0,255))
    fontcolor4= (255,random.randrange(0,255),random.randrange(0,255))
    #绘制4个字
    draw.text((5,2),rand_str[0],font=font,fill=fontcolor1)
    draw.text((25,2),rand_str[1],font=font,fill=fontcolor2)
    draw.text((50,2),rand_str[2],font=font,fill=fontcolor3)
    draw.text((75,2),rand_str[3],font=font,fill=fontcolor4)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    request.session['verify'] = rand_str
    #内存文件操作
    import io
    buf = io.BytesIO()
    im.save(buf,'png')
    return HttpResponse(buf.getvalue(),'image/png')

def verifycodefile(request):
    f = request.session.get("flag", True)
    str = ""
    if f == False:
        str = "请重新输入"
    request.session.clear()
    return render(request,'myApp1/verifycodefile.html',{"flag":str})
def verifycodefilecheck(request):
    code1 = request.POST.get("verifycode").upper()
    code2 = request.session['verify'].upper()
    if code1 == code2 :
        return render(request,'myApp1/success.html')
    else:
        request.session["flag"] = False
        return redirect('/verifycodefile')

def verifycode1(request):
    # 创建画布
    # mode  模式,"RGB"
    # size  画布的尺寸
    image = Image.new("RGB", (200, 70), createcolor())
    imageDraw = ImageDraw.Draw(image, "RGB")
    imageFont = ImageFont.truetype(r"C:\Users\Administrator.PC-20181025PPBX\Desktop\CENTURY.TTF", size=50)
    # imageDraw.text((5,10),"i love you!",fill=createcolor(),font=imageFont)
    import io
    charsource = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"

    sum = ""
    for i in range(4):
        ch = random.choice(charsource)
        imageDraw.text((15 + i * 50, 10), ch, fill=createcolor(), font=imageFont)
        sum += ch
    # 通过session记录这个验证码并且设置过期时间为60秒
    request.session["verCode"] = sum
    request.session.set_expiry(60)
    # 画麻子
    for i in range(2000):
        x = random.randint(0, 200)
        y = random.randint(0, 70)
        imageDraw.point((x, y), fill=createcolor())

    # 创建一个字节流
    byteIO = io.BytesIO()
    # 把图片放在字节流里面去
    image.save(byteIO, "png")
    return HttpResponse(byteIO.getvalue(), "image/png")

# 随机颜色的生成
def createcolor():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)

import os
from django.conf import settings
#上传文件
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

from django.core.paginator import Paginator
#分页显示
def studentpage(request,pageid):
    #所有学生的列表
    allList = Students.stuObj2.all()
    paginator = Paginator(allList,3)
    page = paginator.page(pageid)
    return render(request,'myApp1/studentpage.html',{"students":page})

def ajaxstudents(request):
    return render(request,'myApp1/ajaxstudents.html')
from django.http import JsonResponse
def studentsinfo(request):
    stus = Students.stuObj2.all()
    list = []
    for stu in stus:
        list.append([stu.sname,stu.sage])
    return JsonResponse({"data":list})

def edit(request):
    return render(request,'myApp1/edit.html')

import time
def celery(request):
    print("sunwenbo is a good man ")
    time.sleep(5)
    print("sunwenbo is a nice man ")
    return render(request,'myApp1/celery.html')