from utils.BOTapi import *
from config import *

group_list = enable_groups
myself = qq_account

def nudgeEvent(fromId, target, subject):
    fromId = str(fromId)
    target = str(target)
    if fromId == myself:
        return

    if subject["kind"] == "Friend":
        if target == myself:
            print("nudge "+fromId+" -> "+target)
            sendNudge(fromId)

    elif subject["kind"] == "Group":
        for group_id in group_list:
            if str(subject["id"]) == group_id:
                if target == myself:
                    sendNudge(fromId, group_id)
                else:
                    sendNudge(target, group_id)
                print("nudge "+fromId+" -> "+target+" "+group_id)

