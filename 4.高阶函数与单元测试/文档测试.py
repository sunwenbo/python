#__author:  Administrator
#date:  2020/3/14
import doctest
#doctst 模块可以提取注释中的代码执行
#doctest严格按照python交互模式输入提取

def mySum(x,y):
    '''
    get The Sum from x and Y
    :param x: firstNum
    :param y: SeconNum
    :return: sum

    example:
    >>> print(mySum(1,2))  #注意print前面有空格
    3
    '''
    return x + y

print(mySum(1,2))

#进行文档测试
doctest.testmod()