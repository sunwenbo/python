#__author:  Administrator
#date:  2019/12/8
class Gun(object):
    def __init__(self,bulletBox):
        self.bulletBox = bulletBox
    def shoot(self):
        if self.bulletBox.bulletCount == 0:
            print("没有子弹了")
        else:
            self.bulletBox.bulletCount -= 1
            print("剩余子弹： %d发" % self.bulletBox.bulletCount)


