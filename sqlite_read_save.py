import sqlite3

def read():  # 读取
    pass

def save(id,sex, quarter, genre, colour, buy_time, where, fade, describe):  # 存储
    conn = sqlite3.connect('test.db')
    conn_str = r"INSERT INTO database VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s');"%(id,sex, quarter, genre, colour, buy_time, where, fade, describe)
    conn.execute(conn_str)
    conn.commit()
    conn.close()

def search(搜索语句):  # 搜索
    conn = sqlite3.connect('test.db')
    conn_str = ('select * from database %s')%(搜索语句)
    return conn.execute(conn_str)


for i in search('where sex = "女"'):
    print(i)