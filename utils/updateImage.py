import os.path
import requests
import re
import shutil

# bigfun停止服务，已弃用！！！bigfun停止服务，已弃用！！！
# bigfun停止服务，已弃用！！！bigfun停止服务，已弃用！！！
# bigfun停止服务，已弃用！！！bigfun停止服务，已弃用！！！
# bigfun停止服务，已弃用！！！bigfun停止服务，已弃用！！！
# bigfun停止服务，已弃用！！！bigfun停止服务，已弃用！！！

update = False

def eye():
    global update
    img_path = "./image/千里眼/"
    if update:
        return
        
    # res = requests.get("https://www.bigfun.cn/post/1084598")
    res = ''
    temp = re.findall(r'<p class="ql-align-center">(.+?)></p>', res.text)
    img_urls = re.findall(r'data-src="(.+?)"', str(temp))

    length = len(img_urls)
    if length == 0:
        print("千里眼更新失败")
    else:
        shutil.rmtree(img_path)
        if not os.path.exists(img_path):
            os.mkdir(img_path)
        for i in range(length):
            res = requests.get(img_urls[i])
            with open(img_path+str(i)+".png","wb") as f:
                f.write(res.content)

    update = True


