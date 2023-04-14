#__author:  Administrator
#date:  2019/12/22
'''
多态：一种事物的多种形态
最终目标：人可以喂任何一种动物
'''
from cat import Cat
from mouse import Mouse
from person import Person
from animal import Animal


tom = Cat("tom")
jerry = Mouse("jerry")

tom.eat()
jerry.eat()
#思考：在添加100种动物，也都有name属性和eat方法
#定义了一个有name属性和eat方法的Animal类，让所有的动物都继承自Animal
#定义一个人类，可以喂猫和老鼠吃东西
per = Person()
#per.feedCat(tom)
#思考: 人要喂100种动物，难道要写100种方法？
per.feedAnimal(tom)
abc = Animal("aaa")
per.feedAnimal(abc)

