from utils.sendSticker import sendSticker
from utils.BOTapi import *
from utils.guild_report import *
from utils.command import *
from config import qq_account,enable_groups

myself = qq_account

def groupMessage(sender, messageChain):
    senderID = str(sender["id"])
    groupID = str(sender["group"]["id"])
    at = False
    text = ""

    if groupID in enable_groups:
        for msg in messageChain:
            # print(msg)
            if msg["type"] == "Plain":
                text += msg["text"]
            elif msg["type"] == "At" and str(msg["target"]) == myself:
                at = True

        if at:
             sendMessage(groupID, "Group",
                         [["@",senderID],["text",text]])
             print(f"send group At {groupID}@{senderID}:\n{text}")

        elif text != "":
            print(f"{groupID}.{senderID}: {text}")
            if run_command(groupID, senderID, "Group", text):
                print(f"run group command {groupID}.{senderID}: {text}")
            elif guild_report(groupID, senderID, "Group", text):
                print("send group guild_report "+groupID+" :"+str(text))
            elif sendSticker(groupID, "Group", text):
                print("send group sticker "+groupID+" :"+str(text))
            else:
                # print(f"{groupID}.{senderID}: {text}")
                pass

        else:
            # print("what the fuck: ", messageChain)
            pass

