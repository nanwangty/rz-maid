import easygui as g
import datetime
import pickle
import 生成编码 as num
import sqlite_read_save

def luru():
    with open('list.pkl', 'rb')as f:
        list = pickle.load(f)

    sex = g.buttonbox(msg='选择性别', choices=list[0])
    quarter = g.buttonbox(msg='选择季节', choices=list[1])
    genre = g.buttonbox(msg='选择类别', choices=list[2])
    colour = g.buttonbox(msg='选择颜色', choices=list[3])
    more = g.multenterbox('请输入以下信息',fields=['购买时间:','购买地点:','是否掉色:','其它描述:'],values=[datetime.datetime.now().strftime('%Y-%m-%d'),'淘宝','否','Nothing'])

    id = num.set_num(sex,quarter,genre,colour)

    msg = '''
    物品编码:%s
    性别:%s
    季节:%s
    类别:%s
    颜色:%s
    购买时间:%s
    购买地点:%s
    是否掉色:%s
    其它描述:%s'''%(id, sex, quarter, genre, colour, more[0], more[1], more[2], more[3])

    text = g.indexbox(msg,'选择', ['存储', '修改', '取消'])

    if text == 0:
        sqlite_read_save.save(id, sex, quarter, genre, colour, more[0], more[1], more[2], more[3])

    if text == 1:
        textbox = g.multenterbox(msg='请修改:', fields=['物品编码', '性别', '季节', '类别', '颜色', '购买时间:', '购买地点:', '是否掉色:', '其它描述:'],values=[id, sex, quarter, genre, colour, more[0], more[1], more[2], more[3]])
        print(textbox)
    if text ==2:
        print('已取消')
    # 把得到的信息转换成一个类就行了呗?
    # 但是现在要把它们都在存进sqlite里
