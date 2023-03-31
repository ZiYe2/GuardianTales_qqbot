import os
import random
from utils.BOTapi import sendMessage,uploadImage

imgpath = "./image/"


def sendSticker(groupID, kind, text):
    imgpaths = []
    if text in ["涩", "色", "瑟", "涩涩", "色色", "瑟瑟", "色图", "瑟图", "涩图"]:
        temp_path = imgpath + "不可以涩涩/"
        imgpaths = [temp_path + random.choice(os.listdir(temp_path))]
    elif text in ["不可以涩涩", "不可以色色", "不可以瑟瑟"]:
        temp_path = imgpath + "涩涩/"
        imgpaths = [temp_path + random.choice(os.listdir(temp_path))]
    elif text[:1] == "寄":
        temp_path = imgpath + "寄/"
        imgpaths = [temp_path + random.choice(os.listdir(temp_path))]
    elif text == '千里眼':
        imgpaths = [f'{imgpath}千里眼/{img}' for img in os.listdir("./image/千里眼")]
    elif text == '周边':
        imgpaths = [imgpath + "周边.png"]
    else:
        return False

    msgChain = [["image", p] for p in imgpaths]
    sendMessage(groupID, kind, msgChain)
    return True


if __name__ == '__main__':
    pass

