## @file forms.py
# @author Stephen Longofono
# @brief Defines custom forms for server-side validation
# @details
# This module defines a number of custom forms used for accepting and filtering input
# on the server side portion of our project.  Specifically, we use it to gather login
# information and to verify that a date is of the valid form.
#
# The regular expression was built with help from a 2016 tutorial by Jan Goyvaerts
# Accessed September 2016
# https://www.regular-expressions.info/dates.html
#

from flask_wtf import Form
from wtforms import StringField, PasswordField
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

## @class LoginForm
# @brief Form which requires user credentials to submit
# @details
# LoginForm enforces the presence of both a username and a password.  The parent class
# Form defines the interface to flask. The variables below define fields in the form, and
# how they are validated.
#
class LoginForm(Form): #custom class inherits from wtf.Form
	uname = StringField('uname', validators=[Required()])
	pword = PasswordField('pword', validators=[Required()])

## @class DateForm
# @brief Form which validates a string is in date format, mm/dd/yyyy or mm-dd-yyyy
# @details
# DateForm enforces the presence of a date string, delimited by dashes or slashes.  The parent
# class Form defines the interface to flask.  The date variable below defines the field in the
# form, and provides a regular expression to validate input with.
#
class DateForm(Form):
	date = StringField('date', validators=[Required(), Regexp(dateRegx, message='Please enter a date of the form mm/dd/yyyy')])

class DetailForm(Form):
	detail = StringField('detail')
	
