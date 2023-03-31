from utils.BOTapi import *
from router import router
import time

while True:
    time.sleep(5)
    try:
        cm = countMessage()
    except:
        print("获取消息失败")
        time.sleep(30)
        continue
    # print(cm)

    if cm == -1:
        print("count message error")
    elif cm > 0:
        msgs = getMessage()
        for msg in msgs:
            # print(msg)
            if msg['type'] == "error":
                print("get message error")
            else:
                router(msg)


