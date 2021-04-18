#__author:  Administrator
#date:  2020/3/1
import sys
import importlib
importlib.reload(sys)
from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfpage import PDFTextExtractionNotAllowed

def readPDF(path,toPath):
    #以二进制形式打开pdf文件
    f = open(path,"rb")
    #创建一个PDF分析器
    parser = PDFParser(f)

    #创建一个PDF文件
    pdfFile = PDFDocument()

    #链接分析器与文档对象
    parser.set_document(pdfFile)
    pdfFile.set_parser(parser)
    #提供pdf初始化密码
    pdfFile.initialize()

    #检测文档是否提供txt转换
    if not pdfFile.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        #解析数据
        #数据管理器
        manager = PDFResourceManager()
        #创建一个PDF设备对象
        laparams = LAParams
        device = PDFPageAggregator(manager,laparams=laparams)
        #解释器对象
        interpreter = PDFPageInterpreter(manager,device)

        #开始循环处理，每次处理一页
        for page in pdfFile.get_pages():
            interpreter.process_page(page)
            #开始处理图层
            layout = device.get_result()
            for x in layout:
                if (isinstance(x,LTTextBoxHorizontal)):
                    with open(toPath,"a") as f:
                        str = x.get_text()
                        print(str)
                        f.write(str+"\n")





path = r"E:\python笔记\自动化办公\2.读取PDF文件\Linux云计算第一阶段学员必背.pdf"
toPath = r"E:\python笔记\自动化办公\2.读取PDF文件\a.txt"
readPDF(path,toPath)
