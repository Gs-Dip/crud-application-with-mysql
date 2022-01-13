from flask import Flask,render_template, request ,redirect,url_for,flash #flash hocche flask ar bydefult akti method jar kaj notification deya  
from flask.helpers import url_for
from flask_mysqldb import MySQL

app =Flask(__name__)
app.secret_key="flash messege" # secret_key obossoi bebohar korte hobe ta na hole amra flash bebohar kore gele error dekhabe.....secret_key ar value ja khushi dilei hoy 


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'dipdip2020'
app.config['MYSQL_DB'] = 'user_info'


mysql=MySQL(app)




@app.route('/')
def index():
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM employee")     
    data = cur.fetchall()
    cur.close()


    return render_template('index.html',employee=data)



@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":  
        flash("Add Employee Successfully")  # flash ar kaj hocche notification dekhano

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        cur =mysql.connection.cursor()
        cur.execute("INSERT INTO employee (name, email, phone) VALUES (%s, %s, %s)",(name, email, phone))
        mysql.connection.commit()
        return redirect(url_for('index'))




@app.route('/update', methods= ['POST','GET'])
def update():
    if request.method == 'POST': 
        id_data=request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']


        cur=mysql.connection.cursor()
        cur.execute("""
        
        UPDATE employee
        SET name=%s, email=%s, phone=%s
        WHERE id=%s
        
        
        """,(name,email,phone,id_data))

        flash ("Update Information Successfully") # flash ar ai messege ta receive korar jonno index.html page a code kora ache 
        mysql.connection.commit()
        return redirect(url_for('index'))



@app.route('/delete/<string:id_data>',methods=['GET'])   #/delete/<string:id_data>    akhane /delete ar sathe peramiter pass kora hoyeche and ai peramiter ta obossoi pass korte hobe    
def delete(id_data):


    flash("Information Deleted Successfully")
    cur=mysql.connection.cursor()
    cur.execute("DELETE FROM employee WHERE id=%s ",(id_data,))
    mysql.connection.commit()
    return redirect(url_for('index'))







if __name__=='__main__':
    app.run(debug=True)    