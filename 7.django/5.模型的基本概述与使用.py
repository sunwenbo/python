#__author:  Administrator
#date:  2020/3/31
'''
概述：Django 对各种数据库提供了很好的支持，Django为这些数据库提供了统一调用的API，我们可以根据不同的需求使用不同的数据库。

配置数据库: __init__.py 文件中修改
            import pymysql
            pymysql.install_as_MySQLdb()
修改settings.py文件，配置数据源
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'NAME': "data1",
                    'USER': "root",
                    'PASSWORD': "1qaz2wsx",
                    'HOST': "localhost",
                    'PORT': "3306",
                }
            }
开发流程：
    1）配置数据库
    2）定义模型类  一个模型类都在数据库中对应一张数据表
    3）生成迁移文件
    4）执行迁移生成数据表
    5）使用模型类进行 增删改查

ORM： O 对象  R 关系  M 映射
   任务1：根据对象的类型生成表结构
   任务2：将对象、列表的操作转换为sql语句
   任务3：将sql语句查询到的结果转换为对象、列表
   优点：极大的减轻了开发人员的工作量，不需要面对因数据库的变更而修改代码。

定义模型：模型、属性、表、字段间的关系  一个模型类在数据库对应一张表，在模型中定义的属性，对应该模型对照表中的字段。
定义属性：详情请见，定义属性.txt
创建模型类：
元选项：在模型中定一个Meta类，用于设置元信息
            db_table = 定义数据表名称，推荐使用小写字母，如果不写数据表名默认为项目名小写_类名小写
            ordering = 对象的默认排序字段，获取对象的列表时使用  ordering = ['id']  升序  ordering = ['-id'] 降序
            注意：排序会增加数据库的开销

模型成员：
    类属性：objects  是manager类型的一个对象，作用是与数据库进行交互,当定义模型类时没有指定管理器，则Django为模型创建一个名为objects的管理器
    自定义管理器：
            stuObj = models.Manager()   注意：当我们使用自定义模型管理器，默认的objects就不存在了
    自定义管理器Manager类：
            模型管理器是Django与数据库进行交互的接口，一个模型类，可以有多个模型管理器
            作用：向管理器类中添加额外的方法，修改管理器返回的原始查询集合   重写get_queryset()方法
                       class StudentsManager(models.Manager):
                            def get_queryset(self):
                                return super(StudentsManager,self).get_queryset().filter(isDelete=False)

                        class Students(models.Model):
                            #自定义模型管理器
                            #当自定义模型管理器，objects就不存在了
                            stuObj = models.Manager()
                            stuObj2 = StudentsManager()  #使用自定义的模型类创建模型管理器
    创建对象：
        目的：向数据库中添加数据，当创建对象时，Django不会对数据库进行读写操作，当调用save时才与数据库进行交互，将对象保存到数据库表中。
        注意：__init__方法已经在父类models.Mode中使用，在自定义模型中无法使用
        方法：
            一，在模型类中加一个类方法
                #定义一个类方法创建对象

                @classmethod
                def createStudents(cls,name,age,gender,contend,grade,last,create,delete=False):
                    stu = cls(sname=name,sage=age,sgender=gender,scontend=contend,sgrade=grade,lastTime=last,createTime=create,isDelete=delete)
                    return stu
            二，在定义管理器中添加一个方法
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

    模型查询
        概述：查询集表示数据库获取的对象集合
        查询集可以有多个过滤器（过滤器就是一个函数，基于所给的参数限制查询结果）
        从sql角度来说，查询集合select语句等价，过滤器就像where条件
        查询集：
            可以在管理器上调用过滤方法返回查询集
            查询集经过过滤器筛选后返回新的查询集，所以可以写成链式调用
            惰性执行，创建查询集不会带来任何数据的访问，直到调用数据时，才会访问数据。
            直接访问数据的情况   1.迭代   2.序列化  3.与if合用

            返回查询集的方法称为过滤器：
                1.all()   返回查询集中所有的数据
                2.filter()  返回符合条件的数据
                    1.filter(键=值)
                    1.filter(键=值，键=值)
                    2.filter(键=值).filter(键=值)
                3.exclude() 过滤掉符合条件的数据
                4.order_by()    排序
                5.values()  一条数据就是一个字典，返回一个列表.

            返回单个数据：
                1.get()     返回一个满足条件的对象
                    注意：如果没有找到符合条件的对象，会引发"模型类.DoseNotExit"异常.
                          如果找到多个对象，会引发"模型类.MultipleObjectsReturned"异常.
                2.count()   返回查询集中的对象个数
                3.first()   返回查询集中的第一个对象
                4.last()    返回查询集中的最后一个对象
                5.exists()  返回查询集中是否有数据，如果有数据返回True，否则返回False

            限制查询集：
                1.查询集返回列表，可以使用下标的方法进行限制，等于sql中limit语句
                    注意：下标不能为负数

            查询集的缓存：
                概述：每个查询集都包含一个缓存，来最小化的对数据库访问
                在新建的查询集中，缓存首次为空。第一次对查询集求值，会发生数据缓存。django会将查询集的数据做一个缓存，并返回查询结构，以后的查询直接使用查询集的缓存

            字段查询：
                概述：实现了sql中的where语句，作为方法filter()，exclude() ，get()的参数
                语法：属性名称__比较运算符=值
                外键：属性名_id
                转义：类似sql中的like语句

                1.比较运算符
                    1）exact     判断，大小写敏感    filter(isDelete=False)
                    2）contains      是否包含，大小写敏感
                    3）startswith endswith       以value开头或结尾，大小写敏感
                    注意：以上四个在前面加上i，就表示不区分大小写iexact,icontains,istartswith,iendswith

                    4）isnull,isnotnull      是否为空  filter(sname__isnull=False)
                    5) in       是否包含在范围内    filter(pk__in=[2,4,6,8])
                    6) gt(大于)  gte(大于等于) lt(小于) lte(小于等于)
                    7) year(年)  month(月) week_day(周)  hour(小时)  minute(分钟)  second(秒)
                    8) 跨关联查询 模型类名__属性名__比较运算符
                        #描述中包含孙文波的三个字的数据属于哪个班级的
                        studentsList = Grades.objects.filter(students__scontend__contains="孙文波")
                        return render(request,'myApp1/grades.html',{"grades":studentsList})

                    9) 查询快捷  pk  代表主键primary key
                2.聚合函数
                    使用aggregate()函数，返回聚合函数的值
                    avg   count   max  min  sum
                    注意需要引入：from django.db.models import Max
                3.F对象
                    可以使用模型的A属性与B属性进行比较, 支持F对象的算术运算
                    from django.db.models import F,Q
                    def grades(request):
                        g = Grades.objects.filter(ggirlnum__gt=F('gboynum'))
                        print(g)
                        return HttpResponse("abc")


                4.Q对象
                    概述：过滤器的方法中的关键字参数，条件为and模式
                    需求：进行or查询
                    解决：使用Q对象
                            studentsList = Students.stuObj2.filter(Q(pk__lte=4) | Q(sage__gte=50))
                    注意：只有一个Q的情况，就是匹配


'''

