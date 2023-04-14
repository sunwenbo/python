#__author:  Administrator
#date:  2020/3/15
import re
'''
给你一串字符串，判断是否是手机号码

'''
def checkPhone(str):
    if len(str) != 11:
        return False
    elif str[0] != "1":
        return False
    elif str[1:3] != "39" and str[1:3] != "31":
        #print(str[1:3])
        return False
    for i in range(3,11):
        if str[i] < "0" or str[i] > "9":
            return False
    return True

#print(checkPhone("13912345678"))


def checkPhone2(str):
    pat = r"^1[345678]\d{9}"
    res = re.match(pat,str)
    return res

print(checkPhone2("13123456789"))
print(checkPhone2("13423456789"))

re_QQ = re.compile(r"^[1-9]\d{5,9}$")
print(re_QQ.match("1212311111"))