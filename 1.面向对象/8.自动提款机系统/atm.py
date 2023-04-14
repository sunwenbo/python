#__author:  Administrator
#date:  2020/2/8
from card import Card
from user import User
import random

class ATM(object):
    def __init__(self,allUser):
        self.allUsers = allUser
    #开户
    def createUser(self):
    #目标：向用户字典中添加一对键值对（卡号-用户）
        name = input("请输入您的姓名：")
        idcard = input("请输入您的身份证号码：")
        phone = input("请输入您的电话号码：")
        prestoreMoney = int(input("请输入预存款金额："))
        if prestoreMoney <= 0:
            print("预存款输入有误！！开户失败……")
            return -1
        onePasswd = input("请设置密码：")
        #验证密码
        if not self.checkPassword(onePasswd):
            print("密码输入错误！！开户失败……")
            return -1
        #所有需要的信息全了
        cardStr = self.randomCardid()
        #创建卡对象
        card = Card(cardStr,onePasswd,prestoreMoney)
        #创建用户对象
        user = User(name,idcard,phone,card)
        #存到字典
        self.allUsers[cardStr] = user
        print("开户成功！！请牢记卡号(%s)……" % (cardStr))

    #查询
    def searchUserInfo(self):
        cardNum = input("请输入您的卡号:")
        #验证该卡号是否存在
        user =self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！查询失败……")
            return -1
        #判断是否锁定
        if user.card.cardLock:
            print("该卡已被锁定！！请解锁后再进行其他操作……")
            return -1
        #验证密码
        if not self.checkPassword(user.card.cardPasswd):
            print("密码输入错误！！查询失败……")
            user.card.cardLock = True
            return -1
        print("账号：%s   余额：%d" % (user.card.cardId,user.card.cardMoney))
    #取款
    def getMoney(self):
        cardNum = input("请输入您的卡号:")
        #验证该卡号是否存在
        user =self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！取款失败……")
            return -1
        #判断是否锁定
        if user.card.cardLock:
            print("该卡已被锁定！！请解锁后再进行其他操作……")
            return -1
        #验证密码
        if not self.checkPassword(user.card.cardPasswd):
            print("密码输入错误！！取款失败……")
            user.card.cardLock = True
            return -1
        tempIdCard = input("请输入您的身份证号码：")
        if tempIdCard != user.idCard:
            print("身份证输入错误！！取款失败……")
            return -1
        moneyGet = int(input("请输入您要取款的金额："))
        if user.card.cardMoney < moneyGet:
            print("卡内余额不足!! 卡内余额为%d" % (user.card.cardMoney))
        elif moneyGet <= 0:
            print("请输入大于0的金额……")
        else:
            #取款
            user.card.cardMoney -= moneyGet
            print("卡内余额为%d元 ……" % (user.card.cardMoney))
    #存款
    def saveMoney(self):
        cardNum = input("请输入您的卡号:")
        #验证该卡号是否存在
        user =self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！存款失败……")
            return -1
        #判断是否锁定
        if user.card.cardLock:
            print("该卡已被锁定！！请解锁后再进行其他操作……")
            return -1
        #验证密码
        if not self.checkPassword(user.card.cardPasswd):
            print("密码输入错误！！存款失败……")
            user.card.cardLock = True
            return -1
        tempIdCard = input("请输入您的身份证号码：")
        if tempIdCard != user.idCard:
            print("身份证输入错误！！存款失败……")
            return -1
        moneyGet = int(input("请输入您要存款的金额："))
        if moneyGet <= 0:
            print("您存入的金额不能小于或等于0")
        else:
            user.card.cardMoney += moneyGet
            print("存款后卡内余额为%d元 ……" % (user.card.cardMoney))
    #转账
    def transferMoney(self):
        cardNum = input("请输入您的卡号:")
        # 验证该卡号是否存在
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！转账失败……")
            return -1
        # 判断是否锁定
        if user.card.cardLock:
            print("该卡已被锁定！！请解锁后再进行其他操作……")
            return -1
        #输入要转账的卡号
        cardNum2 = input("请输入要转账的卡号：")
        user2 = self.allUsers.get(cardNum2)
        if not user2:
            print("被转账的卡号不存在！！转账失败……")
            return -1
        # 判断是否锁定
        if user2.card.cardLock:
            print("被转账的卡已被锁定！！请解锁后再进行其他操作……")
            return -1
        # 验证密码
        if not self.checkPassword(user2.card.cardPasswd):
            print("密码输入错误！！转账失败……")
            user.card.cardLock = True
            return -1
        tempIdCard = input("请输入您的身份证号码：")
        if tempIdCard != user.idCard:
            print("身份证输入错误！！转账失败……")
            return -1
        transMoney = int(input("请输入您要转账的金额："))
        if transMoney <= 0:
            print("您转账的金额不能小于或等于0……")
        elif transMoney >= user.card.cardMoney:
            print("您的转账数额已超过实际余额……转账失败！！卡内余额为%d元 ……" % (user.card.cardMoney))
        else:
            #开始转账
            user.card.cardMoney -= transMoney
            user2.card.cardMoney += transMoney
            print("转账后卡内余额为%d元 ……" % (user.card.cardMoney))
    #改密
    def changPasswd(self):
        cardNum = input("请输入您的卡号:")
        # 验证该卡号是否存在
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！")
            return -1
        # 判断是否锁定
        if user.card.cardLock:
            print("该卡已被锁定！！请解锁后再进行其他操作……")
            return -1
        # 验证密码
        if not self.checkPassword(user.card.cardPasswd):
            print("密码输入错误！！")
            user.card.cardLock = True
            return -1
        tempIdCard = input("请输入您的身份证号码：")
        if tempIdCard != user.idCard:
            print("身份证输入错误！！")
            return -1
        newPasswd = input("请输入新的密码：")
        user.card.cardPasswd = newPasswd
        print("密码已修改成功，此次修改后的密码为%s" % (user.card.cardPasswd))
    #锁定
    def lockUser(self):
        cardNum = input("请输入您的卡号:")
        # 验证该卡号是否存在
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！锁定失败……")
            return -1
        if user.card.cardLock:
            print("该卡已被锁定！！请解锁后再使用其他功能……")
            return -1
        if not self.checkPassword(user.card.cardPasswd):
            print("密码输入错误！！锁定失败……")
            return -1
        tempIdCard = input("请输入您的身份证号码：")
        if tempIdCard != user.idCard:
            print("身份证输入错误！！锁定失败……")
            return -1
        #锁定
        user.card.cardLock = True
        print("锁定成功……")
    #解锁
    def unlockUser(self):
        cardNum = input("请输入您的卡号:")
        # 验证该卡号是否存在
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！解锁失败……")
            return -1
        if not user.card.cardLock:
            print("此卡没有被锁定，无需解锁……")
            return -1
        if not self.checkPassword(user.card.cardPasswd):
            print("密码输入错误！！解锁失败……")
            return -1
        tempIdCard = input("请输入您的身份证号码：")
        if tempIdCard != user.idCard:
            print("身份证输入错误！！解锁失败……")
            return -1
        # 解锁
        user.card.cardLock = False
        print("解锁成功……")
    #补卡
    def newCard(self):
        cardNum = input("请输入您之前的卡号:")
        # 验证该卡号是否存在
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！补卡失败……")
            return -1
        if not self.checkPassword(user.card.cardPasswd):
            print("您输入账户的密码错误！！补卡失败……")
            return -1
        tempIdCard = input("请输入您的身份证号码：")
        if tempIdCard != user.idCard:
            print("身份证输入错误！！补卡失败……")
            return -1
        #开始补卡
        NewCard = self.randomCardid()
        self.allUsers[NewCard] = self.allUsers.pop(cardNum)
        print(self.allUsers)
        print("补卡成功，您的新卡号为：%s" % (NewCard))

    #销户
    def killUser(self):
        cardNum = input("请输入您的卡号:")
        # 验证该卡号是否存在
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！注销用户失败……")
            return -1
        if not self.checkPassword(user.card.cardPasswd):
            print("密码输入错误！！注销用户失败……")
            return -1
        tempIdCard = input("请输入您的身份证号码：")
        if tempIdCard != user.idCard:
            print("身份证输入错误！！注销用户失败……")
            return -1
        # 开始注销用户
        self.allUsers.pop(cardNum)
        print(self.allUsers)
        print("注销卡账号为%s成功……" %(cardNum))

    #验证密码
    def checkPassword(self, realPasswd):
        for i in range(3):
            tempPasswd = input("请再次输入密码：")
            if tempPasswd == realPasswd:
                return True
        return False

    #生成卡号
    def randomCardid(self):
        while True:
            str = ""
            for i in range(6):
                ch = chr(random.randrange(ord('0'), ord('9') + 1))
                str += ch
            #判断是否重复
            if not self.allUsers.get(str):
                return str






