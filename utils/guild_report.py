import datetime
import os.path
import random
import re
import time
import traceback
# import dataframe_image as dfi
from PIL import Image, ImageFont, ImageDraw
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager 
import numpy as np
import pandas as pd
import requests
timeout = 20
if not __name__ == '__main__':
    from config import *
    from utils.illness import get_illness
    from utils.draw_card import draw_card
    from utils.BOTapi import uploadImage, sendMessage, getMemberList

prop = font_manager.FontProperties(fname='./ZhanKuKuaiLeTi2016XiuDingBan-2.ttf')
font_manager.fontManager.addfont('./ZhanKuKuaiLeTi2016XiuDingBan-2.ttf')
plt.rcParams['font.family'] = [prop.get_name()]  # 显示中文字体

role_translate = {"alpaca_girl": "土羊", "dancing_archer": "土弓", "kamael": "土神", "innuit": "可可", "demon_ceo": "莉莉丝",
                  "invader_knight": "暗刀", "sheep_girl": "火羊", "lifeguard_yuze": "水柚子", "future_knight": "大骑",
                  "steam_princess": "阿伊莎", "store_angel": "光弓", "mecha_android": "MK99", "eight_tail": "奈莉",
                  "lady_thief": "火牌", "eleanor": "光琴", "villain_redhood": "暗炮", "witch_coco": "暗狼", "flower_girl": "土花",
                  "half_vampire": "光萝", "redhood": "小红帽", "priestess": "水教", "lina": "莉娜", "mercenary": "虎鲸",
                  "garam":"水狐","vampire_lord":"岳父","future_princess":"公主","robot_tanker":"暗盾","china_chef":"火刀",
                  "plitvice":"布丁","fire_harpy":"火腿","hana":"哈娜","saintess":"克拉拉","knight_female":"女骑","knight_male":"男骑",
                  "summer_loraine":"老板娘"}
boss_convert = {"暗影魔王":"黑屎","boss_harvester_guild_fury":"归蚊","机械人艾瑞娜":"奶奶","雪人将军盖斯特":"雪人", "boss_nine_tailed_fox_guild":"水狐",
                "改良疯狂熊猫MK-三型":"火箭队","熔岩史莱姆国王":"史莱姆","春秋派首领":"老头","海军舰长玛丽娜":"船长","boss_minister_guild":"邓肯",
                "哥布林族长":"哥布林", 'boss_invader_director_guild': '导演'}
urge_white_list = []
urge_designated_dict = urge_designated_dict
headers = {"Cookie": bigfun_cookie}
date_list = []
member_dict = {}
date_log_time = 0
report = {}
report_log_time = 0
t_report = {}
draw_card_log_path = './limit/draw_card_log.csv'
draw_card_limit = 2
say_hello_path = './limit/say_hello.txt'
illness_log_path = './limit/illness_log.csv'
illness_limit = 3
administrator = administrator

__today__ = open(say_hello_path).read() if os.path.exists(say_hello_path) else ''

def guild_report(group_id, senderID, kind, text):
    try:
        return guild_report2(group_id, senderID, kind, text)
    except Exception as e:
        print("失败",kind, group_id,text,'  ',e)
        traceback.print_exc()
        sendMessage(group_id, kind, [["text","失败"]])
        return True
