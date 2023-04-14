#__author:  Administrator
#date:  2019/12/8
class Person(object):
    def __init__(self, name, age, height, weight,money):
        #print(name, age, height, weight)
        self.name = name
        self.__age__ = age
        self._height = height
        self.weight = weight
        self.__money = money

    def run(self):
        print(self.__money)
    def eat(self, food: object):
        print("eat " + food)
    #def __del__(self):
        print("这里是析构函数")
    def __str__(self):
        return "%s-%d-%d-%d" % (self.name,self.age,self.height,self.weight)
    #通过自定义的方法实现对私有的属性的赋值与取值
    def setMoney(self,money):
        #数据的过滤
        if money < 0:
            money = 0
        self.__money = money
    def getMoney(self):
        return self.__money
per = Person("sunwenbo",24,177,60,10000)
per.age = 10
print(per.age)
#如果要让内部的属性不被外部直接访问,在属性前加两个下划线（__）
#在python中如果在属性前加两个下划线，那么这个属性就变成了private（私有）的
#per.money = 0
#print(per.money)
#print(per.__money)    #外部无法使用私有变量
#per.run()              #调用类内部的方法
per.setMoney(100)
print(per.getMoney())
#不能直接访问per.__money是因为Python解释器把__money变成了_Preson__money，
#仍然可以用_Person__money去访问，但是不建议去这么调用，不同版本的解释器可能存在解释的变量名不一致
per._Person__money = 1
print(per.getMoney())
#在python中，__XXX__ 属于特殊变量，可以直接访问
print(per.__age__)
#在python中 _XXX_ 变量，这样的实例变量在外部也是可以直接访问的。
#但是按照约定的规则，当我们看到这样的变量时，代表虽然可以访问，
#但是不要直接访问。约等于私有变量，不要在外部直接访问
print(per._height)
