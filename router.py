from message.friendMessage import friendMessage
from message.groupMessage import groupMessage
from message.nudgeEvent import nudgeEvent
from config import qq_account

def router(msg):
    msgtype = msg['type']
    # print(msg)
    if msgtype == "FriendMessage":
        #friendMessage(msg["sender"],
         #             msg["messageChain"])
        pass

    elif msgtype == "GroupMessage":
        groupMessage(msg["sender"],
                     msg["messageChain"])

    elif msgtype == "NudgeEvent":
        if str(msg['target']) == qq_account:
            nudgeEvent(msg["fromId"],
                       msg['target'],
                       msg["subject"])
