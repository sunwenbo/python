from django.contrib import admin

# Register your models here.
from .models import Grades,Students

class StudentsInfo(admin.TabularInline):#StackedInline
    model = Students
    extra = 2

@admin.register(Grades)
class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo]
    # #列表页属性
    list_display = ['pk','gname','ggirlnum','bboynum','isDelete']
    list_filter = ['gname']
    list_per_page = 5
    search_fields = ['gname']
    # #添加，修改页属性
    #fields = ['ggirlnum','bboynum','isDelete','gname']
    fieldsets = [("num",{"fields":['ggirlnum','bboynum']}),
                 ("base",{"fields":['gname','gdate','isDelete']}),]
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        #设置返回值
        if self.sgender:
            return "男"
        else:
            return "女"
    #设置页面的名称
    gender.short_description = "性别"
    def age(self):
        return  self.sage
    age.short_description = "年龄"
    def pk(self):
        return self.pk
    pk.short_description = "序号"
    def name(self):
        return self.sname
    name.short_description = "姓名"
    def contend(self):
        return self.scontend
    contend.short_description = "备注"

    list_display = [pk,name,gender,age,contend,'isDelete']
    list_filter = ['sname']
    list_per_page = 2
    search_fields = ['sname']
    fieldsets = [("base",{"fields":['sname','gender','sage','isDelete']}),
                 ("num",{"fields":['scontend']})]

    #执行动作的位置
    actions_on_top = False
    actions_on_bottom = True
#注册
#admin.site.register(Grades,GradesAdmin)
#admin.site.register(Students,StudentsAdmin)
