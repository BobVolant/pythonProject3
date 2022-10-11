import json
from flask import  Flask
from flask import jsonify
from flask import request
app = Flask(__name__)


import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root',passwd='root', database='mse')
mycur = mydb.cursor(dictionary=True)
mycur.execute('''
create table if not exists mse.student(StudentCode VARCHAR(255), FirstName VARCHAR(255), LastName VARCHAR(255), Birthday VARCHAR(255), Address VARCHAR(255), Mark VARCHAR(255))
''')

# mydb.commit()
@app.route("/")
def hello():
    mycur = mydb.cursor(dictionary=True)
    mycur.execute("SELECT * FROM student")
    myresult = mycur.fetchall()
    return myresult

@app.route("/EditStudent",methods=[ 'POST'])
def EditStudent():
    u = request.get_json()
    StudentCode = u.get('StudentCode','')
    FirstName = u.get('FirstName','')
    LastName = u.get('LastName','')
    Birthday = u.get('Birthday','')
    Address = u.get('Address','')
    Mark = u.get('Mark','')
    mycur = mydb.cursor(dictionary=True)
    sql = "UPDATE student SET LastName =%s, FirstName = %s, Birthday=%s, Address=%s, Mark=%s WHERE StudentCode =%s"
    val =(LastName,FirstName,Birthday,Address,Mark,StudentCode)
    mycur.execute(sql,val)
    mydb.commit()
    return 'hello'

@app.route("/DelteSutdent",methods=[ 'POST'])
def DeleteStudent():
    u = request.get_json()
    StudentCode = u.get('StudentCode','')
    print(StudentCode)
    mycur = mydb.cursor(dictionary=True)
    sql = "DELETE FROM student WHERE StudentCode =%s"
    val =(StudentCode,)
    mycur.execute(sql,val)
    # mydb.commit()
    return 'hello'

@app.route("/AddStudent",methods=[ 'POST'])
def AddStudent():
    u = request.get_json()
    StudentCode = u.get('StudentCode', '')
    FirstName = u.get('FirstName', '')
    LastName = u.get('LastName', '')
    Birthday = u.get('Birthday', '')
    Address = u.get('Address', '')
    Mark = u.get('Mark', '')
    print(StudentCode)
    mycur = mydb.cursor(dictionary=True)
    sql = "INSERT INTO student (StudentCode,FirstName,LastName,Birthday, Address,Mark) VALUES (%s,%s,%s,%s,%s,%s)"
    val =(StudentCode,FirstName,LastName,Birthday,Address,Mark)
    mycur.execute(sql,val)
    mydb.commit()
    return 'hello'

app.run(host='127.0.0.1', port=9999)