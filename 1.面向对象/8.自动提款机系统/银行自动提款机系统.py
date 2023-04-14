#__author:  Administrator
#date:  2020/2/8
'''
卡
类名：Card
属性：卡号  密码  余额

提款机
类名：ATM
属性：用户字典
行为：开户 查询 取款 存款 转账 改密码 锁盯 解锁 补卡 销户

管理员
类名：admin
属性：
行为：管理员界面   系统功能界面  管理员登录  管理员验证

'''
from admin import Admin
from atm import ATM
import pickle
import os
import time
def main():
    #管理员对象
    admin = Admin()
    #管理员开机
    admin.printAdminView()
    if admin.adminOption():
        return -1
    #获取数据文件的绝对路径
    filepath = os.path.join(os.getcwd(), "allusers.txt")
    #打开该文件，读取文件内容
    f = open(filepath,"rb")
    # #将文件的内容赋值给allUser
    allUser = pickle.load(f)
    #取款机对象
    #allUser = {}
    atm = ATM(allUser)

    while True:
        admin.printsysFunctionView()
        #等待用户的操作
        option = str(input("请输入您的操作："))
        if option == "1":
            atm.createUser()
        elif option == "2":
            atm.searchUserInfo()
        elif option == "3":
            atm.getMoney()
        elif option == "4":
            atm.saveMoney()
        elif option == "5":
            atm.transferMoney()
        elif option == "6":
            atm.changPasswd()
        elif option == "7":
            atm.lockUser()
        elif option == "8":
            atm.unlockUser()
        elif option == "9":
            atm.newCard()
        elif option == "10":
            atm.killUser()
        elif option == "q":
            if  not admin.adminOption():
                #0为false   非0 为true
                #如果返回值为-1 ，not -1 代表为假,不执行下面的代码，继续执行while循环，如果返回值为0 ，not 0 代表不为假为真，继续执行下面的代码。
                #将当前系统中的用户信息保存到文件里面
                f = open(filepath,"wb")
                pickle.dump(atm.allUsers,f)
                f.close()
                return -1
        time.sleep(2)


if __name__ == "__main__":
    main()