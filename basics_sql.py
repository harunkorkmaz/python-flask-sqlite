import sqlite3
import datetime

now = datetime.datetime.now()
print(now.strftime("%y-%m-%d %H:%M:%S"))
time = now.strftime("%y-%m-%d %H:%M:%S")
# connect to data base
dat = sqlite3.connect('members.db')
# create a cursor
data = dat.cursor()
# create a table for once then no need
# data.execute(""" CREATE TABLE members_v2(
#        name text,
#        email text,
#        password text,
#        date text
#        )
#    """)

me = [('kevser', 'kevser@gmail.com', '123456', now.strftime("%y-%m-%d %H:%M:%S"))]
# data.execute("INSERT INTO members VALUES('harun','korkmaz','asdasda',(?))",time)
#data.executemany("INSERT INTO members_v2 VALUES(?,?,?,?)", me)
data.execute("SELECT rowid, * FROM members_v2")
my_list = data.fetchall()

i = 1
for item in my_list:
    print(item)

dat.commit()
data.close()
