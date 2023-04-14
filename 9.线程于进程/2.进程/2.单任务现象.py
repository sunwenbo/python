from time import  sleep

def run():
    while True:
        print("sunwenbo is a nice man")
        sleep(1.2)


if __name__ == "__main__":
    while True:
        print("sunwenbo is a good man")
        sleep(1)

    #不会执行到run方法，只有上面等while循环结束才可以执行
    run()