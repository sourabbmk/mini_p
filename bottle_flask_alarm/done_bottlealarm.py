from bottle import request, template,route,run,get,post
import sqlite3
import threading
import datetime

@route('/')
def index():
    return template('smart')

@post('/result')
def result():
    # print(request.body.read())  gives raw data
    result = request.forms
    usr_time = request.forms['usr_time']      #get all the values using keys
    A = request.forms.get('A')
    B = request.forms.get('B')
    C = request.forms.get('C')
    usr_hour,usr_mins = usr_time.split(":")


    with sqlite3.connect("database.db") as conn:
        cur = conn.cursor()

        cur.execute("CREATE TABLE IF NOT EXISTS bottable(hour TEXT, minutes TEXT, A TEXT, B TEXT, C TEXT)")
        cur.execute("INSERT INTO bottable(hour,minutes,A,B,C) VALUES (?,?,?,?,?)", (usr_hour,usr_mins,A,B,C))
        cur.execute("select * from bottable")
        data = cur.fetchall()       #get the whole table

        conn.commit()

    t1=threading.Thread(target=calc, args=(data,))    
    t1.start()  

    return template("result",result = result)

def calc(data):

    print(data)               #prints the whole table
    match_not_found=True
    while match_not_found:
        h=datetime.datetime.today().strftime("%H")              
        mi=datetime.datetime.today().strftime("%M")
        # z=[(i[2],i[3],i[4]) for i in data if i[0] == h and i[1]==mi]
        for i in data: 
            if i[0] == h and i[1]==mi:
                print ([j for j in i[2:5] if j != None])
                match_not_found=False
                break


if __name__ == '__main__':
    run(host='localhost',port=8080,debug='True',reloader='True')