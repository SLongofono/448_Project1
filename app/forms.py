## @file forms.py
# @author Stephen Longofono
# @brief Defines custom forms for server-side validation
# @details
# This module defines a custom form used for accepting and filtering input
# on the server side portion of our project.  Specifically, we use it to gather login
# information.
#

#

from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import Required

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
