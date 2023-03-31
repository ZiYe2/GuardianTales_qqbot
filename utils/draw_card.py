import random
import datetime
import os


green_box = ['琳达','波比','海尔佛','利娅',
'杰伊','暴龙','东泰','佩吉',
'艾尔丽','阿加莎','达芬奇','凯特',
'玛利亚','丽莎','乔伊','布雷德',
'美娜','利奥','奥拉莉','康儿',
'聂恩','马蒂二世']
yellow_box = ['骑士','伊娃','埃尔韦拉','罗兰因',
'拉比','帕比','瑞秋','赫卡忒',
'可可','佩儿/梅儿','马修','克雷格',
'柚子','阿伊莎','夏皮拉','白兽',
'卡瑞娜','道尔夫','青叶','吉蒙里',
'艾米','玛丽安','索菲','吉尔瓦斯',
'赤雪','岚芳','凯瑟琳','莉耶',
'奈娃']
white_box_list = ['普利特维采','拉碧丝','阿拉贝尔', '蒂尼亚',
'瑞皮娜','兰儿','伊娃','尤金',
'玛丽娜','芭莉','比什巴赫','奈莉',
'比安卡','欧格玛','阿勒夫','美娅',
'未来公主','佳岚','贝丝','加百列',
'琳','未来骑士','维罗妮卡','诺克希娅',
'梅丽尔','鲁','MK.99','莉莉丝',
'罗茜','索菲','柚子','埃莉诺',
'辛缇拉','埃里娜','蕾伊','卡麦尔',
'MK.2','奥尔卡','康娜','哈娜',
'克拉拉','帕尔瓦蒂','普莉希拉','克劳德',
'娅拉','AA72','罗兰茵','疯狂熊猫团', 
'克罗塞尔','安德拉斯'] + ['卡洛儿']
up_role = '安德拉斯'

def get_white_box_list(up_role):
    if up_role != None:
        if up_role in white_box_list:
            white_box = white_box_list.copy()
            white_box.remove(up_role)
        else:
            return 
    else:
        white_box = white_box_list
    return white_box

def hundred_draw(up_role):
    white_box = get_white_box_list(up_role)
    if white_box == None:
        return f"我不知道叫'{up_role}'的角色哦"
    g = 0
    y= 0
    w = 0
    for _ in range(10):
        g_, y_, w_ = ten_draw_core()
        g += g_
        y += y_
        w += w_

    text = f"绿盒：{g}个\n黄盒：{y}个"
    if w == 0:
        text += "\n白盒：0个"
    else:
        for _ in range(w):
            if up_role != None:
                if random.random() < 0.5:
                    role = random.choice(white_box)       
                    text += f"\n★★★{role}"
                else:
                    text += "\n★★★up："+up_role
            else:
                role = random.choice(white_box)       
                text += f"\n★★★{role}"
    crystal = g + y*8 + w*50
    text += f"\n水晶数：{crystal}"
    return text

def ten_draw_core():
    green = 0
    yellow = 0
    white = 0
    for _ in range(9):
        probably = random.random()
        if probably < 0.8825:
            green += 1
        elif probably < 0.8825+0.0900:
            yellow += 1
        else:
            white += 1
    probably = random.random()
    if green != 9 and probably < 0.8825:
        green += 1
    elif probably < 0.8825+0.0900:
        yellow += 1
    else:
        white += 1
    return green, yellow, white
def ten_draw(up_role):
    white_box = get_white_box_list(up_role)
    if white_box == None:
        return f"我不知道叫'{up_role}'的角色哦"
    g, y, w = ten_draw_core()
    text = f"绿盒：{g}个"
    for _ in range(y):
        text += f'\n★★{random.choice(yellow_box)}'
    for _ in range(w):
        if up_role != None:
            if random.random() < 0.5:
                role = random.choice(white_box)       
                text += f"\n★★★{role}"
            else:
                text += "\n★★★up："+up_role
        else:
            role = random.choice(white_box)       
            text += f"\n★★★{role}"
    crystal = g + y*8 + w*50
    text += f"\n水晶数：{crystal}"
    return text

def single_draw(up_role):
    white_box = get_white_box_list(up_role)
    if white_box == None:
        return f"我不知道叫'{up_role}'的角色哦"
    probably = random.random()
    if probably < 0.7825:
        return "★"+random.choice(green_box)
    elif probably < 0.7825+0.1900:
        return "★★" + random.choice(yellow_box)
    elif probably < 0.7825+0.1900+0.01375 \
        or up_role==None:
        return "★★★" + random.choice(white_box)
    else:
        return f"★★★up：{up_role}" 
    
def draw_card(order) -> str:
    role = None
    if order[2:] == '角色列表':
        return "没做"
    elif order[2:] == '武器列表':
        return '没做'
    elif len(order) > 4:
        role = order[4:].replace(' ','').upper()
        if role == 'UP':
            role = up_role
        elif role not in white_box_list:
            return f"我不知道叫'{role}'的角色哦"
    # if check_ticket() == False:
    #     result = ""
    if order[:4] == "角色单抽":
        result = single_draw(role)
    elif order[:4] == "角色十连":
        result = ten_draw(role)
    elif order[:4] == "角色百连":
        result = hundred_draw(role)

    elif order[:4] == "武器单抽":
        result = "没做"
    elif order[:4] == "武器十连":
        result = "没做"
    elif order[:4] == "武器百连":
        result = "没做"

    else:
        result = f"抽卡指令错误：{order}"
        print(result)
    return "\n"+result




if __name__ == '__main__':
    # for i in range(100):
    pass

