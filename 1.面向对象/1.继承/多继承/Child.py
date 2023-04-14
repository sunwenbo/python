#__author:  Administrator
#date:  2019/12/22
from Father import Father
from Mother import Mother

class Child(Mother,Father):
    def __init__(self,money,faceValue,name,age):
        Father.__init__(self,money)
        Mother.__init__(self,faceValue)
        #自定义的属性
        self.name = name
        self.age = age