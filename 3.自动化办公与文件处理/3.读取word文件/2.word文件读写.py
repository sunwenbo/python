#__author:  Administrator
#date:  2020/3/8
import win32com
import win32com.client

def readWordFiletoOtherFile(path,topath):
    mw = win32com.client.Dispatch("Word.application")
    doc = mw.Documents.Open(path)
    #将word文件的内容保存到另一个文件
    doc.SaveAs(topath,2)  #2代表text文件
    doc.Close()
    mw.Quit()


path = r'E:\python笔记\3.自动化办公\3.读取word文件\2.docx'
topath = r'E:\python笔记\3.自动化办公\3.读取word文件\a.txt'
readWordFiletoOtherFile(path,topath)