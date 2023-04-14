'''
设计类
类名：见名之意，首字母大写，其他遵循驼峰原则
属性：见名之意，其他遵循驼峰原则
行为（方法/功能）：见名之意，其他遵循驼峰原则

创建类
类：一种数据类型，本身并不占内存空间，根所学过的number，string，Boolean等类似。

'''

class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 23
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' '+ self.model
        return long_name.title()
    def read_odmoter(self):
        print("this car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self,mileage):
        self.odometer_reading = mileage

my_new_car = Car('audi','a4', 2016)

print(my_new_car.get_descriptive_name())
my_new_car.read_odmoter()
my_new_car.update_odometer(44)
my_new_car.read_odmoter()

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        a = self.restaurant_name + self.cuisine_type
        return a
    def open_restaurant(self):
        print("正在营业")
restaurant = Restaurant('sunwenbo',' love')
print(restaurant.describe_restaurant())
print(restaurant.open_restaurant())
restaurant = Restaurant(123,456)
print(restaurant.describe_restaurant())
