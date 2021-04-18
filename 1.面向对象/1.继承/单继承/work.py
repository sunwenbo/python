#__author:  Administrator
#date:  2019/12/22
from person import  Person
class Work(Person):
    def __init__(self,name,age,money,like):
        super(Work, self).__init__(name,age,money)
        self.like = like


