## @file views.py
# @author Stephen Longofono
# @brief Manages login, session, and server-side interaction of project pages
#
# @details
# 	This file defines all the viable addresses for our project webpages and how
# they will interact on the server side.  After directing visitors through a login
# process, a session is established to designate that a user is authenticated.
#
# 	A calendar object is maintained for the lifetime of the server, created from scratch
# and populated with details from a logfile if present.  There is only one user, so for
# this iteration there is only one logfile.
#
#	Each method is marked with a decorator, indicating that Flask should call that
# method when the address argument of app.route() is accessed by the user.  Most methods
# handle the control of what the user can and cannot see or otherwise access.  The process
# method interacts with client-side Javascript to parse and interpret input.  Javascript is
# able to access objects passed into the render_template() method, and responds to the server
# via JSON.
#

from app import app					# Import our configured app object from upstream
from flask import render_template	# Ability to use jinja2 templates
from flask import flash				# Ability to pass consumeable text content to user
from flask import redirect			# Ability to override browser address request
from flask import session			# Cookies to track the calendar for session
from flask import url_for			# Let flask manage urls, we use function names
from forms import LoginForm			# Import custom definition defined in forms.py
from flask import request			# Allow access to HTTP requests
from flask import json				# Prepare responses to requests for client
from flask import logging			# Developer feedback
import traceback					# Exception feedback
import Calendar

# TODO insert logfile i/o here
calendar_obj	= Calendar.Calendar(2016, 2017, 'logfile.txt')
calendar_obj.load()
app.logger.info(calendar_obj.year1.name)
app.logger.info(calendar_obj.getCurrentDay().details)

@app.route('/deleteDetail')
def delete():
	try:
		# Grab and process form data
		#['day','date','month','year', 'detail']
		day = request.form['day']
		date = request.form['date']
		month = request.form['month']
		year = int(request.form['year'])
		detail = request.form['detail']

		#Find the day
		day_obj = calendar_obj.getCurrentDay()

		#Find the index of the detail and delete
		day_obj.pop(day_obj.index(detail))

		#Update log file
		calendar_obj.save()

		app.logger.info('This day state:')
		app.logger.info(day_obj.details)

		app.logger.info('Calendar obj state:')
		app.logger.info(calendar_obj.getCurrentDay().details)
	except:
		# Log exception info on failure
		app.logger.info(traceback.print_exc())

		#return fail status
		return json.dumps({'status':'BAD'})

	# return ok status
	return json.dumps({'status':'OK'})


## @fn index
# @brief root domain request behavior
# @param [in]  session An implicit variable generated by flask, acts as a cryptographically signed cookie to store any information which should be preserved across requests
# @param [in]  view An optional parameter representing the view template to render
# @param [out] return A rendered HTML document representing the current state of the calendar
#
# @details
#
# The root will always check that a session has been established for the user.
# Failure to meet this condition will redirect the user to the login() method.
# If the optional view is specified, the appropriate template will be rendered, otherwise
# the day template is used.
#
@app.route('/')
@app.route('/index')
@app.route('/index/<string:view>')
def index(view=None):
	if 'uname' in session:
		# if logged in...

		# Give precedence to directly specified view
		display = view or 'day'
		year  = calendar_obj.getCurrentYear().name
		month = calendar_obj.getCurrentMonth().name
		weekday = calendar_obj.currentDay.weekday

		if 'week' == display:
			daysList = [str(x.date) for x in calendar_obj.currentWeek]
			return render_template('week.html',
									days=daysList,
									dayNames = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
									month=month,
									year=year,
									user=session['uname'])

		elif 'month' == display:
			month_obj = calendar_obj.getCurrentMonth()
			firstDay = month_obj.days[0].weekday
			numDays = len(month_obj.days)
			lastDay = month_obj.days[numDays-1].weekday
			weeks = []
			for week in calendar_obj.getCurrentMonth().weeks:
				weeks.append([str(x.date) for x in week])
			return render_template('month.html',
									weeks=weeks,
									firstDay=firstDay,
									lastDay=lastDay,
									month=month,
									year=year,
									user=session['uname'])

		elif 'year' == display:
			return render_template('year.html',
									year=year,
									user=session['uname'])

		weekday = calendar_obj.getCurrentDay().weekday
		date = calendar_obj.getCurrentDay().date
		details = list(calendar_obj.getCurrentDay().details)
		for i in details:
			i.replace('_', ' ')
		app.logger.info(details)
		return render_template('day.html',
								weekday=weekday,
								date=date,
								details=details,
								month=month,
								year=year,
								user=session['uname'])

	# User hasn't logged in yet, provide feedback
	flash('You must log in to see this page')
	return redirect(url_for('login'))


