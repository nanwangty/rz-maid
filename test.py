# import sqlite3
#
# conn = sqlite3.connect('test.db')
# str = "INSERT INTO database VALUES ('10101020','女','夏','外套','红','2017-05-26','淘宝','否','没有');"
# conn.execute(str)
# conn.commit()
# conn.close()
import sqlite3
import sqlite_read_save
conn = sqlite3.connect('test.db')
str = conn.execute('select * from database where %s = "%s"')%(项目,值)
for i in str:
    print(i)