def guild_report2(group_id, senderID, kind, text):
    msg = None
    if text == "菜单" or text == "menu":
        msg = [["text", "[公会]\n前线(进度)|查刀(cd)|出刀数(cds)|兑换码|公会伤害|作业|催🔪|提醒\n[娱乐]\n寄|抽卡|涩涩|不可以涩涩|发癫"]]
    
    elif '寄器人' in text or '寄寄人' in text:
        msg = [['@', senderID],["text", '恭喜你成为勇士战神候选人！通过试炼成为勇士战神，拯救世界吧！']]
    
    elif text == "cds" or text == "出刀数":
        path = cds()
        if os.path.exists(path):
            msg = [["image", path]]
        else:
            msg = [["text", "失败"]]

    elif text == "cd" or text == "查刀" or text == "cd " or text == "查刀 ":
        msg = [["text", "正确用法：\ncd 玩家名称"]]
    elif text[:3] == "cd " or text[:3] == "查刀 ":
        path = cd(name=text[3:])
        if path is None:
            msg = [["text", "找不到该玩家"]]
        else:
            msg = [["image", path]]

    elif text == "redeemcode" or text == "兑换码" or text == "兑换":
        code = redeemcode()
        if code is None or code == "":
            code = "失败"
        msg = [["text", code]]

    elif text in ["front","前线","前线报道","进度"]:
        t = front()
        if t is None or t == "":
            t = "失败"
        msg = [["text", t]]

    elif text == "公会伤害" or text == "工会伤害":
        path = guild_damage()
        if path is None:
            msg = [["text", "公会伤害查询失败"]]
        else:
            msg = [['image', path]]

    elif text == "作业":
        msg = [["text","https://dx35.ww2.ren/#f/tool_work/t/list/"]]

    elif text == "催刀" or text == "催🔪" or text == "🔪":
        msg = urge_blade(group_id, senderID)
    
    elif text == '抽卡':
        msg = [['text', "角色单抽|角色单抽up\n角色单抽维罗妮卡\n角色十连|角色百连\n武器单抽|武器单抽up\n角色单抽塞弥亚\n武器十连|武器百连\n(一二三)星角色列表\n(一二三四五)星武器列表"]]
    elif text[:4] in ['角色单抽','角色十连','角色百连','武器单抽','武器十连','武器百连']\
            or text[2:] in ["角色列表",'武器列表']:
        msg = [['@',senderID],["text", guild_draw_card(group_id, senderID, text)]]

    elif text[:3] in ['发电 ','发点 ','发癫 ','发病 ']:
        if len(text) > 3:
            illness = guild_illness(group_id, senderID, text[3:])
            msg = [['text', illness]]

    elif text == '提醒':
        msg = [["image",'./image/催神.png'],
               ['text','催催催催催催催催\n我是催神维罗妮卡\n\n签到了吗？\n33打了吗？\n日常做了吗？\n体力清了吗？\n共斗打了吗？\n陨石敲了吗？\n死斗打了吗？\n公会战打了吗？\n农场树砍了吗？\n卡玛逊打了吗？']]

    else:
        return False
    if msg is None:
        msg = [["text","逻辑错误"]]
    
    # 每日打招呼
    global __today__
    today = datetime.date.today().strftime('%Y-%m-%d')
    if __today__ != today and os.path.exists(say_hello_path) and today != open(say_hello_path).read():
        __today__ = today
        open(say_hello_path, 'w').write(today)
        sendMessage(group_id, kind, [["text","您好，您看上去挺面善的～最近您会因为诸事不宜而感到沮丧吗？别担心！和我们一起追随​勇士战​​神吧！这样定能一帆风顺！​"]])  
    
    sendMessage(group_id, kind, msg)
    return True

def update_date_member():
    global date_list
    global member_dict
    global date_log_time
    if time.time() - date_log_time > 600:
        try:
            res = requests.get("https://www.bigfun.cn/api/feweb?target=kan-gong-guild-log-filter%2Fa", headers=headers, timeout=timeout)
            date_list = res.json()['data']['date']
            if type(date_list) != type([]):
                raise Exception("获取日期失败")
            date_list.sort()
            member_list = res.json()['data']['member']
            member_dict = {mem['name']: mem['id'] for mem in member_list}
            date_log_time = time.time()
        except Exception as e:
            print(f"获取日期失败{e}")
update_date = update_member = update_date_member
def update_t_report():
    update_date()
    global t_report
    for date in date_list:
        if t_report.get(date) and time.time() - t_report.get(date).get("time") < 3600:
            if date == date_list[-1]:
                if time.time() - t_report.get(date).get("time") < 600:
                    continue
            else:
                continue
        try:
            res = requests.get("https://www.bigfun.cn/api/feweb?target=kan-gong-guild-report%2Fa&date=" + date, timeout=timeout,
                               headers=headers)
            t_report[date] = {"time": time.time(), "data": res.json()["data"]}
            time.sleep(random.randint(1, 2))
        except Exception:
            print(f"更新{date}数据失败")
