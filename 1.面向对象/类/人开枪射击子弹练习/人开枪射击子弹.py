#__author:  Administrator
#date:  2019/12/8
'''
人
类名：Person
属性：gun
行为：fire
枪
类名：Gun
属性：bulletBox
行为：shoot
弹夹
类名：bulletBox
属性：bulletCount
行为：
'''

from person import Person
from gun import Gun
from bulletbox import BulletBox
#弹夹
bulletBox = BulletBox(3)
#枪
gun = Gun(bulletBox)
#人
per = Person(gun)

per.fire()
per.fire()
per.fire()
per.fire()
per.fillBullet(2)
per.fire()
per.fire()
per.fire()
