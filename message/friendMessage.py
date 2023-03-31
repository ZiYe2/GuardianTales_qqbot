from utils.BOTapi import *
from utils.sendSticker import sendSticker
from utils.guild_report import *

def friendMessage(sender, messageChain):
    senderID = str(sender['id'])
    # print(senderID + str(messageChain))

    text = ""
    img_list = []
    for msg in messageChain:
        # print(msg)ls
        
        if msg["type"] == "Plain":
            text += msg["text"]
        if msg['type'] == "Image":
            img_list.append(msg['url'])

    if not text == "":
        if sendSticker(senderID, "Friend", text):
            print("send Friend sticker "+senderID+" :\n"+str(text))
        elif guild_report(senderID, "Friend", text):
            print("send Friend guild_report "+senderID+" :\n"+str(text))
        else:
            print(f"friend.{senderID}: {text}")

    elif not img_list == []:
        print("imagem message: ",senderID)
    else:
        print("what the fuck: ", senderID, messageChain)


