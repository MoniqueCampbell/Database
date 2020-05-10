from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import TextAreaField, TextField, SelectField, StringField, PasswordField, HiddenField
from wtforms.validators import DataRequired, Email, InputRequired, Required
from wtforms.fields.html5 import DateField

class RegForm(FlaskForm):
    firstname = TextField('First Name:', validators = [DataRequired()])
    lastname = TextField('Last Name:', validators = [DataRequired()])
    email = TextField('Email:', validators = [DataRequired(), Email()], render_kw={"placeholder": "e.g. jdoe@example.com"})
    password = PasswordField('Password:', validators = [DataRequired()])
    con_pass = PasswordField('Confirm Password:', validators=[InputRequired()])
    telephone_no = TextField('Telephone Number:', validators = [DataRequired()])
    street_name = TextField('Street Name:', validators = [DataRequired()])
    city = TextField('City:', validators = [DataRequired()])
    country = TextField('Country:', validators = [DataRequired()])
    area_code = TextField('Area Code:', validators = [DataRequired()])

class LoginForm(FlaskForm):
    e_mail = StringField('Email:', validators=[InputRequired()])
    password = PasswordField('Password:', validators=[InputRequired()])

gen = [('Female', 'Female'), ('Male', 'Male')]
class ModAboutForm(FlaskForm):
    dob = DateField('Date of Birth:', format='%Y-%m-%d')
    gender = SelectField('Gender', choices=gen)
    nickname = TextField('Nickname:', validators=[InputRequired()])

class AdminForm(FlaskForm):
    username = StringField('Username:', validators=[InputRequired()])
    password = PasswordField('Password:', validators=[InputRequired()])

class CPostForm(FlaskForm):
    description = TextAreaField('Description:', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'Images only!'])])

class UppForm(FlaskForm):
    photo = FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'Images only!'])])

class Addcom_PostForm(FlaskForm):
    usr_text = StringField('', validators=[InputRequired()])
    pi_d = HiddenField('', validators=[InputRequired()])
