#!/uxr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'L'

import pickle
import 计数器 as js
with open('list.pkl', 'rb')as f:
    list = pickle.load(f)
# sex-->list[0] ,quarter-->list[1], genre-->list[2], colour-->list[3]


def set_num(sex, quarter, genre, colour):
    if sex in list[0]:
         sex_num = list[0].index(sex)+1
    else:
        print('sex Error')

    if quarter in list[1]:
        quarter_num = list[1].index(quarter)
    else:
        print('quarter Error')

    if genre in list[2]:
         genre_num = list[2].index(genre)+10
    else:
        print('gener Error')

    if colour in list[3]:
         colour_num = list[3].index(colour)+10
    else:
        print('colour Error')

    num = str(sex_num)+str(quarter_num)+str(genre_num)+str(colour_num)+str(js.jishu())
    # 第一位为性别(0/1),第二位季节(0/1/2),第三四位类别(10-99),第五六位颜色(10-99),第七位后编码(0-无限)
    return num
    # 反回了一个字符串

# 缺少序列号(库里总共有多少东西+1就是号码)

