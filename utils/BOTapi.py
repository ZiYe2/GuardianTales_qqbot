#!/usr/bin/env python
# coding: utf-8
import requests
from io import BytesIO
from config import qq_account

rootURL = "http://127.0.0.1:6666/"
session = ""
qq = qq_account
timeout=20

def get(api: str):
    global res
    res = requests.get(rootURL + api, timeout=timeout)
    return checkCode(res)

def post(api: str,json=None, files=None, data=None):
    global res
    res = requests.post(rootURL + api, json=json, files=files, data=data, timeout=timeout)
    return checkCode(res)

def checkCode(res):
    try:
        if 0 == res.json()["code"]:
            return res
        if 500 == res.json()["code"]:
            if "Not a http session" ==  res.json()["msg"]:
                print("verify!!!")
                verify()
        print(res.json())
    except Exception:
        pass

def verify(key=""):
    global session
    res = post("verify", {
        "verifyKey":key
    })
    if res:
        session = res.json()['session']
verify()

def bind(session=session, qq=qq):
    post("bind",{
        "sessionKey": session,
            "qq": qq
    })

def release(session=session, qq=qq):
    post("release",{
        "sessionKey": session,
        "qq": qq
    })

def countMessage(session=session):
    res = get("countMessage?sessionKey=" + session)
    if res:
        return res.json()['data']
    else:
        verify()
        return -1

def getMessage(session=session):
    res = get("fetchMessage?sessionKey=" + session + "&count=10")
    if res:
        return res.json()['data']
    else:
        return [{'type': 'error'}]

def sendMessage(target, kind, msgChain, session=session):
    messageChain = []
    if not kind == "Friend" and not kind == "Group":
        raise Exception()
    for msg in msgChain:
        if msg[0] == "text":
            messageChain += [{"type": "Plain", "text": msg[1]}]
        elif msg[0] == "image" or msg[0] == "img":
            img_url = uploadImage(kind, msg[1])
            messageChain += [{"type": "Image", "url": img_url}]
        elif msg[0] == "@":
            messageChain += [{"type": "At", "target": msg[1]}]
        else:
            raise Exception()

    post('send'+kind+"Message",json={
        "sessionkey": session,
        "target": target,
        "messageChain": messageChain
    })


def uploadImage(kind, path, session=session):
    if kind == "Group" or kind == "Friend":
        img = BytesIO(open(path, 'rb').read())
        try:
            url = requests.post(rootURL+"uploadImage", timeout=timeout,
                   data={"sessionKey": session, "type": kind},
                   files={"img": img}).json()["url"]
            print("upload image: "+path+" "+url)
            return url
        except Exception as e:
            print(f'发送图片失败: {path}  {e}')
    else:
        raise Exception

def sendNudge(target, subject=None, kind="Friend", session=session):
    if subject:
        kind = "Group"
    else:
        subject = target
    post("sendNudge",json={
        "sessionKey": session,
        "target": target,
        "subject": subject,
        "kind": kind
    })

def getMemberList(target, session=session):
    try:
        member_list = get(f"/memberList?sessionKey={session}&target={target}").json()
        if member_list['code'] != 0:
            raise Exception(f"状态码不为0：{member_list}")
        return member_list['data']
    except Exception as e:
        print(f"获取群友列表失败:{target}  {e}")
        return []

if __name__ == "__main__":
    for i in range(10):
        print(i)
        