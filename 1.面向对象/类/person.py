#__author:  Administrator
#date:  2019/12/8
class Person(object):
    def __init__(self,gun):
        self.gun = gun
    def fire(self):
        self.gun.shoot()
    def fillBullet(self,count):
        self.gun.bulletBox.bulletCount = count
