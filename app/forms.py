from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import Required
from wtforms.validators import Regexp


#match 19** or 20**
yearRegx = '(19|20)\d\d'

#match 0* or 10,11,12
monthRegx= '(0[1-9]|1[012])'

#match 0* or 1* or 2* or 30,31
dayRegx  = '(0[1-9]|[12][0-9]|3[01])'

#match delimiters '-' or '/'
delimRegx = '[-/]'

#line up with beginning of input, and find the patterns below
dateRegx = '^' + dayRegx + delimRegx + monthRegx + delimRegx + yearRegx

class LoginForm(Form): #custom class inherits from wtf.Form
	uname = StringField('uname', validators=[Required()])
	pword = StringField('pword', validators=[Required()])

class DateForm(Form):
	date = StringField('date', validators=[Required(), Regexp(dateRegx, message='Please enter a date of the form mm/dd/yyyy')])
