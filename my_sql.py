import sqlite3
import datetime


def show_all():
    # connect data base
    variable1 = sqlite3.connect('members.db')

    # create a cursor
    variable3 = variable1.cursor()

    variable3.execute("SELECT * FROM members_v2")
    items = variable3.fetchall()
    # print(type(items))
    i = 1
    for item in items:
        print(i, item[0], item[1], item[2])
        i += 1
    # commit our command
    variable1.commit()
    # close our connection
    variable1.close()


def add(first_name, my_mail, my_password):
    # current time
    now = datetime.datetime.now()
    time = now.strftime("%y-%m-%d %H:%M:%S")

    # connect data base
    variable1 = sqlite3.connect('members.db')
    my_list = [first_name, my_mail, my_password, time]
    # create a cursor
    variable3 = variable1.cursor()
    variable3.execute("INSERT INTO members_v2 VALUES (?,?,?,?)", my_list)

    # commit our command
    variable1.commit()
    # close our connection
    variable1.close()


def add_many(my_list):
    # connect data base
    variable1 = sqlite3.connect('members.db')

    # create a cursor
    variable3 = variable1.cursor()
    variable3.executemany("INSERT INTO members_v2 VALUES (?,?,?,?)", my_list)

    # commit our command
    variable1.commit()
    # close our connection
    variable1.close()


def search_list(email, password):
    # connect data base
    variable1 = sqlite3.connect('members.db')

    # create a cursor
    variable3 = variable1.cursor()
    my_bool = bool
    variable3.execute("SELECT * FROM members_v2")
    items = variable3.fetchall()

    for item in items:
        if item[1] == email and item[2] == password:
            my_bool = True
            return my_bool
        else:
            my_bool = False
            return my_bool

    # commit our command
    variable1.commit()
    # close our connection
    variable1.close()


def all_data():
    # connect data base
    variable1 = sqlite3.connect('members.db')

    # create a cursor
    variable3 = variable1.cursor()
    variable3.execute("SELECT rowid, * FROM members_v2")

    my_list = variable3.fetchall()
    # commit our command
    variable1.commit()
    # close our connection
    variable1.close()
    return my_list
