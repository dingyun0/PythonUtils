import time
import winsound

def remind():
    #毫秒和频率
    duration=1000
    freq=440
    winsound.Beep(freq,duration)

while True:
    time.sleep(3)
    print("休息时间到啦，起来动一动吧！")
    remind()
    print("提醒时间：",time.ctime())