def update_report():
    global report_log_time
    global report
    update_date()
    for date in date_list:
        try:
            if report.get(date) is not None and time.time() - report.get(date)[0]['server_time'] < 600:
                continue
            res = requests.get(
                f"https://www.bigfun.cn/api/feweb?target=kan-gong-guild-log%2Fa&date={date}&user_id=&page=1&size=200",
                headers=headers, timeout=timeout)
            time.sleep(random.randint(1, 2))
            t = []
            for data in res.json()['data']:
                knife = {}
                knife['server_time'] = time.time()
                knife['log_time'] = data['log_time']
                knife['user_name'] = data['user_name']
                knife['boss'] = data['boss']['elemental_type_cn'] + '·' + data['boss']['name']
                knife['damage'] = data['damage']
                role = re.findall("/portraits/(.+?).png", data['role_list'][0]['icon'])[0]
                if role in role_translate.keys():
                    role = role_translate[role]
                knife['role'] = role
                t.append(knife)
            report[date] = t
        except:
            print(f"{date}更新失败")
def update_all():
    update_report()
    update_t_report()

def switch_color(boss_name):
    e = boss_name[0]
    if e == "火": return "red"
    if e == "水": return "deepskyblue"
    if e == "土": return "orange"
    if e == "虚": return "lightsteelblue"
    if e == "光": return "yellow"
    if e == "暗": return "darkviolet"
    return "hotpink"
def boss_convert1(boss_name):
    if boss_name[2:] in boss_convert.keys():
        boss_name = boss_name[:2] + boss_convert[boss_name[2:]]
    return boss_name
def boss_convert2(boss_name):
    if boss_name in boss_convert.keys():
        boss_name = boss_convert[boss_name]
    return boss_name

def guild_damage(path="./image/guild/guild_damage.png"):
    update_report()
    boss_set = set()
    for date in report.values():
        for k in date: # k == knife
            boss_set.add(k['boss'])
    df = pd.DataFrame(0,index=member_dict.keys(),columns=list(boss_set))
    for date in report.values():
        for k in date:  # k == knife
            if not k['user_name'] in df.index:
                df.loc[k['user_name']] = 0
            df[k['boss']][k['user_name']] += k['damage']
    boss_list = [boss_convert1(boss) for boss in boss_set]
    df.columns = boss_list
    df['sum'] = df.sum(axis=1)
    df.sort_values(by="sum",inplace=True)

    plt.figure(figsize=(9,16), dpi=120, facecolor="white")
    ax = plt.axes(facecolor="white")
    ax.spines['left'].set_color('black')
    left = df.iloc[:,0] - df.iloc[:,0]
    for boss_name in df.columns[:-1]:
        p = plt.barh(df.loc[:,boss_name].index, df.loc[:,boss_name], color=switch_color(boss_name),
                     edgecolor="black", linewidth=0.5, left=left, label=boss_name)
        plt.bar_label(p, color="black", label_type="center", labels=(df.loc[:,boss_name]/10000).astype('int'))
        plt.yticks(color="black",)
        plt.xticks([])
        plt.title("公会伤害: {}           ".format(df['sum'].sum()), color="black")
        left += df.loc[:,boss_name]
    plt.box(False)
    plt.axvline(0, color='black', linewidth=2)
    df['sum'] = (df['sum']/10000).astype('int').astype('str')+"万"
    plt.bar_label(p, color="black", labels=df['sum'])
    plt.legend()
    plt.savefig(path, bbox_inches='tight', facecolor="white")
    return path

