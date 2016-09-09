from app import app
import Year

#@app.route('/')
#@app.route('/index')
#def index():
#	return 'hello'
from flask import render_template	#ability to use jinja2 templates
from flask import flash			#ability to pass consumeable text content
from flask import redirect		#ability to override browser address request
from flask import session		#cookies to track the calendar for session
from flask import url_for		#let flask manage urls, we use function names
from forms import LoginForm		#import custom definition defined in forms.py
from forms import DateForm		#import custom date form
import datetime

#flask will trigger this if domain/, domain/index.html are accessed
@app.route('/')
@app.route('/index')
def index():
	if 'uname' in session:
		# if logged in...
		# Check if we already made a calendar for the user
		if not 'calendar' in session:
			# Instantiate a calendar object
#			session['calendar'] = init_calendar()
			calendar = {}
			calendar['name'] = '2016'
			calendar['months'] = []
			calendar['months'].append('january')
			calendar['displayMode'] = 'day'
			session['calendar'] = calendar

			# Render the day template page
			return render_template('day.html', calendar=session['calendar'], user=session['uname'])

		else:
			flash('calendar was found, rendering from main')
			# We have a calendar, render the appropriate template
			# for the calendar's display mode
			if 'day' == session['calendar']['displayMode']:
				return render_template('day.html', calendar=session['calendar'], user=session['uname'])

			elif 'week' == session['calendar'].displayMode:
				return render_template('week.html', calendar=session['calendar'])

			elif 'month' == session['calendar'].displayMode:
				return render_template('month.html', calendar=session['calendar'])

			return render_template('year.html', calendar=session['calendar'])

	# User hasn't logged in yet, provide feedback
	flash('You must log in to see this page')
	return redirect(url_for('login'))

#login view trigger
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
			flash('session prepared')
			# Go to main page with populated session
			return redirect(url_for('index'))

	# bad login, provide feedback
	flash('invalid username or password')
	return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('login'))
