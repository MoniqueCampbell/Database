from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import TextAreaField, TextField, SelectField
from wtforms.validators import DataRequired, Email
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired

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
   