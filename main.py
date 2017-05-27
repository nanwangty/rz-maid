welcome = '''
您好,欢迎使用任眞小管家!
-*-*-*-*-*-*-*-*-*-*-*-
1.录入
2.查找
3.更改
4.删除
5.设置
'''
print(welcome)
choose = int(input('请输入您的选择:'))

def main(choose):
    if choose == 1:
        import 录入函数
        录入函数.luru()
    elif choose == 2:
        import sqlite_read_save
        for i in sqlite_read_save.search():
            print(i)
    elif choose == 3:
        pass
    elif choose == 5:
        pass
    else:
        print('Error')

main(choose)