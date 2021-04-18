#__author:  Administrator
#date:  2020/3/8

import win32com
import win32com.client
def makePPT(path):
    ppt = win32com.client.Dispatch("PowerPoint.Application")
    ppt.Visible = True

    #新增文件
    pptFile = ppt.presentations.Add()

    #创建页
    page1 = pptFile.Slides.Add(1,1)#参数1代表页数从1开始  参数2为类型
    t1 = page1.Shapes[0].TextFrame.TextRange
    t1.Text = "sunwenbo"
    t2 = page1.Shapes[1].TextFrame.TextRange
    t2.Text = "sunwenbo is a good man"
    page2 = pptFile.Slides.Add(2,1)
    t3 = page2.Shapes[0].TextFrame.TextRange
    t3.Text = "hello"
    t4 = page2.Shapes[1].TextFrame.TextRange
    t4.Text = "hello word"
    page3 = pptFile.Slides.Add(3, 2)
    t5 = page3.Shapes[0].TextFrame.TextRange
    t5.Text = "hello"
    t6 = page3.Shapes[1].TextFrame.TextRange
    t6.Text = "hello word"

    #保存
    pptFile.SaveAs(path)
    pptFile.Close()
    ppt.Quit()

path = r'E:\python笔记\3.自动化办公\5.PPT文件\sunwenbo.ppt'

makePPT(path)