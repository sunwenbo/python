#__author:  Administrator
#date:  2020/3/8
import win32com,win32com.client,os

def makeWordFile(path):
    word = win32com.client.Dispatch("Word.Application")
    #让文档可见
    word.Visible = True
    #创建word文档
    doc = word.Documents.Add()
    #写内容，从头开始写
    r = doc.Range(0,0)
    r.InsertAfter("亲爱的" + name +"\n")
    r.InsertAfter("        插入文字\n")
    #存储文件
    doc.SaveAs(path)
    #关闭文件
    doc.Close()
    #退出word
    word.Quit()

names = ["张三","李四","王五"]
for name in names:
    path = os.path.join(os.getcwd(),name)
    makeWordFile(path)