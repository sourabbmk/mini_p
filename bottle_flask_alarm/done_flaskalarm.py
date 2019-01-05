
import datetime
import threading
import sqlite3
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
   return render_template('smart.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        
        result = request.form                   #save whole form in result as multidictionary
        usr_time = request.form['usr_time']      #get all the values using keys
        fan = request.form.get('Fan')
        ac = request.form.get('AC')
        light = request.form.get('Light')
        usr_hour,usr_mins = usr_time.split(":") 

        print (usr_time, usr_hour, usr_mins)



        with sqlite3.connect("database.db") as conn:
            cur = conn.cursor()

            cur.execute("CREATE TABLE IF NOT EXISTS smarttable(hour TEXT, minutes TEXT, fan TEXT, ac TEXT, light TEXT)")
            cur.execute("INSERT INTO smarttable(hour,minutes,fan,ac,light) VALUES (?,?,?,?,?)", (usr_hour,usr_mins,fan,ac,light))
            cur.execute("select * from smarttable")
            data = cur.fetchall()       #get the whole table
   
            conn.commit()
        
    t1=threading.Thread(target=calc, args=(data,))    
    t1.start()                                  #start a thread to the function calc             
        
    return render_template("result.html",result = result)



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
    app.run(debug = True)

