#__author:  Administrator
#date:  2020/2/16
import tkinter
win = tkinter.Tk()
win.title("欢迎来到Tk系统")
#win.geometry("300x200+200+50")
'''
文本控件，用于显示多行文件
滚动条控件
'''
#创建滚动条
scroll = tkinter.Scrollbar()
text = tkinter.Text(win,width=40,height=10)
#height 显示的行数   width 显示的宽度
#text.pack()
#side将滚动条放到窗口的右侧,  fill填充，Y轴填充满
scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
text.pack(side=tkinter.LEFT,fill=tkinter.Y)
#关联
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)
str = '''新冠肺炎疫情牵动着14亿中国人的心。我们原本熟悉的生活仿佛被按下“暂停键”，
但与生命有关的一切正在“加速奔跑”。对国家而言，这场战“疫”是一场大考。在这场大考中，
我们看到了举国上下齐心协力，更感受到了我们伟大民族、伟大政党、伟大人民迸发出的磅礴力量。
2月15日，在德国慕尼黑，世界卫生组织总干事谭德塞在第56届慕尼黑安全会议上讲话。 新华社记者 逯阳 摄

新华社慕尼黑2月15日电（记者任珂 朱晟）世界卫生组织总干事谭德塞15日在德国慕尼黑表示，中国采取的从源头上控制新冠肺炎疫情的措施令人鼓舞，尽管这些措施让中国付出了很大代价，但为世界争取了时间，减缓了病毒向世界其他地方传播的速度。

14日开幕的第56届慕尼黑安全会议（慕安会）正值新冠肺炎疫情暴发，谭德塞专程前来参会，会议主办方还组织了一场有关此次疫情的边会。
'''
text.insert(tkinter.INSERT,str)
win.mainloop()