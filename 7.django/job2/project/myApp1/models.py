from django.db import models

# Create your models here.

class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.gname
    class Meta:
        db_table = "grades"
class StudentsManager(models.Manager):
    def get_queryset(self):
        return super(StudentsManager,self).get_queryset().filter(isDelete=False)

    def createStudents(self,name,age,gender,contend,grade,last,create,delete=False):
        stu = self.model()
        stu.sname = name
        stu.sage = age
        stu.sgender = gender
        stu.contend = contend
        stu.sgrade = grade
        stu.lastTime = last
        stu.createTime = create
        return stu


class Students(models.Model):
    #自定义模型管理器
    #当自定义模型管理器，objects就不存在了
    stuObj2 = StudentsManager()  #使用自定义的模型类创建模型管理器
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField(db_column="age")
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    #关联外键
    sgrade = models.ForeignKey("Grades",on_delete=models.CASCADE)
    def __str__(self):
        return self.sname
    lastTime = models.TimeField(auto_now=True)
    createTime = models.TimeField(auto_now_add=True)
    class Meta:
        db_table = "students"
    def getName(self):
        return self.sname

    #定义一个类方法创建对象
    @classmethod
    def createStudents(cls,name,age,gender,contend,grade,last,create,delete=False):
        stu = cls(sname=name,sage=age,sgender=gender,scontend=contend,sgrade=grade,lastTime=last,createTime=create,isDelete=delete)
        return stu

from tinymce.models import HTMLField

class GoodsInfo(models.Model):
    gcontent = HTMLField()