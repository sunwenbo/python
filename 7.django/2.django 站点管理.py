#__author:  Administrator
#date:  2020/3/29

'''
Admin站点管理
概述：
    内容发布：负责添加、修改、删除内容
    公告访问：
配置Admin应用：在settings.py 中INSTALLED_APPS 添加 'django.contrib.admin' 默认是添加好的
创建管理员用户：python manage.py createsuperuser  输入用户名、邮箱和密码
汉化：修改settings.py文件 LANGUAGE_CODE = 'zh-Hans'  TIME_ZONE = 'Asia/Shanghai'
管理数据表：修改admin.py 文件
            from .models import Grades,Students
            #注册
            admin.site.register(Grades)
            admin.site.register(Students)
            自定义管理页面：
                列表页属性：
                list_display 显示字段
                list_filter  过滤字段或表
                list_per_page 分页显示
                search_fields 搜索字段
                修改、添加页属性：
                fields      属性先后顺序
                fieldsets   给属性分组, fields和fieldsets 不能同时使用

                from .models import Grades,Students

                class GradesAdmin(admin.ModelAdmin):
                    # #列表页属性
                    list_display = ['pk','gname','ggirlnum','bboynum','isDelete']
                    list_filter = ['gname']
                    list_per_page = 5
                    search_fields = ['gname']
                    # #添加，修改页属性
                    #fields = ['ggirlnum','bboynum','isDelete','gname']
                    fieldsets = [("num",{"fields":['ggirlnum','bboynum']}),
                                 ("base",{"fields":['gname','gdate','isDelete']}),]
    关联对象：
        需求：(创建班级时，可以创建两个学生)
        class StudentsInfo(admin.TabularInline):#StackedInline
        model = Students
        extra = 2
        class GradesAdmin(admin.ModelAdmin):
        inlines = [StudentsInfo]   #添加

    布尔值显示问题：
        添加函数，并将函数传入 list_display中
        def gender(self):
            if self.sgender:
                return "男"
            else:
                return "女"
        list_display = [pk,name,gender,age,contend,'isDelete']

    执行动作位置：
        actions_on_top = False
        actions_on_bottom = True

    使用装饰器完成注册：
            装饰器@   写在要装饰的类上面
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

'''