## @fn login
# @brief login request behavior
# @param [in]  session An implicit variable generated by flask, acts as a cryptographically signed cookie to store any information which should be preserved across requests
# @param [out] return Redirects to the index() method, or A rendered HTML document of the login page if the login credentials are invalid
#
# @details
#
# The login will validate the user's input using a LoginForm and create a session for the user if the
# credentials are valid.  The user and session are then redirected to the index() method.  If the user
# credentials are invalid, the login page is re-rendered and feedback is provided.
#
@app.route('/login', methods=['GET', 'POST'])
def login():

	form = LoginForm()
	if form.validate_on_submit():	#if all our validation checks pass
		if form.uname.data == app.config['USERNAME'] and form.pword.data == app.config['PASSWORD']:
			# Send up a feedback message
			flash('%s was logged in' % ( form.uname.data ))
			user = {'name':form.uname.data}
			# Prepare a session to hold user info and the calendar objects
			session['uname'] = form.uname.data
			# Go to main page with populated session
			return redirect(url_for('index'))

	# bad login, provide feedback
	flash('invalid username or password')
	return render_template('login.html', title='Sign In', form=form)


## @fn logout
# @brief logout request behavior
# @param [in]  session An implicit variable generated by flask, acts as a cryptographically signed cookie to store any information which should be preserved across requests
# @param [out] return Redirects to the login() method
#
# @details
#
# The logout will clear all data from the session field, and redirect to the login() method
#
@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('login'))

## @fn process
# @brief processes changes to details in calendar and logfile
# @param [in] JSON This is an implicit parameter passed along via Flask's
#				   request construct.  It is reconstructed as a dictionary
#				   on entry to this method.
# @param [out] return Returns a JSON-style object representing the status
#
# @details
#
# The process method will attempt to parse JSON-style form data sent from the client-side
# representing a day and its current details.  The day in questions is located using the
# month and year passed in, and its details are replaced by those parsed from the JSON.
#
# Assumes 'day', 'month', 'year', and 'date' are present
#
@app.route('/process', methods=['POST'])
def process():

	try:
		# Grab and process form data
		#['day','date','month','year']
		day = request.form['day']
		date = request.form['date']
		month = request.form['month']
		year = int(request.form['year'])

		newDetails = []

		for key, value in request.form.iteritems():
			if key.startswith('detail'):
				newDetails.append(value)
		#Find the day
		day_obj = calendar_obj.getCurrentDay()

		app.logger.info('Changing details, old values:')
		app.logger.info(day_obj.details)
		day_obj.details = newDetails
		app.logger.info('\nNew values:')
		app.logger.info(day_obj.details)
		#Update log file
		calendar_obj.save()

		app.logger.info('This day state:')
		app.logger.info(day_obj.details)

		app.logger.info('Calendar obj state:')
		app.logger.info(calendar_obj.getCurrentDay().details)
	except:
		# Log exception info on failure
		app.logger.info(traceback.print_exc())

		#return fail status
		return json.dumps({'status':'BAD'})

	# return ok status
	return json.dumps({'status':'OK'})


