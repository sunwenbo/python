#__author:  Administrator
#date:  2019/12/8
'''
设计类
类名：见名之意，首字母大写，其他遵循驼峰原则
属性：见名之意，其他遵循驼峰原则
行为（方法/功能）：见名之意，其他遵循驼峰原则

创建类
类：一种数据类型，本身并不占内存空间，根所学过的number，string，Boolean等类似。
用类创建实例化对象（变量），对象占内存空间

格式：
class 类名（父类列表）:
    属性
    行为
'''
# object：基类，超类，所有类的父类
#一般没有合适的父类就写object
class Person(object):
    #定义属性
    name = ""
    age = 0
    height = 0
    weight = 0
    #定义方法(定义函数)
    #注意：方法的参数必须以self当第一个参数
    #self代表类的实例（某个对象）
    def run(self):
        print("run")
    def eat(self, food: object) -> object:
        print("eat " + food)
    def openDoor(self):
        print("我已经打开了冰箱门")
    def fillEle(self):
        print("我已经把大象装进冰箱了")
    def clossDoor(self):
        print("我已经关闭了冰箱门")
"""
实例化一个对象
格式：对象名=类名（参数列表）
注意：没有参数，小括号也不能省略
"""
per1 = Person()
print(per1)
print(type(per1))
per2 = Person()
print(per2)
print(type(per2))
# 变量在栈区，对象在堆区
print(id(per1))
print(id(per2))
#访问对象的属性与方法
'''
访问属性
格式：对象名.属性名
赋值：对象名.属性名 = 新值
'''
per1.name = "tom"
per1.age = "18"
per1.height = "170"
per1.weight = "80"
print(per1.name,per1.name,per1.height,per1.weight)
'''
访问方法
格式，对象名.方法名(参数列表)
'''
per1.openDoor()
per1.fillEle()
per1.clossDoor()
per1.eat("苹果")
#问题：目前来看Person创建的所有对象属性都是一样的
#对象的初始状态，构造函数
'''
构造函数： __init__(): 在使用类创建对象的时候自动调用 
注意：如果不显示的写出构造函数，默认回自动添加一个空的构造函数
'''
per1 = Person("sunwenbo",24,177,80)
print(per1)