def cds(path="./image/guild/cds.png"):
    """出刀数"""
    update_all()
    form = {}
    for d in range(len(date_list)):
        day = f"第{d+1}天"
        form[day] = {}

        user_boss = {}
        for user in t_report[date_list[d]]['data']:
            boss_list = [ [damage_list['boss_name'], damage_list['is_kill']] for damage_list in user['damage_list'] ]
            user_boss[user['user_name']] = boss_list

        count1 = {}
        for knife in report[date_list[d]]:
            name = knife['user_name']
            l = count1.get(name)
            if l:
                count1[name] += [[knife['role'], knife['boss']]]
            else:
                count1[name] = [[knife['role'], knife['boss']]]

        for user in count1.keys():
            knife2 = []
            c = 0
            if user not in user_boss.keys():
                continue
            for i in range(count1[user].__len__()-1,-1,-1):
                role = count1[user][i][0]
                boss_count = (np.array(count1[user])[:i+1,0] == role).sum()
                if role in knife2 or boss_count == 2:
                    knife2.append(role)
                    boss_name = count1[user][i][1][2:]
                    try:
                        user_boss[user].remove([boss_name, 1])
                    except:
                        user_boss[user].remove([boss_name, 0])
                    count1[user].pop(i)
                    c += 0.5

            for u_b in user_boss[user]:
                if u_b[1] == 1:
                    c+=0.5
                elif u_b[1] == 0:
                    c+=1
                else:
                    raise Exception()
            form[day][user] = c

    df = pd.DataFrame(form)
    df = df.fillna(0)
    df.loc['出刀数'] = df.sum(axis=0)
    df['出刀数'] = df.sum(axis=1)
    df = df.astype(object)
    for day in df.columns:
        for name in df.index:
            df[day][name] = "%g" % (df[day][name])

    # draw table
    font = ImageFont.truetype('fangzhengshaoer_GBK.ttf', size=30)
    scale = 1.6
    cell_height = int(font.getbbox(df.index[0])[3]*scale)
    margin = int(cell_height *(scale - 1)/2 -scale)
    name_width_list = [int(font.getbbox(name)[2]) for name in df.index]
    name_width = max(name_width_list)
    col_width = int(max([font.getbbox(title)[2] for title in df.columns]))
    
    image = Image.new('RGB', (col_width*len(df.columns)+name_width,cell_height*len(df.index)+cell_height+margin), color='#ffffff')
    draw = ImageDraw.Draw(image)
    for i, name in enumerate(df.index):
        draw.text((name_width - font.getbbox(name)[2], cell_height * (i+1)+margin), name, fill='#000000', font=font)
    for i, title in enumerate(df.columns):
        draw.text((col_width*i+name_width+(col_width-font.getbbox(title)[2])/2, 0+margin), title, fill='#000000', font=font)

    for y, columns in enumerate(df.values):
        for x, content in enumerate(columns):
            c = float(content)
            content = str(content)
            if c <= 0: fill = 'red'
            elif c < 3: fill = 'orange'
            elif c == 3: fill = 'lightgreen'
            else: fill = None
            x_, y_ = col_width*x+name_width, cell_height*(y+1)
            draw.rectangle((x_,y_,x_+col_width,y_+cell_height), fill=fill)
            x_ += (col_width - font.getbbox(content)[2])/2
            draw.text(( x_, y_+margin), content, fill='#000', font=font)
    image.save(path)

    # 傻逼chrome整天失败
    return path

