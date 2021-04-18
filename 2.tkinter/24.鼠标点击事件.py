#__author:  Administrator
#date:  2020/2/23
'''
鼠标事件
<ButtonPress-n>     <Button-n>      <n>                         鼠标按钮n被按下，n为1左键，2中键，3右键
<ButtonRelease-n>                                               鼠标按钮n被松开
<Double-Button-n>                                               鼠标按钮n被双击
<ButtonRelease-n>                                              鼠标释放事件
<Triple-Button-n>                                               鼠标按钮n被三击
<Motion>                                                        鼠标被按下，同时，鼠标发生移动
<Bn-Motion>                                                     鼠标按钮n被按下，同时，鼠标发生移动
<Enter>                                                         鼠标进入
<Leave>                                                         鼠标离开
<MouseWheel>                                                    鼠标滚轮滚动

键盘事件
<Any-KeyPress>      <KeyPress>      <Key>                       任意键按下
<KeyRelease>                  ButtonReleased                                  任意键松开
<KeyPress-key>      <Key-key>       <key>                       特定键按下
<KeyRelease-key>                                                特定键松开
<Control-Shift-Alt-KeyPress-key>    <Control-Shift-Alt-key>     组合键按下（Alt，Shift，Control任选一到三个）
'''
import tkinter
win = tkinter.Tk()
win.title("欢迎来到Tk系统")
win.geometry("300x300+200+50")

def func(event):
    #x，y的坐标为鼠标点击控件的位置的坐标
    print(event.x,event.y)
#鼠标左键
button1 = tkinter.Button(win,text="leftmouse button")
#bind 给控件绑定事件，
button1.bind("<Double-Button-1>",func)  #1 为左键，2为滑轮，3为右键
button1.pack()


win.mainloop()