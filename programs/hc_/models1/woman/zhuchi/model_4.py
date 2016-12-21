#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
__author__ = 'top'
date = '16/11/8'
我爱学习,学习使我快乐
'''
'''
长辈辈分	%(bf)s
年龄	%(nl)s
姓名	%(xm)s
举办地址	%(jbdz)s
//家庭住址	%(jtzz)s
晚辈辈分	%(fyrbf)s
//其他祝寿人姓名	%(qtxm)s
长辈名字	%(zbxm)s
季节	%(jj)s
'''

model_4 = [
    {
      "model":"身为主持人我谨代表子女敬祝母亲健康如意，福乐绵长，春秋不老，耄耋重新。向光临寿筵现场的各方宾朋致以衷心的感谢和崇高的敬意。天底下最伟大最无私最崇高最温暖最实惠最感人的爱是天下的母亲开发缔造的！这位母亲同样具备了这样神圣而平凡的素质和品质！老人家思想开明、豁达大度、宽容忍让、和睦邻里、勤劳节俭、尊老爱幼，在最艰难的岁月里维护着我们家庭的团聚，在困苦的环境中完成了赡养长辈哺育儿女的重任。她的一言一行感化着后人，激励着大家，为家庭支撑起一片生活的蓝天，为儿女们铺建起幸福健康的道路。我们对她有报不完的恩、叙不断的情。%(nl)s高龄的母亲仍呵护着女儿女婿，关注着孙儿辈的健康成长！母亲晚年注重保健、不辍劳作、年高不忘奉献余热、播撒爱心，这样的美德是我们后人最好的精神财富！也是我们赖以自豪和骄傲的传家之本！我们由此坚信老人家今后的日子会更加幸福、安康、快乐！ 这次生日庆宴，是在我们儿孙们一再要求下才举办的。老人家再三要求我们不张扬、不奢侈、不给亲朋添麻烦，但我们想到大家庭现在的幸福祥和，看到第三代人的成长进步、目睹第四代的天真活泼。想借母亲诞辰这个契机，来回顾母亲美德，弘扬长辈风范，增进邻里友谊，再叙亲朋情爱，同时共享老人家在时间年轮上的重大收获，反复酝酿终于决心诚邀今天的亲朋至交光临！"
    },
    {
      "model":"我谨代表全家人向亲爱的母亲祝寿。祝您福如东海，日月昌明，松鹤长春，春秋不老，古稀重新，欢乐远长。 天底下最伟大最无私、最崇高、最温暖、最感人的爱就是母爱！我的母亲同样具备了这样神圣而平凡的素质和品质！您思想开明、豁达大度、宽容忍让、和睦邻里、勤劳节俭、尊老爱幼，在最艰难的岁月里维护着我们家庭的团聚，在困苦的环境中完成了赡养长辈哺育儿女的重任。您的一言一行感化着后人，激励着大家，为家庭支撑起一片生活的蓝天，为儿女们铺建起幸福健康的道路。 %(nl)s年风风雨雨，%(nl)s载生活沧桑，满头的白发见证您的操劳和艰辛。如今我们都长大成人，为人父母，我们深深的懂得了父母的不易和伟大。"
    },
    {
      "model":"在这非常激动的时刻，我代表%(bf)s的子女，想到了我们全天下的所有母亲，她们在最艰难困苦的年代，把自己的儿女养大，成人成家，经历了比我们这代人数倍的辛苦和磨难，付出了比我们这代人数倍的心血和汗水，我无法想象她们是怎样挺过来的，他们对儿女的爱是那样的无私，为儿女的付出的精神是那样的伟大，她们的母爱之心比大地更深厚，比太阳更灿烂比宇宙更无限是做儿女的无论无何都无法完全彻底解读透，为此我向与老寿星年龄相近的所有母亲以及中国所有的老母亲深深地鞠躬！"
    },
    {
      "model":"人生就像一条奔流不息的江河，流淌中记录着流逝的岁月，象征着您走过的平凡而又伟大的日子。虽然，您只是一个普通的女性，但您是一位伟大而不平凡的母亲，我们的好妈妈！您孕育了我们四个儿女，您给了我们生命，您把您的青春年华无私地奉献给了我们；为了我们健康茁壮地成长，您含辛茹苦，每日辛劳，您不仅给了我们健康的身体，还给了我们健康的心理和生活的能力，更重要的是我们承接了您的智慧，使我们能够阳光地面对生活，勇敢地面对人生的种种挑战和际遇。至今，我们都清晰地记得您为我们所做的每一件小事和每一次无私的帮助，记得您的每一次体贴和关怀。每当想到这些，我们都万分感动，都觉得无论怎样孝顺您，都无法报答您的养育之恩！我们每时每刻都在记挂着您，惦念着您。无论走到哪里，无论是否每天都能看到您，我们的心永远和您在一起。我们怀着感恩的心情，会尽我们之所能报答您的养育之恩。"
    },
    {
      "model":"在这里，我们代表老寿星的子女祝您福寿安康，万寿无疆！我们在场的每一位都有自己可敬的母亲，妈妈，您老人家寒心茹苦地扶养我们长大成人，您以那亲切地教诲，深爱的目光照耀着我们的哭，我们的笑，愿雨屋檐降。于大千世界里，孩子们把心酸与痛苦都洒向妈妈您那饱经风霜，宽厚慈爱的胸怀。妈妈的苦，妈妈的累，妈妈的情妈妈的爱，我们将终身难以报答。尽管我们失去了很多很多，但我们拥有人世间最保贵的，那就是妈妈您的爱！妈妈，让我代表我们姐弟，向您鞠躬了。"
    },
    {
      "model":"我代表老寿星的女子相对大家说，天底下最伟大、最无私、最崇高、最温暖、最实惠、最感人的爱是母亲的爱！如果说父爱是巍峨挺拔的山，那么母爱就是深沉宽阔的海。母亲思想开明、豁达大度、宽容忍让、和睦邻里、勤劳节俭、善良朴实、尊老爱幼。我们对她老人家有报不完的恩、说不完的情。亲爱的妈妈，是您给了我们生命，是您培育我们长大，您用全部的心血塑造了我们的灵魂和身躯，您用全部的关爱指引了我们的理想和人生！ 这次生日庆宴，我们做儿女的，想借母亲诞辰这个机会，来回顾母亲的美德，弘扬母亲的风范，增进邻里的友谊，共享老人家在%(nl)s大寿上的最大快乐。"
    },
    {
      "model":"我代表老寿星的子女想对您说，%(nl)s年风风雨雨，%(nl)s载生活沧桑，满头的白发见证您的操劳和艰辛。如今我们都长大成人，为人父母，我们深深的懂得了父母的不易和伟大。妈妈，在您%(nl)s寿辰的今天，我们做儿女的，发自肺腑的向您说一声：“敬爱的妈妈，您辛苦了，没有您就没有咱们全家的今天！您是这个家庭的缔造者，是抚育我们成长的大恩人，是教诲我们成才的导师，是带领我们前进的舵手！您是我们的至亲、至尊！我们永远热爱您、孝敬您！您的健康就是我们最大的幸福，让您健康长寿是我们做子女的共同心愿，在今后的岁月里，我们一定 要让您过一个幸福，安康，开心，快乐的晚年。”"
    },
    {
      "model":"我代表老寿星的子女想说，没有母亲也就没有我们的今天，母亲的爱恩重如山，我们为有这样一位平凡而又伟大的母亲感到骄傲和自豪。母亲给与我们的不仅是无微不至的关爱，还有取之不尽、用之不竭的一笔精神财富，那就是他们的美德：善良、质朴、正直，吃苦耐劳，勤俭节约，他们双老的崇高品质值得我们用一生去学习。 敬老尊贤，兄友弟恭是中华民族的传统美德，我们有理由相信，在我们子女的共同努力下，我们的家业一定会蒸蒸日上，兴盛繁荣！我们的母亲、父亲一定会健康长寿，老有所养，老有所乐！"
    },
    {
      "model":"我代表老寿星的子女，想对您说，风风雨雨%(nl)s载，母亲历尽人间沧桑。正因为有您年轻时养育我们的艰辛，才换来了您今天的满堂儿孙，满堂孝心。我们感谢您给予了我们勤劳、善良、正直的品格；感谢您教会我们如何待人，如何接物，如何处事；感谢您宽厚待人的处世之道；感谢您给予这个家族厚道朴实的家风，这一切都将作为最宝贵的精神财富伴随您的儿孙走好以后的路。 曾经的您是辛苦的，现在的您，是幸福的。因为您不仅拥有至爱的亲朋好友、邻里乡亲，还有孝顺的儿子儿媳，体贴的女儿，能干的女婿，更有一群活泼可爱，聪明伶俐的小字辈。 为培养我们姊妹七人，母亲您含辛茹苦，勤俭持家，为儿女忘已，承受生活重担的磨难，全然是对儿女的无私奉献。正是您的坚强、勤俭和善良，培育了我们良好的思想品德和美好的心灵；正是您的质朴、真诚和乐观，教会了我们怎样做人做事。我们作儿女的永远不会忘记母亲的养育之恩和给我们的爱。"
    },
    {
      "model":"八十五年风著雨，八十五载苍桑泪。岁月的泪痕早已爬上了%(bf)s的额头，将老人家的头发染成了白霜。而今%(nl)s多岁的%(bf)s依然还在为她的儿女、孙子操心，为生活琐事烦心！我想代表老寿星的子女说一句，“养儿方知父母恩”，在现今我们儿女都有了一定的社会阅历，能进行理性思考的时候，我们才深深地感受，老大人给予我们的，不仅是生命和身体，还有热血心肝和铮铮铁骨；%(bf)s给予我们的不仅是物质财富，更多的是勤劳质朴、与人为善的精神动力，而这些才是一个人傲立于世的无价之宝，取之不尽、用之不竭的力量和财富源泉。常言道:饮水当思源，勿忘挖井人！一个人，只有心存感激地活在这个世界上，才能真正体会到生活的美好。如今子女们事业有成，生活幸福,这首先最要感谢的就是父母的哺育恩、感谢父母亲给我们晚辈打下的基础，父母的恩情我们将终生铭记!"
    },
  ]