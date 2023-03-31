
import ctypes
import os
import time
import traceback
from utils.BOTapi import sendMessage
from threading import Thread
from config import administrator

last_error = ''
permission_list = [administrator,]
_groupID = ''

th_cmd = None
last_cmd = ''
th_py = None
last_py = ''

def run_command(groupID, senderID, kind, text):
    global _groupID
    _groupID = groupID
    global _kind
    kind = 'Group' if kind is None else kind
    _kind = kind
    global last_error
    if str(senderID) not in permission_list:
        return False
    if text.__len__() == 0:
        return False
    
    if text[0] == '/':
        global th_py
        global last_py
        if text.__len__() == 1:
            send_py()
            return True
        else:
            def py(text):
                global last_py
                reply = ''
                T1 = time.time()
                try:
                    loc = locals()
                    exec(text[1:])
                    reply = loc['reply']
                except:
                    reply = traceback.format_exc()
                if reply == '':
                    T2 = time.time()
                    reply = f'finish {round((T2-T1)*1000, 2)}ms'
                last_py = str(reply)
                send_py()
        if th_py is not None:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(th_py.ident), ctypes.py_object(SystemExit))
        th_py = Thread(target=py, args=(text,))
        th_py.start()
        return True
            
                
    elif text[0] == '!' or text[0] == '！':
        global th_cmd
        global last_cmd
        if text.__len__() == 1:
            send_cmd()
            return True
        
        def cmd(text):
            T1 = time.time()
            global last_cmd
            reply = os.popen(text[1:]).read()
            if reply == '':
                T2 = time.time()
                reply = f'finish {round((T2-T1)*1000, 2)}ms'
            last_cmd = reply
            send_cmd()
        if th_cmd is not None:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(th_cmd.ident), ctypes.py_object(SystemExit))
        th_cmd = Thread(target=cmd, args=(text,))
        th_cmd.start()
        return True
    return False

def send_py():
    global last_py
    global _groupID
    global _kind
    reply = last_py[:500]
    last_py = last_py[500:]
    if last_py != '':
        reply += '-'
    if reply != '':
        sendMessage(_groupID, _kind, [["text", reply]])
    # print(reply)

def send_cmd():
    global last_cmd
    global _groupID
    global _kind
    reply = last_cmd[:500]
    last_cmd = last_cmd[500:]
    if last_cmd != '':
        reply += '-'
    if reply != '':
        sendMessage(_groupID, _kind, [["text", reply]])
    # print(reply)

if __name__ == '__main__':
    pass


