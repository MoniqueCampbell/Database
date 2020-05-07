"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import os
from app import app
from flask import render_template, request, redirect, url_for, flash, session, abort
from werkzeug.utils import secure_filename
from .forms import RegForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash

from flask_mysqldb import MySQL
from app import app

# Configure db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Monique5!'
app.config['MYSQL_DB'] = 'socialmedia'

mysql = MySQL(app)

@app.route('/')
def index():
    """Render website's home page."""
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        form = RegForm()
        return render_template('reg.html', form = form)

    form = RegForm()
    if request.method == 'POST':
        # Fetch form data
        first = request.form['firstname']
        last = request.form['lastname']
        email_add = request.form['email']
        #reg expression
        telephone = request.form['telephone_no']
        #reg expression (7 numbers not starting with 0)
        street = request.form['street_name']
        city_name = request.form['city']
        coun = request.form['country']
        area = request.form['area_code']
        #reg expression (4 numbers)
        passw = request.form['password']
        #reg expression (more than 7 characters with alteast a capital letter and symbol)
        cpass = request.form['con_pass']

        if passw!=cpass:
            flash('Non-matching Passwords', 'success')
            form = RegForm()
            return render_template('reg.html', form = form)
        cur = mysql.connection.cursor()
        cur.execute("SELECT count(email) FROM User WHERE email='{}'".format(email_add))
        result=cur.fetchall()
        emailcount = int(result[0][0])

        if emailcount > 0:
            flash('Email being used', 'success')
            form = RegForm()
            return render_template('reg.html', form = form)
        passwo = generate_password_hash(passw, method='pbkdf2:sha256')
        cur.execute("INSERT INTO User(firstName, lastName, email, password_digest) VALUES (%s, %s, %s, %s)", (first, last, email_add, passwo))
        mysql.connection.commit()
        cur.execute("SELECT user_id FROM User WHERE email='{}'".format(email_add))
        result=cur.fetchall()
        use_r = result[0][0]
       
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Phone(user_id, telephone_no, area_code) VALUES (%s ,%s, %s)", (use_r, telephone, area))
        cur.execute("INSERT INTO Address(user_id, street_name, city, country) VALUES (%s ,%s, %s, %s)", (use_r, street, city_name, coun))
        #cur.execute("INSERT INTO Phone(user_id, telephone_no, area_code) VALUES  (use_r, telephone, area)")
        #cur.execute("INSERT INTO Address(user_id, street_name, city, country) VALUES (use_r, street, city_name, coun)")
        mysql.connection.commit()
        cur.close()
        return render_template('index.html')
    return render_template('reg.html',form=form)

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM User")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html',userDetails=userDetails)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form = LoginForm()
        return render_template('login.html', form = form)

    form = LoginForm()
    if request.method == 'POST':
        # Fetch form data
        email_add = request.form['e_mail']
        passw = request.form['password']
        passwo = generate_password_hash(passw, method='pbkdf2:sha256')
        cur = mysql.connection.cursor()

        cur.execute("SELECT password_digest FROM User WHERE email='{}'".format(email_add))
        re_sult=cur.fetchall()

        if len(re_sult)==0:
            flash('Invalid Info', 'success')
            return render_template('login.html', form = form)

        pass_hash = re_sult[0][0]

        if check_password_hash(pass_hash,passw):
            flash('Successfully Logged In', 'success')
            cur.execute("SELECT user_id FROM User WHERE password_digest='{}'".format(pass_hash))
            result=cur.fetchall()
            userid = result[0][0]

            cur.close()
            return redirect(url_for('profileuserid', userid = userid))
        else:
            flash('Invalid Info', 'success')
            return render_template('login.html', form = form)

@app.route('/profileuserid/<int:userid>')
def profileuserid(userid):
    cur = mysql.connection.cursor()
    cur.execute("SELECT firstname FROM User WHERE user_id='{}'".format(userid))
    result=cur.fetchall()
    firstname = result[0][0]
    return render_template('profileuserid.html', fn=firstname)
        
###
# The functions below should be applicable to all Flask apps.
###

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
