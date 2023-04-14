#__author:  Administrator
#date:  2020/3/14

import unittest
from 对函数进行单元测试 import mySum
from 对函数进行单元测试 import mySub
from testperson import Person

#测试函数命名必须加test

class Test(unittest.TestCase):
    def setUp(self):
        print("开始测试时自动调用")
    def tearDown(self):
        print("结束测试时自动调用")
    #为了测试mySum
    def test_mySum(self):
        self.assertEqual(mySum(1,2),3,"加法有误")
    def test_mySub(self):
        self.assertEqual(mySub(2,1),1, "减法有误")

    def test_init(self):
        p = Person("hanmeimei",20)
        self.assertEqual(p.name,"hanmeimei","属性赋值有误")

    def test_getAge(self):
        p = Person("hanmeimei",20)
        self.assertEqual(p.getAge(), p.age, "getAge函数有误")



if __name__ == "__main__":
    unittest.main()