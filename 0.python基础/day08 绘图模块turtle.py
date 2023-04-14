"""
是一个简单的绘图工具
提供一个小海龟，可以把它理解为一个机器人，只能听得懂有限的命令
绘图窗口的原点(0,0)在正中间，默认海龟的方向是右侧。

运动命令
forward(d)    向前移动d长度
backward(d)   向后移动d长度
right(d)      向右转动多少度
left(d)      向左转动多少度
goto(d)      移动到坐标为(x，y)位置
speed(speed)  笔画回执的速度[0,10] 越大越快

笔画控制命令
up()        笔画抬起，在移动的时候不会绘图
down()      笔画落下，在移动的时候会继续绘图
setheading(50)  改变海龟的朝向
pensize(d)      笔画的宽度
pencolor("颜色")   笔画的颜色
reset()       清空窗口，重置turtle状态
clear()       清空窗口，但不会重置turtle窗口
circle(r,e)   绘制一个圆形，r为半径，e为次数可以不写

begin_fill()    开始填充
fillcolor("colorstr")
end_fill()      结束填充
其他命令
done()          程序继续执行
undo()          撤销上一次命令
hideturtle()    隐藏海龟
showturtle()    显示海龟
screensize(x,y)  屏幕
"""
import turtle

turtle.speed(1)
turtle.forward(100)
turtle.right(45)
turtle.forward(100)
turtle.goto(-100,-100)
turtle.up()
turtle.goto(100,100)
turtle.left(30)
turtle.down()
turtle.pencolor("red")
turtle.forward(80)
turtle.goto(0,0)
turtle.setheading(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
#turtle.clear()
turtle.begin_fill()
turtle.fillcolor("blue")
turtle.pencolor("green")
turtle.circle(50,steps=4)

turtle.right(90)
turtle.forward(100)
turtle.circle(60,steps=6)
turtle.end_fill()

turtle.done()


import turtle

bob = turtle.Turtle()

print(bob)