from flask_wtf import FlaskForm
from wtforms import validators,EmailField,StringField,SubmitField,PasswordField
from wtforms.validators import Email,Length,DataRequired
class RegistrationForm(FlaskForm):
 username = StringField("Username", validators=[DataRequired(),Length(min=4,max=35)])
 email = EmailField("Email",validators=[Email(),DataRequired()])
 password = PasswordField("Password", validators=[DataRequired(),Length(min=8,max=20)])
 submit = SubmitField("Submit")

class LoginForm(FlaskForm):
 email = EmailField("Email",validators=[Email(),DataRequired()])
 password = PasswordField("Password",validators=[Length(min=5,max=25)])
 submit = SubmitField("Submit")