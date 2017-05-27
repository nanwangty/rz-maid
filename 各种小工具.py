# 这里面是关于本软件的各种小软件 方便开发时使用,也准备里后放在设置里!
# 本类工具应该有密码 只有密码对的人才能使用 不然危险
import pickle
import sqlite3

def pkl_choose_list():
    '''
    # sex-->list[0] ,quarter-->list[1], genre-->list[2], colour-->list[3]
    这个工具用来把一些选择的内容腌制起来方便各个模块读取
    如果以后有需要更改选择内容例如颜色类别 就可以在这里更改
    :return:
    '''
    list = [['女', '男'], ['夏', '春秋', '冬'], ['外套', '裤子', '裙子', '冬外套', '保暖', '内衣', '袜子'],
            ['红', '黄', '绿', '青', '蓝', '紫', '白', '黑', '灰', '褐', '棕']]
    with open('list.pkl', 'wb') as f:
        pickle.dump(list, f)

def set_genre_colour():
    '''
    这个函数用来增加或删除颜色或类别选项,也就是更该腌制起来的内容
    :return:
    '''
    with open('list.pkl', 'rb')as f:
        list = pickle.load(f)

    def set_genre():  # 设置类别(增加,删除)
        print('现有类别为:', list[2])
        pass

    def set_colour():  # 设置颜色(增加,删除)
        print('现有颜色为:')
        pass


def js_to_0():
    '''
    用来给物品编码的计数器归0工具
    :return:
    '''
    with open('jishu.pkl', 'wb')as f:
        pickle.dump(0, f)
    with open('jishu.pkl', 'rb')as z:
        if  pickle.load(z) == 0:
            print('计数器已归零!')
        else:
            print('出错,请检查!')

def db_to_0():
    '''
    数据库初始化工具,清空数据库内所有内容
    :return:
    '''
    conn = sqlite3.connect('test.db')
    conn.execute('delete from database ')
    conn.commit()
    conn.close()
    print('数据库已清空!')
    # jieguo = conn.execute('select * from database')
    # for i in jieguo:
    #     print(i)
db_to_0()
js_to_0()