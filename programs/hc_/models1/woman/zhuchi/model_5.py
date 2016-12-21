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

model_5 = [
    {
      "model":"%(nl)s年的风风雨雨，%(nl)s年的生命历程，老人家阅尽人间沧桑。她含辛茹苦把子女们抚养成人、成才，成家立业，现如今家家和睦，平平安安。她一生中积累的最大财富是他那勤劳善良的朴素品格，她那宽厚待人的处世之道，她那严爱有加的朴实家风。这一切，伴随他经历了坎坷的岁月，更伴随他迎来了晚年生活的幸福，让我们为老人家送上最真诚、最温馨的祝福，共同祝愿她老人家福如东海、寿比南山、健康如意、福乐绵绵、笑口常开、益寿延年。"
    },
    {
      "model":"春华秋实，花开并蒂。鲜花的盛开孕育着丰硕的果实，老人家%(nl)s年的风雨历程，阅尽人间沧桑，品足生活酸甜，结下了累累硕果，积累了可贵的财富，那就是她勤劳善良朴素的精神品格！让我们向老人家敬献寿果，感谢她为子孙后辈们创造了宝贵的精神财富和难能的物质利益，同时祝福老人家福如东海，寿比南山！"
    },
    {
      "model":"%(nl)s年风风雨雨，%(nl)s载生活苍桑。岁月的泪痕消消地爬上了她的额头，将老人家的双鬓染成白霜。大千世界里，孩子们把心中的话语都洒向老人那宽厚慈爱的胸膛。“严于律己，宽以待人，认真工作，发奋图强”简单的话语，让儿女镌刻在心，永记不忘。老人的辛苦并没有白费，在她的教育下，子女们都已经长大成人，为老人赢得了无尚的荣光。现如今老寿星一家是五世同堂，正可为儿子孝，儿媳能，女儿贤，女婿强，成绩优异，捷报平传，后继有人。"
    },
    {
      "model":"我们的%(zbxm)s%(bf)s一贯积善行德，关心帮助马氏宗亲族人，孝敬尊长，教育子侄，主持公道；她助人为乐，%(bf)s所做的一切，她的一言一行，为我们晚辈树立了良好的榜样，是后辈的楷模。虽然她们不是豪门显贵，尽管她们是劳苦的一生，但她们的一生却是创业的一生、奋斗的一生。她们是平凡的、朴素的，但在我们的心目中却永远是神圣的、伟大的！"
    },
    {
      "model":"%(bf)s是位知足常乐的人，更是一个自得其乐的人，也富有幽默感。%(bf)s的一言一行，为我们晚辈树立了良好的学习榜样，她是儿女们的好母亲，是儿媳们的好婆婆。我们很爱%(bf)s，%(bf)s是一位伟大的母亲，又是一位伟大的%(bf)s。 %(nl)s年风风雨雨，%(nl)s载生活苍桑。岁月的泪痕爬上了%(bf)s的额头，将老人家的双鬓染成白霜。%(bf)s阅尽人间沧桑，%(bf)s一生中积累的最大财富是她那勤劳正直的朴素品格，%(bf)s那宽厚待人的处世之道，%(bf)s那严爱有加的朴实家风。这一切，伴随%(bf)s经历的坎坷岁月，更伴随%(bf)s迎来了今天晚年生活的幸福。"
    },
    {
      "model":"%(nl)s年来，%(bf)s长期勤于公事，为兴家业，起早贪黑，披星戴月，精打细算。在家境极度困难的情况下，承担起了家庭生活的重担，为扶养我们兄妹成人，呕心沥血，不辞劳苦，用超过常人的艰辛养育了他的儿女，用严爱供养儿女们读书成人，奠定了儿女们人生的起点，用永不气馁的鼓励和高标准的要求激励儿女们开拓事业，造就了幸福今天。堪称恩德惠恩，功德无量！虽然您不曾是高官显贵、名流宿儒，但在儿女的心中您永远是神圣的、伟大的！！水有源，树有根，儿女不忘养育恩。在这里，请允许我代表我们晚辈们——您的后代子孙，对母亲真诚的说一声：您辛苦了！您对我们的养育之恩，我们将永世不忘！ 君颂南山是说南山春不老，我倾北海希如北海量尤深。乐享晚年漫道世间难逢百岁；宜登上寿且看堂上再过十年。还是让我们献上最衷心的祝愿，祝福我们的%(bf)s生活之树常绿，生命之水长流，寿诞快乐，春辉永绽！愿今天光临的各位亲朋好友人人都能在这里感悟到寿星的灵气，都能沾到寿星的圣光，从而得以能够家家家庭幸福，个个事业有成。让我们共同举杯畅饮长寿酒，喜进长乐餐！"
    },
    {
      "model":"%(nl)s载风雨沧桑、含辛茹苦，岁月的泪痕悄悄地爬上了老寿星的额头，将寿星双鬓染成白霜。老人家严格要求自己凡事都要做得最好，在多个工作岗位上，都成绩卓著，深受领导和群众欢迎，荣得社会极高的评价。在家庭方面，艰苦朴素、勤俭治家，对待双方老人孝敬有加，教育子女以身作则，如今四子三女都已长大成人，家庭和睦幸福，如今已是四世同堂，正是有老人家的谆谆教诲，这个四世家庭和睦相处，幸福温馨。对待亲友，宽厚待人，悉心帮助，深受尊重。堪称：老人的孝子、子女的慈母、亲朋的挚友、社会的良民。"
    },
    {
      "model":"%(nl)s年的风风雨雨、%(nl)s年的沧海桑田，老人家能走过%(nl)s年的人生路程，不知经历了多少的艰辛和坎坷，换来了今天儿孙满堂的天伦之乐。我们从内心感到由衷的欣慰和喜悦！ 她那勤劳善良的人生品格、宽厚待人的处世之道、严爱有加的朴实家风，时时刻刻都在关心和激励着几代人的成长。现在，她的几代人都围绕在她的身旁，感受着爱和幸福的真谛。 让我们向老寿星献上最衷心的祝愿，祝福%(zbxm)s老人“寿至祥来映日月，东海南山祝长寿，待到到百岁日, 满堂重聚把酒欢。”"
    },
    {
      "model":"%(nl)s年风风雨雨，%(nl)s年生活沧桑，岁月的痕迹悄悄地爬上了她的额头，将老人家的双鬓染成白霜。在老人所走过的%(nl)s个岁月中，她把孝心献给了父母，把真情捧给了邻里，把责任心交给了事业，把爱心给了孩子。 先生尊崇孝道，在生活上竭尽全力让老人吃好穿暖，在精神上尽其所能替老人分忧解愁，使父母亲颐养天年。对邻里好比自己父兄姐妹，用待亲人般的爱去待乡邻，备受邻里盛赞。在劳动中严于律已，宽以待人，以高度的责任心和使命感，对待她所从事的职业。"
    },
    {
      "model":"我代表所有的晚辈、%(nl)s年的风风雨雨，%(nl)s载生活沧桑，岁月的泪痕爬上了%(bf)s的额头，将老人家的双鬓染成白霜。%(bf)s阅尽人间沧桑，%(bf)s一生中积累的最大财富是她勤劳正直的朴素品格，%(bf)s那宽厚待人的处世之道；%(bf)s那严爱有加的朴素家风。这一切伴随%(bf)s经历的坎坷岁月、更伴随%(bf)s迎来了今天晚年生活的幸福。嘉宾旨酒、笑指青山来献寿。百岁平安，人共梅花老岁寒。今天高朋满座、让这里暖意融融；让我们一起恭祝%(zbxm)s%(bf)s增寿富贵、添光添彩添吉祥、福如东海；祝福%(zbxm)s%(bf)s生活之树常青、生命之水长流、寿诞快乐、春辉永绽，同时祝愿在场的每一位来宾都幸福安康。最后祝各位来宾家人万事如意、心想事成！"
    },
  ]