from flask import Flask, render_template, redirect ,flash,request,session
import mysql.connector
app = Flask(__name__)
app.secret_key = "super secret key"
@app.route('/')
@app.route('/home')
def home():
    db = mysql.connector.connect(user = 'root',
                                  password='Password@1',
                                  host= 'localhost',
                                  auth_plugin='mysql_native_password',
                                  database = 'test')
    cur1 = db.cursor()
    cur1.execute('select * from student;')
    df = cur1.fetchall()
    return render_template("predict.html",name = df )


@app.route('/edit/<int:value>', methods = ['GET'])
def edit(value):
    db = mysql.connector.connect(user='root',
                                 password='Password@1',
                                 host='localhost',
                                 auth_plugin='mysql_native_password',
                                 database='test')
    cur2 = db.cursor()
    cur2.execute('select * from student where roll_no = %s' % int(value))
    df2 = cur2.fetchone()
    cur2.close()
    db.close()
    return render_template("edit.html", name=df2)



@app.route('/edit/<int:value>', methods = ['POST'])
def edit2(value):
    if request.method == 'POST':
        name = str(request.form['name'])
        emailid = str(request.form['emailid'])
        mobile = str(request.form['mobile'])
        db = mysql.connector.connect(user='root',
                                     password='Password@1',
                                     host='localhost',
                                     auth_plugin='mysql_native_password',
                                     database='test')

        cur2 = db.cursor()
        query = 'update student set name = %s, emailid = %s, mobile = %s where roll_no  = %s;'
        data = (name,emailid,mobile,int(value))
        cur2.execute(query, data)
        db.commit()
        flash("User Details updated successfully")
        return redirect("/")

@app.route('/add', methods = ['POST','GET'])
def add():
    if request.method == 'POST':
        name = str(request.form['name'])
        emailid = str(request.form['emailid'])
        mobile = str(request.form['mobile'])
        value = str(request.form['id'])
        db = mysql.connector.connect(user='root',
                                     password='Password@1',
                                     host='localhost',
                                     auth_plugin='mysql_native_password',
                                     database='test')

        cur2 = db.cursor()
        query = 'insert into student values(%s,%s,%s,%s);'
        data = (int(value),name,emailid,mobile)
        cur2.execute(query, data)
        db.commit()
        flash("User Details updated successfully")
        return redirect("/")
    else:
        return render_template("add.html")

@app.route('/delete/<int:value>')
def delete(value):
    db = mysql.connector.connect(user='root',
                                 password='Password@1',
                                 host='localhost',
                                 auth_plugin='mysql_native_password',
                                 database='test')
    cur2 = db.cursor()
    cur2.execute('delete from student where roll_no = %s' % int(value))
    db.commit()
    cur2.close()
    db.close()
    flash("User Deleted Successfully")
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)