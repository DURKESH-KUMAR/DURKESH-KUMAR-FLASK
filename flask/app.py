from flask import Flask,render_template,url_for,redirect,request,flash
from flask_mysqldb import MySQL
app=Flask(__name__)
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="durk2004"
app.config["MYSQL_DB"]="crud"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)

#loading home page
@app.route("/")
def home():
    connection=mysql.connection.cursor()

    connection.execute("select*from users")
    x=connection.fetchall()
    
    return render_template("home.html",data=x)

#new users 
@app.route("/addusers.html",methods=['GET','POST'])
def addusers():
    if request.method=='POST':
        name=request.form['name']
        city=request.form['city']
        age=request.form['age']
        connection=mysql.connection.cursor()
        x="""insert into users(NAME,CITY,AGE)value("{}","{}","{}")""".format(name,city,age)
        connection.execute(x)
        mysql.connection.commit()
        connection.close()
        flash('user details added')
        
        return redirect(url_for("home"))

    return render_template("addusers.html")

#update users
@app.route("/edituser/<string:id>",methods=['GET','POST'])
def edituser(id):
    connection=mysql.connection.cursor()
    if request.method=='POST':
        name=request.form['name']
        city=request.form['city']
        age=request.form['age']
        sql="""update users set NAME="{}",CITY="{}",AGE="{}" where ID="{}" """.format(name,city,age,id)
        connection.execute(sql)
        mysql.connection.commit()
        connection.close()
        flash("user details updated")
        return redirect(url_for("home"))
    connection=mysql.connection.cursor()
    x="""select * from users where ID="{}" """.format(id)
    connection.execute(x)
    y=connection.fetchone()
    return render_template("editusers.html",datas=y)
#delete user
@app.route("/deleteuser/<string:id>",methods=['GET','POST'])
def deleteuser(id):
    connection=mysql.connection.cursor()
    sql="""delete from users where ID="{}" """.format(id)
    connection.execute(sql)
    mysql.connection.commit()
    connection.close()
    flash("user details deleted")
    return redirect(url_for("home"))



    

if(__name__=='__main__'):
    app.secret_key="durk2004"
    app.run(debug=True)
