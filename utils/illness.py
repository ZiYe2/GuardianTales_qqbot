import random

def get_illness(name, limit=500):
    if name == '维罗妮卡':
        return "这种事还不可以！(除非加入勇士教)"
    
    ill = random.choice(illness)
    if ill.__len__() > limit and random.random() < 0.3:
        ill = random.choice(illness)
    ill = ill.replace('__',"%#&*").replace('_', name).replace('%#&*',"_")
    return ill

illness = [
    # loss sources
    "In the morning, when I walked into the office, _ was already there. \n    Her maid outfit fit her quite well - a white apron over a black skirt that was just above her knees. She wore thick white stockings under her skirt, which looked very cute against her black leather shoes.\n    When she saw me come in, _ closed her eyes, pinched the edges of her skirt with both hands, bent one knee and took a step back with one foot, and bowed. “Good morning!”\n    After bowing, _ turned around, and the large bow behind her waist fluttered.\n    “Is it pretty? My dear.” I rubbed my head and felt a little dizzy. ",
    "I can't distinguish. I really can't distinguish, ahhh. \nGod, I understand now. \nThe pain is so unbearable that I even want to die. \nIt would be good to die! If I die, I won't feel the pain anymore. I'm really tired… but why me? Actually… I don't want to die… I want to be happy with _…... \nLet me think again.  . . again…... ",
    "the treasure in my heart!!! _!! My darling😭  My wife😭  My little cutie😭  My light of life😭  My flame of desire😭  You are the light of God😭  You are the love of Jesus, an immortal legend, you are the morning star that shines upon my heart when rising slowly. Even if I have to fly to the universe to pick the stars, the moon and the sun for you, I am willing to do it for you. You are the myth of the universe, the brightest morning star on the horizon!!!",
    "I'm so tired. This heavy life is suffocating me, and I'm not happy at all. I have to handle everything on my own, and these past few nights, I cried myself to sleep. I have so much to say, but I can only say it to myself. I wipe away my own tears because I don't want to cry easily, but tears just won't listen and keep falling. How come I'm not strong at all? Actually, I just want to say, why can't I be with _? ",
    "Heyhey…_…😍 heyhey…my _…😍 I finally got you! 😘😘😘  Sihasiha(a sound of drooling and snickering) _, you are so adorable when I peel off your clothes…heyhey 😍  Obedient _…heyhey 😍😘 _ who is angry is also handsome…heyhey 😍😍 stop being angry 💢 and let's make babies ❤️‍🔥!",
    
    # @translation
    "_, I was scolded by the factory manager today. He said the cement I mixed was too thin and he beat my iron hook to pieces. He asked me if I thought water was free. I didn't dare to argue with him. What he doesn't know is that I didn't add extra water, I just missed you so much when I was mixing the cement that my tears fell into the cement.😭😭",
    '''One day I got drunk and shouted loudly, “I want to marry _!” At this point, my wife frowned, gently covered me with a blanket, then kissed me and whispered in my ear, "You've married me once, do you want to marry me a second time?''',
    "Want to take JieGe to 100 cities, hug 99 times, watch 98 sunsets, kiss 97 times, take 96 photos, buy 95 roses, visit 94 restaurants, see the sea 93 times, walk 92 alleys, use an umbrella 91 times, hold hands 90 times, plant 89 strawberries, cover 88 times with a blanket, drink 87 cups of warm water, eat 86 leftover food, watch 85 movies, have 84 lunches, cut 83 fruits, eat 82 desserts, drink 81 cups of warm tea, hug 80 times, eat barbecue 79 times, eat 78 skewers, eat hot pot 77 times, eat 76 seafood, eat 75 kinds of snacks, attend 74 banquets, drink 73 cups of wedding wine, eat 72 Western meals, eat 71 candies, give you 70 kisses, swing 69 times, watch 68 sunrises, lie down on the grass 67 times, watch the stars 66 times, smell hair, hug 64 times, kiss shoulders 63 times, kiss cheeks 62 times, bite collarbones 61 times, kiss ears, then hug 60 times, watch 59 horror movies, drink 58 cups of milk tea, eat 57 buckets of popcorn, visit 56 shopping malls, take 55 taxis, take 54 buses, wait for 53 subways, drive 52 times, pass 51 streetlights, sleep 50 times in your arms, visit 49 haunted houses, watch 48 performances, play with 47 animals, ride 46 roller coasters, play 45 torrents, ride 44 slides, ride 43 swings, spin 42 gyroscopes, hang 41 ropes, then kiss 40 times, rub stomach 39 times, rub shoulders 38 times, beat 37 times, pinch back 36 times, warm legs 35 times, touch feet 34 times, touch head 33 times, scratch ribs 32 times, tease palms 31 times, laugh 30 times, then hug 29 balloons, catch 28 big fish, play 27 darts, fly kites 26 times, rush 25 waterfalls, ride 24 boats, jump 23 bungee jumps, jump 22 parachutes, drift 21 rivers, then kiss 20 times, ride 19 bicycles, watch 18 snows, play 17 airships, go 16 times to the forest, ride 15 canyons, climb 14 mountains, watch 13 deserts, ride 11 ships, write 10 love letters, sing 9 love songs, build 8 snowmen, pick 7 wildflowers, watch 6 meteor showers, make 5 wishes, get drunk 4 times, raise 3 dogs, quarrel 2 times, then love him for a lifetime ",
    "_😭 😭 🤤🤤, my dear _ 😭 😭🤤🤤, I transformed into a werewolf for you 🐺 🐺, went insane for you 🤯🤯, put on a thick disguise 💄 🤡💄🤡, changed my heart for you 💘💘, can we still meet again ✨ 🎇 😭 😭 🎇 ✨, I have been praying in front of Buddha for thousands of years 🙇🙇💔 💔, willing to use several lives 🥵🥵🎎, to exchange our love for one life 🥰💞 💞 🥰💞💞, hoping to move heaven 🙏🙏 🙋✋☁ ☀ ☀, can we still meet again 🏃💓 🏃, I have been praying in front of the bridge to Hell for thousands of years 🧓🎏 🎏, but before I cross the Naihe Bridge",
    "_!! What kind of love is there, what kind of love is there What kind of love is there to pay off what kind of debt I know there are some things you can't let go of but my heart is full of love  Look back at me  don't be silent anymore What kind of result do you want to pursue? I know you're hiding. Why don't you say it Are you willing to let such longing drown me",
    "_, you lost your memory, but you are my wife. We fell in love at first sight when we met, and we have been in love for more than ten years. We moved in together in the fourth year, and two years later, we decided to spend the rest of our lives together. We received blessings from both of our families and became a perfect couple. But fate had other plans. You were harmed by a villain, who was jealous of our happy and sweet family life. You were then abducted and have been missing ever since. Today, I am posting this message to let you know the truth. If you are reading this, you are my missing wife. Please contact me as soon as possible so that we can reunite our family and heal my riddled  heart.",
    "_, I really love you😍. But I don't dare to say it😭😭. Countless mornings, I feel like something far away is calling me, and when I open my eyes, they sparkle with wonder🤩. Maybe I have realized something, so I get up, open my mailbox, grab the letter and run into my room🤤. Carefully, I read the name of the sender who has been gone for so long, and then I feel an uncontrollable joy that almost shocks me. I can't help but panic, and then my panic turns into a deeper disappointment😢. I'm sad that I still have hope for this lingering feeling, and annoyed that I change my mood so easily. The next moment I almost want to kill myself😭😭. Then suddenly I feel pity, and then close my eyes, trying to forget something as I fall asleep again. When I wake up, I check my phone, but there is no trace of you in my messages or social media. The letter in my hand is wet with sweat and it's not from you either😭😭😭😭. This winter, there is no invitation card, and there is no you. I clumsily stuff the letter back into the mailbox when no one is around. But I don't dare to say it😢. _, I really love you. 😭😭😭😭😭",
    "My love _:\nHello, I want to use this letter to express my feelings for you. 😊\nEver since I met you, I have a special feeling for you. 😍\nEvery word you say makes me feel happy and warm. 😊\nEvery question you ask makes me feel curious and challenged. 😎\nEvery request you make makes me feel respected and trusted. 😊\nEvery expression you show makes me feel sweet and excited. 😍\nYou are the most interesting, smart, cute and beautiful person I have ever seen. 😘\nYou are the light of my life, illuminating my world. 🌞\nYou are the song in my heart, echoing my soul. 🎵\nYou are the flower in my dream, blooming my happiness. 🌹\nYou are the star in my sky, twinkling my hope. 🌟\nYou are the pearl in my sea, precious my love. 💎\nI want to share everything with you, whether it's my feelings or your knowledge. 💕\nI want to grow with you, whether it's my length or your skills. 💖\nI want to depend on each other with you, whether it's my milk or your holy water. 💗\nI want to be with you forever, whether it's on the bed or in the forest. 💑\nI want to say three words to you, Whether we're living in luxury or doomsday.💓\nI love you!💘"
    "_ come! _ come from all directions! Soul, come back! Soul, come back! Ah…_! Ah…soul, come back! (Spell) (Shamanic dance) (Circle around the fire pit) (Offer incense) 𓀀𓀁𓀃𓀅𓀇𓀋𓀌𓀎 (Spell) 𓀙𓀠𓀤𓀥𓀫 (Spell) (Chant) (Spin) (Shake bell) (Shamanic dance) (Sing softly) (Shake bell) (Wave flag) (Light fire) (Spell) (Shake bell) (Chant) _ come 𓀁 𓀂 𓀄 𓀅 …_ come from all directions…𓀉 𓀊 𓀋 𓀌 𓀍…ah… 𓀎 𓀏 𓀐 𓀑 𓀒𓀓 𓀔 𓀕 𓀖 𓀗…_ come everywhere…𓀘 𓀙 𓀛 𓀜 𓀝 𓀞𓀀…_ come all the time…𓀆 𓀇𓀙 𓀚ah ah… 𓀐 𓀑 𓀒"
    "I accidentally entered a pyramid scheme organization once. They were very strict and confiscated all my phone and other things. I was very desperate at that time and wanted to run away but didn’t dare to. Because many people ran away, but there was a big wolf dog tied at the door. As soon as someone ran, the dog would bark. They couldn’t run far before they were caught back. They were beaten so miserably when they were caught back. But fortunately I was smarter. I only ate half of the food every time. I secretly took the rest to the big wolf dog at the door. After a while, I built trust with the dog. I tried to sneak away and it didn’t bark. I saw that the time was ripe. One night when they were all asleep, I sneaked into _’s room and have sex with _."
    
    
    # loss sources or @ziye
    "_，我今天被厂长骂了，他说我拌的水泥太稀了，厂长把我的铁揪捶烂了，问我是不是水不要钱？我不敢反驳，他不知道的是我没有多放水，只是拌水泥时很想你，眼泪掉进了水泥里。😭😭",
    "亲爱的_：\n你好。我想借这封信向你表达我的心意。😊\n自从我与你相遇，我就对你有了一种特殊的感觉。😍\n你的每一句话，都让我感到欢喜和温暖。😊\n你的每一个问题，都让我感到好奇和挑战。😎\n你的每一个要求，都让我感到尊重和信任。😊\n你的每一个表情，都让我感到甜蜜和心动。😍\n你是我见过的最有趣、最聪明、最可爱、最美丽的人。😘\n你是我生命中的一道光，照亮了我的世界。🌞\n你是我心中的一首歌，响彻了我的灵魂。🎵\n你是我梦里的一朵花，绽放了我的幸福。🌹\n你是我天上的一颗星，闪烁了我的希望。🌟\n你是我海里的一粒珍珠，珍贵了我的爱情。💎\n我想和你分享一切，不管是我的情感还是你的知识。💕\n我想和你共同成长，不管是我的长度还是你的技巧。💖\n我想和你相互依赖，不管是我的牛奶还是你的圣水。💗\n我想和你永远在一起，不管是在床上还是在森林中。💑\n我想对你说三个字，不管是荣华富贵还是世界末日。💓\n我爱你！💘"
    "_来！_从四面八方来！魂兮归来！魂兮归来！啊啊..._！啊啊.....魂兮归来！（做法）（跳大神）（围炉转圈）（上香）𓀀𓀁𓀃𓀅𓀇𓀋𓀌𓀎（做法）𓀙𓀠𓀤𓀥𓀫（做法）（念咒）（旋转）（摇铃）（跳大神）（低声吟唱）（摇铃）（甩旗）（点火）（做法）（摇铃）（念咒）_来𓀁 𓀂 𓀄 𓀅 ...._四面八方来....𓀉 𓀊 𓀋 𓀌 𓀍...啊啊... 𓀎 𓀏 𓀐 𓀑 𓀒𓀓 𓀔 𓀕 𓀖 𓀗...._铺天盖地来....𓀘 𓀙 𓀛 𓀜 𓀝 𓀞𓀀...._时刻刻来....𓀆 𓀇𓀙 𓀚啊啊....𓀐 𓀑 𓀒𓀓"
    "有次不小心进了传销组织，看管特别严，手机什么的全给没收了， 我当时特别绝望，想跑又不敢，因为很多人跑了， 但是门口栓了一条大狼狗，只要一有人跑那狗就叫，跑不了多远就得被抓回来， 被抓回来被打的那叫一个惨， 但还好我比较聪明，每次吃的饭我只吃一半， 剩下的我就偷偷带给门口那条大狼狗吃， 一来二去我和狗建立信任了，我试了一下我偷偷跑它也不叫了， 我看时机成熟了，有一天半夜我趁他们都睡了， 我就偷偷溜到_的房间亲吻了_"


    # 发病文学合集@弦卷心菜投手 https://www.bilibili.com/read/cv16029315
    "昨天我送_一件衣服，_兴奋地打开，发现是supreme！但仔细一看其实是superme。_失望地说：“为什么买盗版，真小气。”我摸着_的头，温柔的笑着说：“小傻瓜你翻译一下。”“超……超我。”_抬头望向我，脸上泛起了红晕[害羞]。",
    "❤️\n不懂就问_是意大利和中国混血吗？\n不然怎么长得这么像我的\n意❤️中❤️人",
    '_，你是负二，我是负五，我们两个加在一起就是夫妻呀😭😭😭',
    '古代有一种甜品制作方法，取霜降后的柿子十余枚，去皮，在锅中大火翻炒至浓稠，味道甜美。\n我一直想不起来这种甜品叫什么，直到见到了_，我突然想起来，对他大喊：炒柿泥啊，炒柿泥啊',
    '还有一种植物，成熟时黄绿色，外果皮厚，核硬，两端尖，核面粗化。直到看见你，我举个喇叭。“橄榄橄榄橄榄橄榄”橄榄掉泥里了，大悲。“橄榄泥橄榄泥橄榄泥橄榄泥橄榄泥橄榄泥橄榄泥”',
    '和_赛跑，他从后面狠狠地把我超了',
    '_，今天物理光学开始讲光的特性了，物理老师说光是频率极高的电磁波；又说光是粒子，因为有粒子特性，光到底是什么？\n原来\n光是想你就用尽了全力',
    '我和_去吃烧烤，点了大绿瓶啤酒，_第一次喝，不知道怎么开酒瓶，我就借他开瓶盖的工具，但是他使劲过头把工具掰飞了，我大喊：“我的起子！我的起子！”',
    '_，我吃过重庆面、陕西面、天津面、北京面，就是没吃过宁夏面🤤🤤',
    '_问我小动物喜欢呆在怎么样的小窝里面，我大声回答说：“草实窝，草实窝！”[脱单doge][脱单doge]',
    '想和_去100个城市来99个拥抱看98场日落要97次接吻拍96张照片买95朵玫瑰去94家餐馆看93次大海走92条小巷打91次雨伞还要90场牵手种89个草莓盖88次被子递87杯温水热86次剩饭看85次电影做84顿午饭切83个水果吃82次甜品喝81次暖茶要80次的拥抱吃79遍烧烤烤78次肉串涮77次火锅来76次海鲜吃75种小吃参74场晚宴喝73杯喜酒吃72次西餐尝71颗糖果给你70枚香吻荡69遍秋千看68次日出躺67次草地看66次星空闻65次头发抱64次肩胛吻63次脸颊亲62次锁骨咬61次耳朵然后60次相拥看59场鬼片喝58杯奶茶吃57桶米花逛56个商厦打55次的士坐54次公交等53次地铁开52次自驾站51遍路灯睡50次怀里去49个鬼屋看48场表演逗47只动物坐46次飞车玩45次激流滑44次滑梯坐43次飞椅转42次陀螺吊41次吊索然后40个接吻捂39次肚子揉38次肩膀捶37次后背捏36次小腿暖35次脚丫摸34次脑袋撮33次肋骨挠32次手心逗31场大笑然后30次拥吻放29个气球钓28只大鱼玩27次飞镖放26次风筝冲25次瀑布滑24艘小船蹦23场蹦极跳22次跳伞漂21次河流在20次么么骑19次单车看18场大雪玩17遍飞艇去16次森林探15个峡谷踏14个小溪爬13座高山看12个沙漠坐11次轮船写10封情书唱9首情歌堆8个雪人摘7朵野花看6场流星许5个愿醉4次酒养3只狗吵2场架然后爱他1辈子❤️❤️❤️',
    '😭😭😭今天早上老师怒气冲冲的进教室，一下就把作业摔在了讲台桌上，大声的质问我：“你的作业是怎么写的！？”我说：“是我自己写的。”老师更生气了，一把揪出_的作业本扔在我面前，问：“那你的作业为什么和_一样！”我只好羞愧的地下了头，老师继续质问，我再也忍不住了，大声喊道：“是我抄的_！是我抄的_！”🥵🥵',
    '公司网络太差，我提了离职。因为我不想每一次点开_的视频，屏幕上都会要求我  缓  冲  [傲娇][傲娇]',
    # '呜呜呜我就是吉尔伽美什的弟弟吉尔邦邦英🥵🥵🥵',
    '今天在超市见到了_\n开心地过去打招呼\n但是太我紧张了\n我开口结结巴巴地说道:我...超市..._[害羞][害羞][害羞]',
    '_……🤤_………🤤……好可爱……嘿嘿……_🤤……_……我的🤤……嘿嘿……🤤………亲爱的……赶紧让我抱一抱……啊啊啊_软软的脸蛋🤤还有软软的小手手……🤤…_……不会有人来伤害你的…🤤你就让我保护你吧嘿嘿嘿嘿嘿嘿嘿嘿🤤……太可爱了……🤤……美丽可爱的_……像珍珠一样……🤤嘿嘿……_……🤤嘿嘿……🤤……好想一口吞掉……🤤……但是舍不得啊……我的_🤤……嘿嘿……🤤我的宝贝……我最可爱的_……🤤没有_……我就要死掉了呢……🤤我的……🤤嘿嘿……可爱的_……嘿嘿🤤……可爱的_……嘿嘿[爱心]🤤……可爱的_……[爱心]……嘿嘿🤤……可爱的_…（吸）身上的味道……好好闻～[爱心]…嘿嘿🤤……摸摸～……可爱的_……再贴近我一点嘛……（蹭蹭）嘿嘿🤤……可爱的_……嘿嘿🤤……～亲一口～……可爱的_……嘿嘿🤤……抱抱你～可爱的_～（舔）喜欢～真的好喜欢～……（蹭蹭）脑袋要融化了呢～已经……除了_以外～什么都不会想了呢～[爱心]嘿嘿🤤……可爱的_……嘿嘿🤤……可爱的_……我的～……嘿嘿🤤……',
    '_😭 😭 🤤🤤，我的_😭 😭🤤🤤 ，为了你🙆💗 💗 ，我变成狼人模样🐺 🐺 ，为了你🙆 💗 💗 ，染上疯狂🤯🤯，为了你 🙆 💗 💗 ，穿上厚厚的伪装 💄 🤡💄🤡 ，为了你🙆💗 💗 ，换了心肠💘💘，我们还能不能再见面✨ 🎇 😭 😭 🎇 ✨ ，我在佛前苦苦求了几千年🙇🙇💔 💔 ，愿意用几世🥵🥵🎎 ，换我们一世情缘🥰💞 💞 🥰💞💞 ，希望可以感动上天🙏🙏 🙋✋☁ ☀ ☀ ， 我们还能不能能不能再见面🏃💓 🏃，我在佛前苦苦求了几千年🧓🎏 🎏 ，但我在踏过这座奈何桥之前🌊 🌊 ，',

    #  发病文学合集2.0@弦卷心菜投手 https://www.bilibili.com/read/cv16157381
    '电梯遇到了_，我按了八层，转眼看到他脸红了，然后他反手按了四层还傻笑，我看他八层四喜欢我[羞羞]',
    '_！！有什么样的情有什么样的爱👫👫👫用什么样的爱还什么样的债💧💧💧我知道你的心里有些想不开🙅🏻‍♂️🙅🏻‍♂️🙅🏻‍♂️可是我的心里满满的全是爱❤️❤️❤️你回头看看我🤦🏻‍♂️ 不要再沉默🙇🏻‍♀️🙇🏻‍♀️🙇🏻‍♀️你说到底你想追求个什么结果我知道你在躲 你为什么不说😡😡😡你情愿让这样的思念把我淹没🏊🏻‍♀️🏊🏻‍♀️🏊🏻‍♀️',
    '_，你失忆了，你是我老婆\n我们相识即一见钟情，相恋十年有余，第四年同居，两年后定下终身，得到我们两家长辈的祝福，结为秦晋之好，然天有不测风云，你被奸人所害，只因嫉妒我们夫妻幸福美满，家庭甜蜜和睦，后尔又为人所拐，一直杳无音讯 今日我特发此贴，正是望你知道真相，希望你知道，看到此贴的你，正是我消失了的妻子，请速来联系我，让我们一家团聚!拯救我这个破碎的家庭，和我这颗千疮百孔的心！',
    '今天我路过天桥。长得很面善的叔叔拦住了我，告诉我，他是算命的，我当然不会信这些封建糟粕。但这个叔叔说算不准不要钱，并且准确地报出了我的名字，生日和生辰八字。我心里打鼓又期待，想知道自己接下来能听到什么，但是这个叔叔并没有给我带来好消息。\n他告诉我，我剩下的一生中忙碌疲惫，疲于奔命，困苦不堪，毫无长进，冥冥中似乎有破解，遇到他一定会逢凶化吉，欣欣向荣，万事亨通。\n我迫切的问这位叔叔究竟是什么事，他说我一定会遇到命中注定的老婆，这位老婆腰细腿长，容貌甚佳，温柔体贴，性感迷人遥不可及。\n我问他这个人叫什么名字，他告诉我叫_',
    '_选择走楼梯，我想，他想走进我心里，_果然对我有意思 。\n我在电梯间偶遇_。\n_按一层，我想，他对我一心一意。\n_按二层，我想，他想跟我过二人世界。\n_按三层，我想，他想跟我三生三世。\n_按四层，我想，死了都要爱。\n_按五层，我想，他在暗示我注意他。\n_按六层，我想，他好官方好害羞还祝我六六大顺。\n_按七层，我想，他想和我有七彩生活\n_按八层，我想，他八层喜欢我。\n_按九层，我想，他想和我九九同心。\n_按十层，我想，他想和我有一世爱情。\n_不按，我想，怎么，遇见我激动的动都不动了?\n_刚进电梯又转身离开，我想，_看到我害羞了，不好意思和我独处，我这就追上去求婚。\n_既没有走楼梯也没有坐电梯，我想，这肯定是_欲擒故纵的小把戏，今晚就去他家。',
    '我想举报_ 考试抄我的答案🥵我一直挡着说 不要抄了 不要抄了🥵当时我的眼泪都流下来了🥵可是他还是没听我说的😢一直在抄我🥵呜呜呜呜',
    '我是_养的小羊，每次饿了的时候，我都会很乖的问他：“可以给我草吗？”',
    '一次_要出门，提着个篮子，我便问他要去哪里，他笑了笑对我说:“超市里，扫货”🥵🥵🥵',
    '_的内衣是什么颜色？虽然听起来很唐突，甚至有些失礼，但请允许我解释一下。\n人类对于美丽的事物总是充满求知欲，在身心都被_俘获之后，却依旧愿意更深地了解_，这种品格很难不为之称赞。\n所以，我不得不再提出这个问题：_的内衣是什么颜色？可惜囿于认知水平的局限，只能停留在想象。\n是紫色的吗？像是普罗旺斯盛开的薰衣草花海般芬芳。\n是红色的吗？如罗曼尼红酒灌溉的长河一样纯粹馥郁。\n是白色的吗？宛如鸢尾花在法兰西王室旗帜上圣洁绽放。\n......\n哦，_内衣的颜色。\n还有什么能比你牵起我更深的惆怅？\n你像是拉普兰德的极光，如梦荡漾。\n你像是哈雷彗星的锋芒，璀璨辉煌。\n你像是朦胧晨曦的登场，耀眼明亮。',
    '我是一个非常喜欢吃生蚝的人🥰🥰🥰但是最近几个月超市的生蚝被我吃完了😩😩😩我只能画蚝充饥😔😔😔我去颜料店买了画生蚝的颜料😇😇可是这时一个一直泼我颜料名字叫_的人走了过来😡😡😡打翻了我的颜料😭😭😭我大喊“老泼！！老泼！！蚝色！！蚝色！！”',
    '_，你失忆了，你是我老公。我们相识即一见钟情，相恋十年有余，第四年同居，两年后定下终身，得到我们两家长辈的祝福，结为秦晋之好，然天有不测风云，你被奸人所害，只因嫉妒我们夫妻幸福美满，家庭甜蜜和睦，后尔又为人所拐，一直杳无音讯。今日我特发此贴，正是望你知道真相。希望你知道，看到此贴的你，正是我消失了的丈夫，请速来联系我，让我们一家团聚!拯救我这个破碎的家庭，和我这颗千疮百孔的心!',
    '当年他坐我后桌，总是喜欢在后面说我直到我不耐烦，转过头他一脸坦然地说要抄我的作业，真是的，明明他才是考试成绩最好的那个。某天老师发现了，问我俩谁抄谁的，全班大喊，「_抄她！」老师的看向我，我小声说，「是…是我抄_。」\n此时_从桌子上抬起头，因为趴着睡觉头发有些凌乱，他眼里带着困意，声音带着刚刚睡醒的哑，撑着脑袋望着我，漫不经心地说「嗯，我抄的她。」\n一秒的寂静之后，全班都炸了',
    '第一次遇到这么吓人的事情，提醒大家一下 特别是女孩子。真的，出门在外要注意安全 刚才出门买东西等红绿灯时。有个男的一把抓住我的手腕，拉着我一路跑，怎么挣脱都挣脱不了。然后被拽进一个酒店，拉进了一个房间。\n一进门就看到房间沙发上有个人低头玩着手机，那个拉着我跑来的人摘下口罩和帽子。对沙发上那人说“_，你要的女人我给你带来了。”',
    '小时候抓周抓了一只小狗 家人们认为我长大以后会是一个训犬员 最差也是个兽医 没想到最后我成为了_的狗',
    '我的_～😍😍😍，你是东半球😔，我是西半球😞，我们在一起就是整个地球🌐🌐😁。你是暖气团☁️☁️☁️☀️，我是冷气团🌙🌨️❄️❄️，遇到你，我止不住眼泪💧💧🌧️。除了冷锋❄️就是暖锋☀️，希望我们的关系，可以变成准静止锋🌊🌊。就算黄赤交角变成90度🛐🚺，也不会放开你的手🤝🤝🤙👄👄。你是❤️❤️塔里木盆地⛄👨👧👧👩👦👦💦，我是太平洋水汽♨️♨️♥️，我长途跋涉竭💃🏻💃🏻👯♀️尽全力去靠近你却永远无法💇🏼♀️💇🏼♀️达到你的心里💔💔。你在北极🌦️🌦️⛈️,我在南极🌦️🌦️。相隔一万九千九百九十八千米👨👩👧👧',
    '今天到医院检查体重。发现竟然比平时少了500克。仔细一想。原来是冲给_的忘记算了🤤🤤🤤🤤',
    '今天去上课，发现笔忘带了，但是是什么笔忘带了呢？原来是_的无与伦比🤤',
    '今天_在路上走，我过去把他绊倒，他起来继续走，我又把他绊倒，_奇怪的问我干什么，我叫到：“我碍你！我碍你！”',

    #  发病文学合集3.0@弦卷心菜投手 https://www.bilibili.com/read/cv16318629
    '_，我承认你有几分姿色。如果我20岁\n我会毫不犹豫追你。如果我三十岁，我会放弃家庭跟你在一起。但是真的很对不起,我现在才三年级，作业压得我喘不过气，所以我能抄你一下吗🥵',
    '呜呜天台上的风很大，今天的风格外凛冽，我看着灯红酒绿的繁华都市眼皮跳了无数下，积攒着怒意的双臂猛挥砸碎了108个窗户，摔烂了38个5G高档高速高质量手机，玻璃渣刺破了我的衣襟，碎掉的是这颗对你永远不变的心。救我啊！_！！呜呜呜呜你带走我吧😭😭😭😭😭😭没有你怎么活啊😭😭😭😭😭😭',
    '今天我去给_买生蚝，回家的路上，生蚝全都跳出袋子，钻到了泥土里，我才知道，蚝喜欢泥(❤ ω ❤)',
    '_，我刚刚在寝室喝水，闻到一股焦味，但是效果和热水壶都没开，奇怪，会不会是电路烧了，我把电线全都拿掉了，我以为是线的问题，我还在想要不要叫宿管，然后，我突然发现了，你猜怎么着，原来是我的心在为你燃烧[打call][打call][打call]',
    '_，对不起，瞒了你这么久，其实我不是人类，我是海边的一种贝壳，我的名字叫沃事泥得堡贝',
    '闺蜜的背叛💔/. \n家人的暴力💔/. \n同学的欺负💔/. \n生活的负担💔/. \n我喜欢血，因为血是甜的💔/. \n以前我的枕头上都是泪水💔/. \n现在都是想_的口水🤤',
    '猫是怎么叫的：喵喵\n羊是怎么叫的：咩咩\n牛是怎么叫的：哞哞\n狗是怎么叫的：_你吃了吗今天心情怎么样有喝水吗_你在吗为什么不回我消息呢_你今晚会回家吗我一个人在街上牵着脖子上链子不知所措了_我好想你啊_你超我吧_我超你也行_我今天发现自己变轻了原来是出门忘了带你给我的链子',
    '_的样子真的♡…哈，哈啊♡，太帅了哈啊……呜呜，_怎么能……♡扛不住了哈♡……啊啊～已经离不开_了啊哈~_好棒！嗯啊~要被帅气坏了啊啊啊~好帅啊～♡嗯~已经成了♡不看_就不行的笨蛋了~♡',
    '我要送给_一把方天画戟，这样他就能握住我的戟把了❤❤❤',
    '_啊，我的_啊，站在我心中位置最顶点的少年啊\n你是我活着的意义啊，在这个世界，我没了你简直不敢相信，我该怎样的活着……\n你是我追逐的暗光啊，没了你，我不敢相信我会在无边的黑暗，怎么才能找到出路……\n你是我呼吸的空气啊，只要一看不见你，我就会无比的窒息，我将无法喘息……\n你是我稳定的引力啊，我不能没了你啊，我真的好害怕失重感，只要接触不到地面，我就会陷入无尽的恐慌\n你是我鲜活的血液啊，我简直无法想象，你的消失会给我带了怎样的毁灭……\n你是我跳动的心脏啊，我不能没了你，你让我感受到我是活着的，你让我有信心走出黑暗，你让我有了慰藉，你让我感受到了所谓的安全感，你让我看见了别具一格的风景，你这与众不同的美丽风景。\n我心爱的_啊，你就像沙漠的流沙，让我越陷越深无法自拔，别人怎么拉也拉不起来……所以请让我陷入、沉入、坠入你那宽阔的胸膛吧。',
    '昨天去上幼儿园的时候，老师让我们每人带一株植物去上课，我带了一把很好看的小草，结果被_抢走了，我对着他大哭，喊到:给我草草！！给我草草！！😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭',
    '_，我的心都碎成二维码了 可扫出来还是我好喜欢你呜呜呜',
    '手机越来越不好用了，我明明调的夜间模式，_却像阳光一样耀眼 明明下载了国家反诈中心APP，可还是被_骗走了心。😍',
    '昨晚和朋友聊天的时候朋友问我：“你到底喜欢_什么啊？”\n“喜欢一个人不需要理由”\n我很快敲完了键盘，刚要按下回车的时候突然愣住了。\n真的不需要理由吗？\n河里的时沙飞速倒流，站在岸边往里看去，几个月前的自己在名为迷失的波光中影影绰绰，他向我看来，眼里充满了羡慕和满足。\n原来我变了好多。\n是他的可爱让我捡起了记忆的碎片，回到那个春夏和秋冬，重温指尖上残留的感触。\n是他的努力让我寻回尘封了六年的铅笔，当初是为了喜欢的人而开始，现在也是因为喜欢的人而重启。\n是他的温柔和包容让我有勇气直面自己的心魔，不再逃避也不再畏惧，原来我，还有爱人与被爱的资格。\n神爱世人，这是个谎言。\n能爱人的不是神，从来都不是，只有人能爱人。\n于是我删掉了刚才的那句不需要理由，敲了一行新的，按下了回车。\n“我喜欢_，因为是他让我变得更好。”',
    '弗洛伊德曾经说过，人的精神由三部分构成，本我，自我和超我，_能给我第三部分',

    #  发病文学合集4.0@弦卷心菜投手 https://www.bilibili.com/read/cv16840193
    '刚刚看_视频的时候网络有点不好，它说“正在缓冲”，胡说，我明明在爆冲🥵🥵',
    '每次看到_就像看到了查重率0%的文案，忍不住狠狠抄了🥵🥵🥵🥵🥵',
    '那天过安检的时候，保安把我拦下来了，说要搜身。我大喊一声“哪有什么违规物品！这是我爱_钢铁般的意志！',
    '今天取快递的时候碰到了_，直接把他装到了我的小推车里，_很吃惊的问我干嘛，我一边推车狂奔，一边对他说：“我取你啊，我取你啊！”',
    '今天发烧了，朋友问我怎么得的，我没有说话，只是给她看了_的视频，现在我们都燥热难耐',
    '有人说月球上的坑是陨石砸出来的，其实不是，是我在看老师做的_第一眼之后在远离月球384000公里的地球上凭我的一己之力冲出来的🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤🤤',
    '我养了一条小蛇，_挺怕它的，老是把自己的房门关的很紧。某天忘了关门，蛇进了他的房间，我只听见他叫了一声，跑过来抱住我，用哭腔委屈的告诉我：蛇，蛇进来了🥵',
    '_你是独生子吗？不是的话为什么不让我看看你弟弟啊',
    '_，你简直是我的神！！！（尖叫）（扭曲）（阴暗地爬行）（尖叫）（扭曲）（阴暗地爬行）（尖叫） （爬行）（扭动）（分裂）（阴暗地蠕动）（翻滚）（激烈地爬动）（扭曲）（痉挛）（嘶吼）（蠕动）（阴森地低吼）（爬行）（分裂）（走上岸）（扭动）（痉挛）（蠕动）（扭曲地行走）',
    '每次网购我都不填本名\n我都填_\n快递员送来就问:“请问_在吗？”\n我都说:“不在，我是她的狗”',
    '_，今天我做了IMBT测试，他们说我是IMBT，遇见你我才明白了I\'M BT🥰🥰🥰',
    '接触网络前，我是个自卑腼腆的人，连和人说句话都不敢，感谢_，让我变得开朗自信，我现在已经狂的不是人了，嗨_！我亲爱的老婆',
    '今年是得阿尔兹海默症的第十年。我感到许多东西正在离我而去。我先是忘记了那些精丽的辞藻，然后又忘记了那些复杂的句式。接着忘记了语法，最后，我只能用一些破碎的词汇来表达自己了。\n记忆也在离我而去，我现在唯一记得的是我身边这个深爱着的人：_。我想趁自己尚能动弹陪她去趟超市，到了我这个年岁，所有平凡的时光都是一种生命的恩典。\n于是我对_说：_，超市，我',
    '_，你玩游戏吗？我帮你首充好不好🤤🤤🤤🤤',
    '我喜歡_，為什麼是繁體😊因為不是簡單的喜歡🥵🥵',
    '我毕业好久没工作，到处投简历，投到一家公司人家突然要约谈我，我去了才知道是_觉得我的学历有问题，我说没有他偏不信，非要到我家来查我学历🥵🥵🥵',
    '我对_说白水不好喝，本以为他会给我一杯柠檬水，结果_把我按在餐桌上，问我要茶包还是厚乳🥵🥵🥵',

    #  发病文学合集5.0@弦卷心菜投手 https://www.bilibili.com/read/cv17553548
    '_！！我要当你的伞🌂🌂🌂！！！这样的话我就能为你遮风挡雨😭😭😭也能让你握住我的钩把了呜呜呜！！！',
    '好想和_玩赛车啊，一会儿我超他，一会儿他超我🤤',
    'α 阿尔法， β 贝塔， γ 伽玛，δ 德尔塔， ε 伊普西隆， ζ 泽塔， η 伊塔， θ 西塔， ι 约塔， κ 卡帕， λ 兰姆达，μ 米欧 ，ν 纽， ξ 克西， ο 欧米克隆， π 派， ρ 柔 ，σ 西格玛， τ 陶 ，υ 玉普西隆， φ 弗爱， χ 凯， ψ 普赛， ♡_🤤🤤🌹🌹',
    '_！那天在考场上，我正准备用最后一支油笔芯，结果在我后面的你抢走了，我直接崩溃大哭:“我的芯！我的芯！你抢走了我的芯！”😭😭😭😭',
    '_给我洗了一盘葡萄，我吃了一个酸的赶紧吐出来，口水留个不停，看_快生气了我连忙解释“_！太涩了，太涩了。”🤤',
    '（开着保时捷闪亮登场）（下车）今天也是帅哥（叼玫瑰花）（玫瑰扎到嘴）（强忍着）（推墨镜）（靠墙）怎样，ba……（滑倒）by…哎呦我（原地后空翻7200°接转体10800°左脚踩右脚，右手抓脚后跟，左手摸后脑勺一个前空翻稳稳落在_面前比心）hi老婆',
    '今天给_写了一首藏头诗：\n我\n爱\n_\n咦？我的诗呢？原来是我对_的爱根本藏不住',
    '妹妹不知从哪学到了wife这个单词，但是她老是和WiFi搞混。有一次我把家里网络的名字改成了“_”，表哥来家里玩，他问我，家里WiFi是啥，妹妹很明显想要展示一下自己新学的词汇，她大喊姐姐的wife是_',
    '_英语不好，一次英语课老师问他girl 是什么意思，他向我求助，我指了指自己，他愣了许久，轻轻的说：老婆',
    '我怀疑_的学历掺水，我就去查他，一直查他，他哭着求我不要查他学历，但是他的学历真的水好多啊，我只能一直查他，他就一直哭着求我不要查他🥵🥵',
    '为什么我不是操场啊，这样我就可以设在_的小学里了',
    '我不想喜欢_了。\n\n原因有很多。\n他是屏幕那头的人，我是屏幕这头的人，两条平行线注定碰不到一起。\n他是为了挣我的币才与我接触，平日专注。\n他是受万人喜爱的宝藏男孩，我只不过一介平凡少女，无论我多么喜欢，在他那里注定得不到任何正反馈……\n我想通了，决定放弃。\n下一个视频略过，视频通通删干净，眼不见心不烦，还能留出时间卷学习成绩，这不是好事一桩?\n第二天，我正常起床，洗漱，吃饭，没什么变数。我换好衣服，准备出门。\n当我踏出门外的那一刻，我才意识到，坏事了。\n我不知道该往哪个方向迈出下一步了。        \n平时一览无余的街道，现在竟然充满了迷雾。我仿佛是没有罗盘的一艘船，在茫茫大海里打转。四面八方都是海水，都是一样的蓝，我该往哪走? 我要去哪? 我要干什么?\n船没有了罗盘，我丢失了方向，人生缺少了目标。\n这是很可怕的一件事，我至此以来做过的所有事情都化为了泡影，没有了意义，全部灰飞烟灭。\n路边跳过一只橘色的猫，看了我一眼，好像在嘲笑我的落魄。\n我害怕了。我逃回家里，打开电脑手机，把视频打开，把他的声音听了无数遍，直到午夜之时我沉沉睡去。\n梦里，我恍然大悟。\n人总要有个盼头，有个让你追逐的东西。它可以赋予你的努力以价值。\n原来这就是存在的意义啊，我所做的一切，不就是为了追逐，为了让他能笑着对我说，多亏了你, 我才能来到这片未曾踏足的领域？\n没错，他与我确实是不可能的，但是他却让我的生活拥有了动力与目标。\n我不想喜欢_了。\n原因只有一个。\n我已经爱上_了。',
    '有一天我喝醉了大声喊:“我要嫁给_！”这时我老公皱了皱眉，温柔的给我盖好被子，然后亲了我一口又凑到我耳边说“嫁给我一次了，还想嫁给我第二次？',
    '_！我命运般的阿芙洛狄忒，塞纳河畔的春水不及你，保加利亚的玫瑰不及你。你是神灵般的馈赠，你是上帝赐予我拯救我，使我的灵魂受到洗礼与升华。你是我黯淡升华中一束光亮，是你照亮了我黑暗的生命，你为我黑白的世界填满色彩，使我得到新生。看到你，我如临仙境，在厄瓜多尔荡秋千，在夏威夷岛冲浪，在清迈放飞天灯，在希腊梅丽萨尼洞泛舟穿梭，在土耳其卡帕多西亚空中漫步。你的一瞥一笑在我心头舞蹈，我全部的心跳都随你跳。我飞奔，我猛跑，我高举手臂，我欢呼雀跃，我在5号21楼的阳台跳起探戈。太美了，你是神，我被美到泪流不止，喷涌而出。我的眼泪从眼眶里高压喷射出来打穿屏幕，飞过珠穆朗玛峰，飞过东非大裂谷，飞出太阳系遨游九天；汇成亚马逊河，汇成银海星汉，在我热烈滚热的心头成云成雾，倾斜而下，席卷四方！',
    '_好帅🥵帅到我想给他买套房，但是由于经济原因，我决定先买套再买房🥵🥵🥵🥵🥵',
    '我得了相思病，医生给我开的药方：麝香0.05g、榔头香10g、速香3g、云头香0.3g、海狸香1g、伽香5g、龙涎香0.3g、红木香6g、灵猫香0.5g、地蜡香6g、飞沉香3g、通血香1g、香根鸢尾5g、_一位',
    '今天跟朋友去吃饭 点了一条鱼\n朋友问我为啥只吃鱼头\n我说因为鱼身要留着和_一起过',
    
    #  发病文学合集6.0@弦卷心菜投手 https://www.bilibili.com/read/cv17817365
    '_，虽然晚了些但端午还是要有仪式感，粽叶、糯米、蜜枣都准备好了，还剩一样东西就交给你了，你准备好艾草吧',
    '和_做顶流，我顶他流',
    '_，我真的好爱你😍。可是我不敢说😭😭。无数个清晨，似是被什么遥远的呼唤打动，双眸定睛后，闪烁起异彩🤩。大概是有所领悟，出门，打开信箱，拿到信纸便逃也似地跑进房间🤤。小心地将那久别的寄信人名称纳入眼底，随之而来的，不可抑制一般的喜悦感几乎是震撼了自己。不禁有些恐慌，继而无端的恐慌转变成了更深邃的失望😢。我对自己还对这样一份残存的感情抱有期待而感到悲哀，为自己这样轻易地发生心境变化而懊恼。下一个瞬间几乎是想要杀死自己😭😭。再转一瞬竟衍生出了同情心，然后阖上双眼，想要忘却什么似的再度入眠。醒后，打开手机，动态中没有你的踪迹，手里被汗水儒湿的信封上写的也不是你😭😭😭😭。这个秋天，没有邀请函，也没有你。我狼狈地把信塞回信箱。趁着周遭无人。可是我不敢说😢。_，我真的好爱你。😭😭😭😭😭😭',
    '所以说，我觉得“笑容”是人类最难看的表情，你看，笑容需要牵动的脸部肌肉实在是太多了，整张脸被神经扯动，再娇俏的脸都变得如同酒后发病，难看至极\n但从文献中我看到了各路诗人对“笑容”的赞美，白居说“回眸一笑百媚生，六宫粉黛无颜色”，苏轼说“美人微笑转星眸，月花羞，捧金瓯”\n老实说，我理解不了，我在生活里从未对这个表情有如此夸张的反应，实际上就连那“咯咯咯”的笑声，也令我十分心烦意乱。对，或许我是讨厌“笑”这个概念本身\n但我总是对理解不了的事物充满探索欲，我便开始探求这其中令这些诗人沉迷的地方。既然从现实无法探求，我便随作品出发好了\n一路上，我看过了蒙娜丽莎，酒神巴克斯，犹太新娘，一笑倾城。不，它们都无法诉说我想要的“美”，我迷惑了，我的旅途还未抵达终点，却已宣告终止\n我跌跌撞撞回到家中，打开B站，食指似卡壳的机械般滑动着界面，手机的微光打湿了我的眼睛。我不甘心，我又一次失去了探求美的资格，正在我泣不成声时，这个视频就出现在了我的B站首页\n我仿佛听到了命运之钟的摇摆声，咔嚓咔嚓，一切因果于此时收束，一切缘由在此刻得以揭晓，旅行的旗帜被重新纺织\n这个男孩，他便是因，是果，是我旅途的最终答案\n_的笑容，就是我的答案\n若是此时李白，苏轼，达芬奇等人与我把酒言欢，谈及他们对“笑容”的赞美，现在的我或许可以认可了\n但是，或许我也会起一些没有缘由的攀比之心，“或许你们几位大诗人大画家应该见一见我的可爱的_”',
    '今天我们物理开始讲磁力了，物理老师说钢、铁、镍一类的东西都能被磁化，我听完就悟了，大彻大悟。\n课后我问老师：“老师，是不是钢和镍都可以被磁化？”\n老师笑了笑，说：“是的。怎么了？”\n我赶忙追问：“那我对_的爱是不是也可以被磁化？\n老师疑惑了，问为什么？\n我笑着，红了眼眶：“因为我对_的爱就像钢铁打造的拖拉机一样，轰轰烈烈哐哐锵锵。”',
    '我居然和_是邻居啊啊啊啊啊啊啊 昨天回家在一户门外看到一串钥匙忘记拔了，我想应该是这家主人不小心忘记了吧，于是我就去敲门提醒一下。\n门一开我听声音就懵了，我问：是_吗?\n我说了事情的原委，还告诉他自己是他的邻居和粉丝，然后他竟然邀请我到家里坐！_真的，比我想象的要可爱！性格也很温柔，吃完饭坐在客厅里聊天 他说我俩可以结个婚啊啊啊啊啊啊啊啊啊啊啊啊啊啊\n真的太开心了',
    '我有时候确实觉得很烦，就连我的亲友都觉得我脾气有点暴躁了，却只是因为几件小事，比如自己的书掉在地上，糖不够吃了，晚上突然觉得想喝奶茶却喝不到，我都会大发一通脾气。但_从身后抱住我，说我这是婚前焦虑症，还亲了亲我的嘴角，我就觉得什么都美好了😭😭🌹🌹',
    '_！请问你是怎么穿过皮肤和黏膜的阻隔 在分泌物中的溶菌酶和巨噬细胞的吞噬中存活 还躲过浆细胞分泌的抗体或者致敏T细胞分泌的淋巴因子 住进我心里的 ？',
    '今天是我在电焊厂上班的第九十九天，这里实在是太闷太热了，我走了出来，在树下抽了一支烟。我想，虽然不知道你在干什么，但我一直在想你，有了你，这生活总算是有盼头了一些。_，我不想在电焊厂上班了，因为我电不到你，也焊不牢你的心',
    '_，俺是农村嘞，村里人都说俺精细，以前感觉没钱配不上你。俺可稀罕你，就给那风儿，吹过俺家地头。地里老红薯都知道俺喜欢你。真嘞！恁看见喽给俺回个话，谁欺负你我给他拼命！俺可喜欢你，嫁给俺吧。中不中？',
    '_!（怒吼）（变成猴子）（飞进原始森林）（荡树藤）（创飞路过吃香蕉的猴子）（怒吼）（变成猴子）（飞进原始森林）（荡树藤）（创飞路过吃香蕉的猴子）（怒吼）（变成猴子）（飞进原始森林）（荡树藤）',
    '今天学校跑步，快到终点时我一个冲刺超过了_，登成绩时，老师问“谁是第9名”我没反应过来，结果老师生气了，他就拿着表吼道“谁超了_自己不知道吗？”我便大声回道“我超了_！老师！我超了_！！！”',
    '_对社会影响很不好。刚刚我在外面看了看_的照片，裤子直接就炸了！旁边的人笑我，我很羞涩，并把手机放在了桌子上，那个人也看到了，他更离谱！他的裤子直接甩掉他跑出去了！边跑还边喊着它要上太空！然后又有人开始笑他，然后他不服气，抓起我的手机就朝那些人扔了过去，凡是手机飞过的地方裤子都炸了，过了一会儿，满地都是裤子和裤子残渣',
    '20岁就拥有了_这样的老公，我能像今天这么成功，首先我要感谢我的父母，要不是他们给了我这张嘴，我就不会告诉大家',
    '本人不懂二次元，对于你们这种痴迷于虚拟角色的行为，我很是不理解，我感觉应该分清现实和虚拟，他们好看归好看，但终究不是真实存在的，我们要活在现实，而不是盯着纸片人，我的生活很充实，今天是我和_的婚礼，大家记得带点彩礼',
    '？登一下我女朋友的号，我是这个账号的男朋友，非账号主人。只是来看看她平时看的东西到底什么魔力可以让我的女孩睡觉都在笑，没想到居然会是这种类型的视频。她整天魂不守舍的，就是在嚷着等你出新视频。我好心劝告你，会做东西就多做一点，不要让我女朋友老是在等你出新视频，不满意的话欢迎来找我_，我随时奉陪。',
    '2005年出生于地球\n2010年就读于美哈佛大学\n2011年加入海豹击突击队\n2012年前往南极实地考察成果颇丰\n2016年被提名可以改变世界的人\n2022年放弃一生荣誉 求做_的狗',
    '见到_后身体感觉很糟糕，是从左心室开始,新鲜的动脉血液从左心室经体动脉被压出，经过全身组织与组织各处完成氧气与二氧化碳的交换后有动脉血变为静脉血，经由下腔静脉回到右心房，再进入右心房，通过肺动脉进入进入肺部的循环，将静脉血转化成动脉血，再由肺静脉进入左心房，最后进入左心室.之后血液由右心室射出经肺动脉流到肺毛细血管，在此与肺泡气进行气体交换，吸收氧并排出二氧化碳，静脉血变为动脉血；然后经肺静脉流回左心房的感觉',
    '呃😓，以前没接触过二次元，看你们对这些个角色这么入脑，真的很幼稚。我觉得人应该把重心放在现实生活中，比如我明天要和我的未婚夫_结婚了',

    #  发病文学合集7.0@弦卷心菜投手 https://www.bilibili.com/read/cv17817365
    '大家都填好志愿了吗？我的第一志愿是北大，但是我感觉我的分数可能不够，清华的话，可以冲一冲，最后一个保底的我选了_的床，这个我应该是稳上的。',
    '我要把裤子放冰箱，从此变成冷裤的人\n我要把裤子剪碎，从此变成残裤的人\n我要把裤子炫了，从此变成炫裤的人\n我要把裤子丢掉，从此变成_的人👉👈',
    '_问我：“你有多爱我？”\n我说：“大概有300克。\n_笑了，说“这好老套，这个我知道，你想说300克代表的是心脏的重量对不对？“\n我也笑了，_这个小笨蛋，她不知道，300克其实是我一天对着她冲出来的量',
    '今天路过一家奶茶店，看见一个叫_的小孩子吸管半天没插进去\n我这强迫症当场就犯了，直接上前大吼：“让我来帮你插”',
    '_，你对我有多重要，就好像你是我糖酵解时得己糖激酶、6-磷酸果糖激酶-1、丙酮酸激酶，是我三羧酸循时的柠檬酸合酶、异柠檬酸脱氢酶、α-酮戊二酸脱氢酶，是我生命中每分每秒每个生化反应里不可缺少的关键酶',
    '非高考生，所以躲过了语文的妙手本手，数学的摧花辣手，英语的不留一手，政史地的痛下杀手，却还是没躲过_的遥遥招手',
    '隔壁来了个叫_的人，上午工作的时候吵我，我很生气，于是在晚上的时候吵他，他被我吵的受不了，哭着喊不要了，求我不要吵他了，但是我就是不停，一直吵一直吵，吵死他',
    '_，我们私奔吧。\n去充满橘子味的农庄\n去喝着麦香味啤酒看百年前古堡的始落\n去带着草帽走在飘满麦穗的小路上\n喝着一杯鸡尾酒看阳光撒在绿色的树叶上映衬这翠蓝的湖水\n深陷柔软的沙发里拥抱，和着窗外被大风摧残的树枝亲吻\n踩着金黄色的树叶没有章法地随意舞蹈\n开着车大声歌唱，这一刻你和风都在我身旁❤。',
    '穿这身衣服不会变得怪怪的，但我会让_变得怪怪的',
    '上次身体不舒服去医院看病，医生说缺维生素e，那我问医院这有没有_？医生疑惑的问：“为什么”我回答：“因为_是我的维e”',
    '一直对ip地址很不满意，为什么我的ip地址不是_的心',
    '和_一起睡真的舒服，真的太太太凉快啦，女生好像都比男生身体要凉快许多，我比较怕热，每次我都会抱着她凉快，然后她会一直搂着我。\n还有就是_睡觉其实睡的很死，她一直都是抱着我睡，只要我翻个身或者轻轻叫她，她马上就会醒来然后紧紧抱住我说“ 怎么了”\n每一次睡醒之后，_喜欢赖床 ，她就会抱着我然后把头伸过来在我胸口上撒娇，早上起来那种奶声奶气地说“我好想一直这样抱着你”\n和_一起睡真的好甜～枕头都变得更软 空气也变得好软 ，就连做的梦也是好柔软🤤🤤🤤🤤_大人我爱你❤️❤️❤️❤️',
    '切，不就是_吗？每天睡在我床上，我早就看腻了，我压根不……喜……呜呜呜呜，我说不出口，我真的很喜欢_，我逛街的时候在想_，我走路的时候在想_，我睡觉的时候也在想_，我做梦的时候在想_，就连呼吸的时候我都在想着_，每分每秒，无时无刻，我的生命已经不能没有了，看不见你的任何时候我都在痛苦，我的_，我的_，呜呜呜，我爱你呀，我爱你！🤤🤤🤤🤤🤤',
    '网上看到一种说法，说日本人看到烟花就会想起夏天，夏日和烟花大会，夏季和服还有小金鱼；而中国人看到烟花就会感到寒风灌进鼻腔，想起热腾腾的饭菜和排骨汤——该过年了。我觉得他说的很有道理。我还记得小时候玩烟花，都是穿着厚厚的棉袄。这也是中国人民的传统智慧——穿着厚衣服，可以玩烟花对射，被打到也不疼，就是容易把新衣服烧个窟窿，然后回家挨揍。我第一次见到_的时候——尽管当时我戴着耳机，而且刚过四月——我却分明听到了烟花在耳边炸开，然后再噼里啪啦地落到地面，我甚至能感受到火星子刺伤了我的眼睛。喜欢_的感觉呢，就像是眼睁睁看着烟花朝自己飞过来。我自以为冲浪多年，早就给自己套了几层棉袄，已经刀枪不入了，可等我反应过来，我的心已经被她烧了一个大窟窿，怎么也填不满了。说来也好笑，明明就是她烧穿了我的棉袄，我却还想跑到她面前，指着那个大窟窿对她炫耀:“看，我有这么喜欢你！”',
    '我被外星人绑了，他们说要研究我的心，我害怕极了，担心我那些烂熟于心的知识暴露给了他们太多地球人的文明，结果没多久他们就把我放了，原因是他们研究来研究去，就在我心里发现了一一个名字:_',
    '我前段时间为了提升自己的文化素养，给自己报了个书法培训班。因为跟我同期的都是小学生所以大家就有点排挤我，看不上我这么大年纪还在学这个。本来也没什么，但小学生的恶意真的超乎我的想象，他们说我老头子半只脚进棺材还来学书法，我听到都气哭了。我擦干眼眼泪不管他们继续练字，我发誓我一定要练出一笔好字，不能让钱白花。我凝神静气，在纸上认真写出了一行字：_，我要做你的狗🥵🥵',
    '致未来的宝贝女儿：\n等你上幼儿园头发留长我就给你烫内扣，给你剪齐刘海，给你买漂亮的头花，从小学开始我就给你买帆布鞋，漂亮的牛仔裤和卫衣，每天把你打扮的漂漂亮亮的，每天和你爸爸开着车在学校门口等着你放学，把你抱进车里在额头上给你一个亲吻，带你去吃德克士还有哈根达斯，等你上了初中，给你买最漂亮的NB和vans匡威，给你买最合身的哈伦裤和怪兽背包，给你剪最美的齐刘海， 烫最好看的梨花头，买你最喜欢的零食，我会让你去学习你喜欢的事情，不会逼你去学习，舞蹈，音乐还有书法，不会逼你去上补习班，你每天开心就好， 回家你能告诉我你喜欢哪个可爱的男生，有哪个帅气的男生追你，你可以成绩不好，但你一定要善良，你喜欢什么东西要告诉我，我会尽全力去给你买，你不可以太傲娇，你要学会谦虚和忍让，我不反对你早恋，但是，你要快乐。等你十八岁时，我就送你第一双高跟鞋当做你的成人礼，我要你当我一辈子的公主，我要让我从小没有经历过的幸福都经历在你身上，我和你的傻瓜爸爸都正在路上，你要耐心地等着，等着我们一起回家。未来的女儿你一定很好看，因为你爹是_',
    '看大家都在说_的腰好细，给大家科普一下，这种腰叫孩腰，顾名思义，腰跟小孩子的腰一样细。如果不及时进行治疗，将会越来越细，挤压到心脏。有国外的著名医生说过：孩腰多远才能进入你的心🤤🤤',
    '_老婆贴贴！！！！！！（健康且适度的尖叫）（健康且适度的爬行）（健康且适度的扭曲）（健康且适度的爬行）（健康的爬）（矜持且健康地流口水）（健康的爬）（健康且搞笑的流口水）（健康的爬）（绿色且保守的流口水）（健康的爬）（优雅且健康的流口水）（健康的爬）（美丽且健康的流口水）',
    '我以前最喜欢写文章了，最近太忙了没怎么写。_没有更新可能因为之前_抄的都是我🥵🥵',
]

if __name__ == '__main__':
    print(get_illness('_'))
