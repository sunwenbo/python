import os,time
from multiprocessing import Pool
def copyFile(rPath,wPath):
    fr = open(rPath,"rb")
    fw = open(wPath,'wb')
    context = fr.read()
    fw.write(context)
    fr.close()
    fw.close()

srcpath = r"/Users/admin/Documents/python/9.线程于进程/2.进程/file"
topath = r"/Users/admin/Documents/python/9.线程于进程/2.进程/tofile"

if __name__ == "__main__":
    # 读取path下的所有文件
    filesList = os.listdir(srcpath)
    print(filesList)
    start = time.time()
    pp = Pool(5)
    for filesName in filesList:
        pp.apply_async(copyFile,args=(os.path.join(srcpath,filesName),os.path.join(topath,filesName)))
    pp.close()
    pp.join()
    end = time.time()
    print("总耗时： %0.2f" % (end - start))
