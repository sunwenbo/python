#__author:  Administrator
#date:  2019/12/22
from Child import Child
def main():
   c = Child(300,100,"sunwenbo",24)
   print(c.money,c.faceValue,c.name,c.age)
   c.play()
   c.eat("apple")
   c.func()
   #注意：父类中方法相同，默认调用的是子类在括号中排前面中的方法

if __name__ == "__main__":
    main()