def cd(name, path="./image/guild/cd.png"):
    """查刀"""
    update_member()
    res = None
    for k in member_dict.keys():
        if name in k:
            name = k
            res = requests.get(
                f"https://www.bigfun.cn/api/feweb?target=kan-gong-guild-log%2Fa&date=&user_id={member_dict[k]}&size=100", timeout=timeout,
                headers=headers)
    if res is None:
        return

    # 初次清洗
    damage_list = []
    for knife in res.json()['data']:
        t = time.localtime(knife['log_time'])
        day = f"{t.tm_mon}.{t.tm_mday}"
        role = re.findall(r'portraits/(.+?).png', knife['role_list'][0]['icon'])[0]
        if role in role_translate.keys():
            role = role_translate[role]
        boss = knife['boss']['elemental_type_cn'] + "·" + knife['boss']['name']
        damage = knife['damage']
        damage_list.append([day, boss, role, damage])

    # 找尾刀
    temp_day = ""
    temp_roles = []
    for i in range(len(damage_list) - 1, -1, -1):
        role = damage_list[i][2]
        date = damage_list[i][0]
        if temp_day != date:
            temp_day = date
            temp_roles = []
        if role in temp_roles:
            damage_list[i][2] = role + "尾"
        else:
            temp_roles.append(role)
    damage_list = np.array(damage_list)

    # 建表
    # fuck pandas
    day = []
    for d in damage_list[::-1, 0]:
        if not d in day:
            day.append(d)
    boss_list = list(set(damage_list[:, 1]))
    index = pd.MultiIndex.from_arrays(
        [damage_list[:, 0], damage_list[:, 2]],
        names=["date", "role"]
    )
    df = pd.DataFrame(index=index, columns=boss_list, dtype=int)
    for dam in damage_list:
        df.loc[dam[0], dam[2]][dam[1]] = int(dam[3])
    df = df.fillna(0)
    df.columns = [boss_convert1(boss) for boss in df.columns]
    df1 = df.groupby('date').agg('sum')
    df1 = pd.DataFrame(df1, index=day)

    transform_damage = lambda d: f"{int(d / 10000)}w" if d > 10000 else f'{int(d)}'

    # 获取伤害标签
    def get_damage_label():
        p_label = [[]] * (len(df.columns) + 1)
        for boss in df.columns:
            day = ""
            i = list(df.columns).index(boss)
            p_label[i] = []
            label = ""
            for index in df.index[::-1]:
                damage = df[boss][index]
                if day == "":
                    day = index[0]
                elif day != index[0]:
                    day = index[0]
                    p_label[i] += [label]
                    label = ""
                if damage != 0.0:
                    if label != "":
                        label += "\n"
                    label += index[1] + "\n" + transform_damage(damage)
            p_label[i] += [label]
        p_label[len(df.columns)] = list(df1.sum(axis=1).apply(transform_damage))  # 第5列
        return p_label

    width = 0.85
    p_label = get_damage_label()
    plt.figure(figsize=(13, 5), dpi=200, facecolor="white")
    plt.xticks(range(day.__len__()), day, color="black")
    plt.yticks([])

    # 条形图
    count_boss = len(df.columns)
    if count_boss < 1:
        return
    height_count = df1.iloc[:, 0] - df1.iloc[:, 0]
    for i in range(count_boss):
        boss_damage = df1.columns[i] + " " + list(df1.sum().apply(transform_damage))[i]  # 右上角boss伤害，难以维护
        p = plt.bar(day, df1.iloc[:, i], width, edgecolor="black", linewidth=0.5, color=switch_color(boss_damage),
                    label=boss_damage, bottom=height_count)
        plt.bar_label(p, color="black", label_type="center", labels=p_label[i])
        height_count = height_count + df1.iloc[:, i]
    plt.bar_label(p, color="black", labels=p_label[count_boss])

    plt.axhline(0, color='black', linewidth=2)
    plt.legend(loc="upper right", labelcolor="white", facecolor="#202020")
    plt.box(False)
    plt.title(f'伤害表[{name}]\n总伤害[{format(int(df1.sum().sum()), ",")}]', color="black")
    # plt.show()
    plt.savefig(path, bbox_inches='tight', facecolor="white")
    return path

def redeemcode() -> str:
    res = requests.get(
        r"https://wiki.biligame.com/gt/%E6%B8%B8%E6%88%8F%E7%A4%BC%E5%8C%85%E7%A0%81%E5%85%91%E6%8D%A2%E9%A1%BB%E7%9F%A5",timeout=timeout)
    tbody = re.findall(r"<tbody>[\s\S]+</tbody>", res.text)[0]
    tr_list = re.findall(r"<tr>([\s\S]+?)</tr>", tbody)[1:]

    td_list = []
    for tr in tr_list:
        td_list.append(re.findall(r"<td>([\s\S]+?)</td>", tr))
    td_list = np.array(td_list)
    len = td_list[:, 0].size

    code_list = []
    for i in range(len):
        code_list.append(
            str(re.findall(r'<pre class="copyBtn">(.+?)</pre>', td_list[i, 0]))[2:-2]
                .replace("', '", "\n")
        )

    meaning_list = []
    for i in range(len):
        a_list = re.findall(r'<a .+?>', td_list[i, 1])
        temp = ""
        for a in a_list:
            temp = td_list[i, 1].replace(a, "").replace("</a>", "").replace("<br>", "\n").replace("<br />", "\n")
        meaning_list.append(temp)

    time_list = td_list[:, 2]
    able_list = td_list[:, 3]

    redeemcode = "礼包来源于bwiki，未更新不关我事\n"
    for i in range(len):
        if able_list[i] == '已过期':
            continue
        elif able_list[i] == '可兑换':
            redeemcode += f"----[{time_list[i]}]----\n{code_list[i]}\n"
            if meaning_list[i] != "":
                redeemcode += f"{meaning_list[i]}\n"
        else:
            raise Exception

    return redeemcode

