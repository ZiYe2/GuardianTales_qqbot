# 坎公骑冠剑 qq机器人 
## 基于mirai-http-api<br>写着玩的，不再维护！
<br>

### 主要功能：
#### 查前线（故障），公会伤害报表，出刀数，查刀，催刀，兑换码（故障），发图片，发短文，抽卡

## 效果图
|       |       |       |
| :---: | :---: | :---: |
|![公会伤害](./readme/%E5%85%AC%E4%BC%9A%E4%BC%A4%E5%AE%B3.png)| ![出刀数](./readme/%E5%87%BA%E5%88%80%E6%95%B0.png)|![查刀](./readme/%E6%9F%A5%E5%88%80.jpg)|
|![图片](./readme/%E5%9B%BE%E7%89%87.jpg)|![催刀](./readme/%E5%82%AC%E5%88%80.jpg)|![抽卡](./readme/%E6%8A%BD%E5%8D%A1.jpg)|
|![兑换码](./readme/%E5%85%91%E6%8D%A2%E7%A0%81.jpg)|![短文](./readme/%E7%9F%AD%E6%96%87.jpg)|![前线](./readme/%E5%89%8D%E7%BA%BF.jpg)|


## 运行：
### 在以下环境中通过测试：
- Windows 10/Windows 11 | Ubuntu 16/20
- python 3.8/3.9 
<span style="font-size:66%;">（运行本项目）</span>
- java 11/16
<span style="font-size:66%;">（运行mirai）</span>

### requirement
- pandas
- pillow
- matplotlib

### mirai
#### 有任何步骤失败请前往mirai论坛查找解决方法 -> 
#### 下载[Mirai Console Loader（mcl）](https://github.com/iTXTech/mirai-console-loader)并安装[mirai-api-http](https://github.com/project-mirai/mirai-api-http)插件
```bash
./mcl --update-package net.mamoe:mirai-api-http --channel stable-v2 --type plugin
```
#### 切换到mcl目录运行，命令一般为java -jar mcl.jar
使用 autoLogin 账号 密码 添加账号
在以下该路径创建文件并填写下面的配置
你的MiraiConsoleLoader\config\net.mamoe.mirai-api-http\setting.yml
重启mcl
```yaml
adapters:
  - http
  - ws
enableVerify: false
debug: false
singleMode: true
cacheSize: 4096
adapterSettings:
  http:
    host: localhost
    port: 6666
    cors: ["*"]
    unreadQueueMaxSize: 100
  ws:
    host: localhost
    port: 6667
    reservedSyncId: -1
```

### 本项目   
<blockquote>
下载本项目并切换到项目目录<br>
修改config.py文件 <del>（内有注释）</del><br>
运行命令
</blockquote>

```bash
python main.py
```
<blockquote>
在qq中发送消息检查是否成功
</blockquote>