## @fn viewChange
# @brief handles routing for changing the client's view of the current day/week/month/year
# @param [in] JSON This is an implicit parameter passed along via Flask's
#				   request construct.  It is reconstructed as a dictionary
#				   on entry to this method.
# @param [out] return Returns a JSON-style object representing the status and a link to
# 					  redirect to for client-side
#
# @details
#
# The viewChange method will attempt to parse JSON-style form data sent from the client-side
# representing a new view request.  Acceptable values for the 'view' key are 'next', 'prev',
# 'day', 'week', 'month', or 'year'.
#
# When necessary, the server-side calendar object is updated to point to the next or
# previous day.  In this case, a link for the index in day view is provided in the return.
# Otherwise, a link to index is provided with a view matching the view specfified by the JSON.
#
# Assumes 'view' is present and has a value.
#
@app.route('/viewChange', methods=['POST'])
def viewChange():
	if request.form['view'] == 'next':
		calendar_obj.currentDay = calendar_obj.getCurrentDay().getNext()
		result = {'status':'OK', 'link':url_for('index')}

	elif request.form['view'] == 'prev':
		calendar_obj.currentDay = calendar_obj.getCurrentDay().getPrev()
		result = {'status':'OK', 'link':url_for('index')}

	else:

		if request.form['view'] == 'day':
			result = {'status':'OK', 'link':url_for('index', view='day')}
		elif request.form['view'] == 'week':
			result = {'status':'OK', 'link':url_for('index',view='week')}
		elif request.form['view'] == 'month':
			result = {'status':'OK', 'link':url_for('index',view='month')}
		else:
			result = {'status':'OK', 'link':url_for('index',view='year')}

	# Prepare a JSON response with a link for root
	app.logger.info('Returning: ')
	app.logger.info(result)
	return json.dumps(result)

## @fn changeFocusX
# @brief Updates the 'focus' of the calendar increment: day, week, month, or year.
# @param [in] JSON This is an implicit parameter passed along via Flask's
#				   request construct.  It is reconstructed as a dictionary
#				   on entry to this method.
# @param [out] return A JSON containing the status, and on success a link to index
#					  with the appropriate view set.
#
# @details
#		The changeFocusX methods handle changing the view when a specific day or
# month is indicated client-side.  This method is very similar to the viewChange
# method, except that in this case the calendar object is modified to reflect the appropriate
# focus.  Specifically, the currentDay, currentWeek, currentMonth, and currentYear members of
# the Calendar class are updated.
#
# On completion the method will return a status and a link to the appropriate view using the index method.
#
# Assumes some combination of 'day', 'month', and 'year' are present and have valid values.
# See individual implementations for the expected input.  Recovers gracefully with a catch-all exception handler.
#
@app.route('/changeFocusDay', methods=['GET','POST'])
def changeFocusDay():
	try:
		app.logger.info('In change focus day')
		day = int(request.form['day'])
		monthNum = int(request.form['month'])
		year = int(request.form['year'])
		month = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'][monthNum-1]

		app.logger.info('Jumping to date: ' + month + ' ' + str(day) + ', ' + str(year))

		# Find the new focus day and update current day, week, month, year
		calendar_obj.currentMonth = calendar_obj.getMonth(month, year)
		app.logger.info('Found month: ' + calendar_obj.currentMonth.name)
		calendar_obj.currentDay = calendar_obj.currentMonth.getDay(day) or calendar_obj.currentMonth.days[0]
		if calendar_obj.currentMonth.year == calendar_obj.year1.name:
			calendar_obj.currentYear = calendar_obj.year1
		else:
			calendar_obj.currentYear = calendar_obj.year2
		calendar_obj.currentWeek = calendar_obj.getCurrentWeek()

		# return status and a link to redirect to
		result = {'status':'OK', 'link':url_for('index', view='day')}
		return json.dumps(result)
	except:
		app.logger.info(traceback.print_exc())
		result = {'status':'BAD'}
		return json.dumps(result)

@app.route('/changeFocusMonth', methods=['GET', 'POST'])
def changeFocusMonth():
	try:
		month = request.form['month']
		year = int(request.form['year'])
		calendar_obj.currentMonth = calendar_obj.getMonth(month, year)
		calendar_obj.currentWeek = calendar_obj.currentMonth.weeks[0]
		calendar_obj.currentDay = calendar_obj.currentWeek[0]
		if calendar_obj.currentMonth.year == calendar_obj.year1.name:
			calendar_obj.currentYear = calendar_obj.year1
		else:
			calendar_obj.currentYear = calendar_obj.year2

		result = {'status':'OK', 'link':url_for('index', view='month')}

		#return status and a link to redirect to
		return json.dumps(result)

	except:
		app.logger.info(traceback.print_exc())
		result = {'status':'BAD'}
		return json.dumps(result)


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html', link=url_for('index')), 404