def front() -> str:
    """前线"""
    def convert_hp(hp):
        hp = int(hp)
        if hp < 0:
            raise Exception("hp过小: "+str(hp))
        elif hp < 10000:
            return str(hp)
        elif hp < 1000000:
            hp = hp / 10000
            return str(round(hp,3))[:4] +"万"
        elif hp < 100000000:
            hp = hp / 10000
            return str(round(hp, 4)).split(".")[0] + "万"
        elif hp < 100000000000:
            hp = hp / 100000000
            return str(round(hp, 3))[:4] + "亿"
        raise Exception("hp过大: "+str(hp))

    text = ""
    json = requests.get("https://www.bigfun.cn/api/feweb?target=kan-gong-guild-user-info%2Fa", headers=headers, timeout=timeout).json()
    if json['code'] != 0:
        raise Exception(str(json))
    text += json['data']['guild_name'] # 公会名
    json = requests.get("https://www.bigfun.cn/api/feweb?target=kan-gong-guild-boss-info%2Fa",headers=headers,timeout=timeout).json()
    if json['code'] != 0:
        raise Exception(str(json))
    data = json['data']
    text += f"[第{data['round']}轮 Lv.{data['boss'][0]['level']}]\n"
    for b in data['boss']:
        elem = b['elemental_type_cn']
        name = boss_convert2(b['name'])
        hp = convert_hp(b["remain_hp"])
        text += f"{elem}·{name}: {hp}\n"
    total_hp = convert_hp(data['boss'][0]['total_hp'])
    text += f"满血量: {total_hp}"
    return text

def urge_blade(group_id, sender_id):
    qq_member_list = getMemberList(group_id)
    for qq_member in qq_member_list:
        if int(qq_member['id']) == int(sender_id):
            if qq_member['permission'] != 'ADMINISTRATOR' and qq_member['permission'] != 'OWNER' and str(qq_member['id']) != str(administrator):
                return [['text', '只有勇士战神和管理员可以催刀']]
            else:
                break

    # 查刀数的最后一天
    update_all()
    form = {}
    user_boss = {}
    for user in t_report[date_list[-1]]['data']:
        boss_list = [ [damage_list['boss_name'], damage_list['is_kill']] for damage_list in user['damage_list'] ]
        user_boss[user['user_name']] = boss_list
    count1 = {}
    for knife in report[date_list[-1]]:
        name = knife['user_name']
        l = count1.get(name)
        if l:
            count1[name] += [[knife['role'], knife['boss']]]
        else:
            count1[name] = [[knife['role'], knife['boss']]]
    for user in count1.keys():
        knife2 = []
        c = 0
        for i in range(count1[user].__len__()-1,-1,-1):
            role = count1[user][i][0]
            boss_count = (np.array(count1[user])[:i+1,0] == role).sum()
            if role in knife2 or boss_count == 2:
                knife2.append(role)
                boss_name = count1[user][i][1][2:]
                try:
                    user_boss[user].remove([boss_name, 1])
                except:
                    user_boss[user].remove([boss_name, 0])
                count1[user].pop(i)
                c += 0.5
        try:
            for u_b in user_boss[user]:
                if u_b[1] == 1:
                    c+=0.5
                elif u_b[1] == 0:
                    c+=1
                else:
                    raise Exception()
        except:
            c = 0
        form[user] = c
    # 催刀列表
    urge_member_dict = {}
    for user in member_dict.keys():
        if user in form.keys():
            knife = 3 - form[user]
            if abs(knife) > 0.1:
                urge_member_dict[user] = knife
        else:
            urge_member_dict[user] = 3
    member_count = len(member_dict)
    msg = [["text", f"催🔪 -> {member_count*3 - sum(urge_member_dict.values())}/{member_count*3} ({member_count})"]]
    for user, knife in urge_member_dict.items():
        msg.append(["text", f"\n剩{knife}刀->{user}"])
        if user not in urge_white_list:
            if user in urge_designated_dict.keys() \
                and urge_designated_dict[user] in [member['id'] for member in qq_member_list]:
                msg.append(["@", urge_designated_dict[user]])
            else:
                for qq_member in qq_member_list:
                    if user == qq_member['memberName']:
                        msg.append(["@", qq_member['id']])
    msg.append(["text","\ntip：如果没@到或者不想被@，请联系管理员"])
    return msg

