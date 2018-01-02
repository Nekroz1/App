from flask import Flask, render_template,json,session,request, g
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
import os
import json
app= Flask(__name__)
mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'school'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn=mysql.connect()
cursor=conn.cursor()
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/Enter')
def showLogin():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html')
    
@app.route('/login', methods=['POST'])
def login():
    username=request.form['inputUsername']
    password=request.form['inputPassword']
    if (cursor.execute('Select * from teacher WHERE teusername = "'+username+'" AND tepassword = "'+password+'"')):
        conn.commit()
        session['logged_in'] = True
        return render_template('index.html')
    else:
        conn.commit()
        session['logged_in'] = False
        return render_template('login.html')
    
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return render_template('index.html')
    
@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp',methods=['POST'])
def signUp():
 
    # read the posted values from the UI
    _username = request.form['inputUsername']
    _password = request.form['inputPassword']
    _name = request.form['inputName']
    _surname = request.form['inputSurname']
    _role = request.form['inputRole']
    cursor.callproc('addTeacher',(_username,_password,_name,_surname,_role))
    data = cursor.fetchall()
 
    if len(data) is 0:
        conn.commit()
        return json.dumps({'message':'User created successfully !'})
    else:
        return json.dumps({'error':str(data[0])})
    
def query_db(query, args=(), one=False):
    cursor.execute(query, args)
    rv = [dict((cursor.description[idx][0], value)
    for idx, value in enumerate(row)) for row in cursor.fetchall()]
    return (rv[0] if rv else None) if one else rv        
        
@app.route('/students/', methods=['GET'])
def students():
    if session.get('logged_in'):
        student = query_db("SELECT stid,stusername,stname,stsurname,strole,stbday FROM student")
        return render_template('students.html',student=student)
    else:
        return main() 

@app.route('/students/studentadd')
def studentadd():
    return render_template('student_add.html')

@app.route('/st_add',methods=['POST'])
def st_add():
 
    # read the posted values from the UI
    _username = request.form['inputUsername']
    _password = request.form['inputPassword']
    _name = request.form['inputName']
    _surname = request.form['inputSurname']
    _role = request.form['inputRole']
    _bday = request.form['inputBday']
    cursor.callproc('addStudent',(_username,_password,_name,_surname,_role,_bday))
    data = cursor.fetchall()
 
    if len(data) is 0:
        conn.commit()
        return json.dumps({'message':'Student created successfully !'})
    else:
        return json.dumps({'error':str(data[0])})
 
@app.route('/students/studentup')
def studentup():
    return render_template('student_update.html')
    
@app.route('/st_up',methods=['POST'])
def st_up():
    # read the posted values from the UI
    _id = request.form['inputId']
    _username = request.form['inputUsername']
    _password = request.form['inputPassword']
    _name = request.form['inputName']
    _surname = request.form['inputSurname']
    _role = request.form['inputRole']
    _bday = request.form['inputBday']
    query = "UPDATE student SET stusername = %s WHERE stid = %s AND NOT %s = ''"
    cursor.execute(query,(_username,_id,_username))
    query = "UPDATE student SET stpassword = %s WHERE stid = %s AND NOT %s = ''"
    cursor.execute(query,(_password,_id,_password))
    query = "UPDATE student SET stname = %s WHERE stid = %s AND NOT %s = ''"
    cursor.execute(query,(_name,_id,_name))
    query = "UPDATE student SET stsurname = %s WHERE stid = %s AND NOT %s = ''"
    cursor.execute(query,(_surname,_id,_surname))
    query = "UPDATE student SET strole = %s WHERE stid = %s AND NOT %s = ''"
    cursor.execute(query,(_role,_id,_role))
    query = "UPDATE student SET stbday = %s WHERE stid = %s AND NOT %s = ''"
    cursor.execute(query,(_bday,_id,_bday))
    data = cursor.fetchall()
 
    if len(data) is 0:
        conn.commit()
        return json.dumps({'message':'Student updated successfully !'})
    else:
        return json.dumps({'error':str(data[0])})    
    
@app.route('/students/studentde')
def studentde():
    return render_template('student_delete.html')
    
@app.route('/st_de',methods=['POST'])
def st_de():
    # read the posted values from the UI
    _id = request.form['inputId']
   
    query = "DELETE FROM student WHERE stid = %s"
    cursor.execute(query,_id)
    data = cursor.fetchall()
 
    if len(data) is 0:
        conn.commit()
        return json.dumps({'message':'Student deleted successfully !'})
    else:
        return json.dumps({'error':str(data[0])}) 
        
@app.route('/subjects/', methods=['GET'])
def subjects():
    if session.get('logged_in'):
        subject = query_db("SELECT subid,subcode,subname,subdescription FROM lessons")
        return render_template('subjects.html',subject=subject)
    else:
        return main()  


