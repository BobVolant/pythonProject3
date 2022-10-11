# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharádasdasdasdm')
import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root',passwd='long187977',database='mse')
mycur = mydb.cursor()
# mycur.execute('USE mse')
# mycur.execute('show databases')
# sqlne="INSERT INTO student VALUES('A908098','klfmLastName','klfmLastName','klfmLastName','klfmLastName','klfmLastName')"
# mycur.execute("INSERT INTO student VALUES('Asdf9080ss8','klfmLastName','klfmLastName','klfmLastName','klfmLastName','klfmLastName')")

# mycur.execute("SELECT * FROM student;")
# mycur.execute("CREATE TABLE test (mail VARCHAR(255), name VARCHAR(255))")

import re
EmailArray =[]
with open('mbox.txt') as f:
    i = -1
    for line in f:
        if line.startswith('From r'):
            EmailArray.append(line)
            i += 1

for y in EmailArray:
    ay = re.findall('^From .*@([^ ]*)', y)
    # print('sdf',ay)
    mycur.execute('INSERT INTO test (mail,name) VALUES(%s,%s)',(ay[0],'car'))
# print('alo alo',y,EmailArray[0])

# for i in y:
#     print(i)



mydb.commit()





# for i in mycur:
#     print('nè nè',i)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# from flask import  Flask
# app = Flask(__name__)
# @app.route("/")
# def hello():
#     return "Hello, World!"
#
#
# @app.route('/user/<username>')
# def user(username):
#     return "User Page %s" % username
#
# app.run(host='127.0.0.1', port=9999)

# from tkinter import *
# from tkinter import ttk
# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!fsnkfksndfjknk").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()



# mycur.execute("CREATE TABLE test(Mail VARCHAR(225)")
# mydb.commit()