def guild_draw_card(group_id, qq_id, order):
    today = datetime.date.today().strftime('%Y-%m-%d')
    if os.path.exists(draw_card_log_path):
        with open(draw_card_log_path,'r',encoding='utf8') as f:
            log = f.read().split('\n')
        if log[0] == today:
            for l in log[1:]:
                qqid, count = l.split(",")
                if qqid == qq_id and int(count) >= draw_card_limit:
                    return "今天抽过了哦"
        else:
            with open(draw_card_log_path, 'w', encoding='utf8') as f:
                f.write('')

    update_date_member()
    if date_list[-1] == today:
        user_name = ''
        qq_member = getMemberList(group_id)
        for member in qq_member:
            if str(member['id']) == str(qq_id):
                user_name = member['memberName']
                break

        for key, value in urge_designated_dict.items():
            if str(qq_id) == str(value):
                user_name = key
        if user_name not in member_dict.keys():
            return f"未找到玩家：{user_name}"

        res = requests.get('https://www.bigfun.cn/api/feweb?target=kan-gong-guild-report%2Fa&date=', headers=headers, timeout=timeout)
        data = res.json()['data']
        damage_num = -1
        for knife in data:
            if knife['user_name'] == user_name:
                damage_num = int(knife['damage_num'])
                if damage_num < 3:
                    return f"才{damage_num}刀也好意思？"
        if damage_num == -1:
            return f"你是不是还没出刀"
    
    with open(draw_card_log_path, 'r', encoding='utf8') as f:
        new_log = "" + datetime.date.today().strftime('%Y-%m-%d')
        old_date = f.readline()
        for old_log in f.read().split('\n'):
            if old_log == '':
                continue
            qqid, count = old_log.split(',')
            if str(qqid) == str(qq_id):
                new_log += f"\n{qq_id},{int(count)+1}"
                qq_id = None
            else:
                new_log += '\n' + old_log
        if qq_id != None:
            new_log += f"\n{qq_id},1"
    open(draw_card_log_path, 'w', encoding='utf8').write(new_log)

    return draw_card(order)

def guild_illness(group_id, qq_id, text):
    today = datetime.date.today().strftime('%Y-%m-%d')
    if os.path.exists(illness_log_path):
        with open(illness_log_path,'r',encoding='utf8') as f:
            log = f.read().split('\n')
        if log[0] == today:
            for l in log[1:]:
                qqid, count = l.split(",")
                if qqid == qq_id and int(count) >= illness_limit:
                    return "成为勇士战神的话，就能无限地使用哦！"
        else:
            with open(illness_log_path, 'w', encoding='utf8') as f:
                f.write('')

    with open(illness_log_path, 'r', encoding='utf8') as f:
        new_log = "" + datetime.date.today().strftime('%Y-%m-%d')
        old_date = f.readline()
        for old_log in f.read().split('\n'):
            if old_log == '':
                continue
            qqid, count = old_log.split(',')
            if str(qqid) == str(qq_id):
                new_log += f"\n{qq_id},{int(count)+1}"
                qq_id = None
            else:
                new_log += '\n' + old_log
        if qq_id != None:
            new_log += f"\n{qq_id},1"
    open(illness_log_path, 'w', encoding='utf8').write(new_log)

    return get_illness(text)
    



if __name__ == '__main__':
    # cds(path="./../image/guild/cds.png")
    # cd("好", path="./../image/guild/cd.png")
    # guild_damage(path="./../image/guild/guild_damage.png")
    # asd = requests.get("https://www.bigfun.cn/api/feweb?target=kan-gong-guild-user-info%2Fa",headers=headers)
    pass

