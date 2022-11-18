from flask import Flask,render_template
from flask_mysqldb import MySQL

app=Flask(__name__)
import mysql.connector
connection=mysql.connector.connect(host="localhost",user="root",password="durk2004",database="crud")



@app.route("/")
def home():
    cursor=connection.cursor()
    cursor.execute("select*from users")
    x=cursor.fetchall()
    return render_template("home.html",data=x)
if(__name__=='__main__'):
    app.run(debug=True)