@app.route('/subjects/subjectadd')
def subjectadd():
    return render_template('subject_add.html')
  
@app.route('/su_add',methods=['POST'])
def su_add():
 
    # read the posted values from the UI
    _code = request.form['inputCode']
    _name = request.form['inputSubjectname']
    _description = request.form['inputDes']
    cursor.callproc('addSubject',(_code,_name,_description))
    data = cursor.fetchall()
 
    if len(data) is 0:
        conn.commit()
        return json.dumps({'message':'Subject created successfully !'})
    else:
        return json.dumps({'error':str(data[0])})        

@app.route('/subjects/subjectup')
def subjectup():
    return render_template('subject_update.html')        

@app.route('/su_up',methods=['POST'])
def su_up():
    # read the posted values from the UI
    _id = request.form['inputId']
    _code = request.form['inputCode']
    _name = request.form['inputSubjectname']
    _description = request.form['inputDes']
    query = "UPDATE lessons SET subcode = %s WHERE subid = %s AND NOT %s = ''"
    cursor.execute(query,(_code,_id,_code))
    query = "UPDATE lessons SET subname = %s WHERE subid = %s AND NOT %s = ''"
    cursor.execute(query,(_name,_id,_name))
    query = "UPDATE lessons SET subdescription = %s WHERE subid = %s AND NOT %s = ''"
    cursor.execute(query,(_description,_id,_description))
    data = cursor.fetchall()
 
    if len(data) is 0:
        conn.commit()
        return json.dumps({'message':'Lessons updated successfully !'})
    else:
        return json.dumps({'error':str(data[0])}) 
  
@app.route('/subjects/subjectde')
def subjectde():
    return render_template('subject_delete.html')

@app.route('/su_de',methods=['POST'])
def su_de():
    # read the posted values from the UI
    _id = request.form['inputId']
   
    query = "DELETE FROM lessons WHERE subid = %s"
    cursor.execute(query,_id)
    data = cursor.fetchall()
 
    if len(data) is 0:
        conn.commit()
        return json.dumps({'message':'Subject deleted successfully !'})
    else:
        return json.dumps({'error':str(data[0])}) 
 
@app.route('/projects/', methods=['GET'])
def projects():
    if session.get('logged_in'):
        project = query_db("SELECT prcode,prtitle,prsubdate,prdesc,subcode FROM project")
        return render_template('projects.html',project=project)
    else:
        return main() 
        
@app.route('/projects/projectadd')
def projectadd():
    return render_template('project_add.html')
    
@app.route('/pr_add',methods=['POST'])
def pr_add():
 
    # read the posted values from the UI
    _title = request.form['inputTitle']
    _submission = request.form['inputDate']
    _description = request.form['inputPdes']
    _code = request.form['inputCode']
    cursor.callproc('addProject',(_title,_submission,_description,_code))
    data = cursor.fetchall()
 
    if len(data) is 0:
        conn.commit()
        return json.dumps({'message':'Project created successfully !'})
    else:
        return json.dumps({'error':str(data[0])})
        
@app.route('/projects/projectup')
def projectup():
    return render_template('project_update.html')
    
@app.route('/pr_up',methods=['POST'])
def pr_up():
    # read the posted values from the UI
    _id = request.form['inputId']
    _title = request.form['inputTitle']
    _submission = request.form['inputDate']
    _description = request.form['inputPdes']
    _code = request.form['inputCode']
    query = "UPDATE project SET prtitle = %s WHERE prcode = %s AND NOT %s = ''"
    cursor.execute(query,(_title,_id,_title))
    query = "UPDATE project SET prsubdate = %s WHERE prcode = %s AND NOT %s = ''"
    cursor.execute(query,(_submission,_id,_submission))
    query = "UPDATE project SET prdesc = %s WHERE prcode = %s AND NOT %s = ''"
    cursor.execute(query,(_description,_id,_description))
    query = "UPDATE project SET subcode = %s WHERE prcode = %s AND NOT %s = ''"
    cursor.execute(query,(_code,_id,_code))
    data = cursor.fetchall()
 
    if len(data) is 0:
        conn.commit()
        return json.dumps({'message':'Project updated successfully !'})
    else:
        return json.dumps({'error':str(data[0])})
        
@app.route('/projects/projectde')
def projectde():
    return render_template('project_delete.html')
    
@app.route('/pr_de',methods=['POST'])
def pr_de():
    # read the posted values from the UI
    _id = request.form['inputId']
   
    query = "DELETE FROM project WHERE prcode = %s"
    cursor.execute(query,_id)
    data = cursor.fetchall()
 
    if len(data) is 0:
        conn.commit()
        return json.dumps({'message':'Project deleted successfully !'})
    else:
        return json.dumps({'error':str(data[0])})     
        
if __name__=="__main__":
    app.secret_key =os.urandom(12)
    app.run()