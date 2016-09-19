## @page template_dox
# @brief describes the function and purpose of the project's Jinja template files
# @author Stephen Longofono
#
# @section Files Template Files
#
# The project makes use of Jinja templates to generate uniform and dynamic HTML and CSS
# for our web application.  Each of the calendar views has its own format, which is rendered
# by flask from the views.py script.  They are documented here, because there is no great
# way to place and interpret doxygen hooks in the form of HTML comments.
#
# See the files tab for the files themselves - within are detailed descriptions
# of each of the helper functions
#
# Adapted from templates in a 2012 Flask tutorial written by Miguel Grinberg
# Accessed September 2016
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world/
#
# @subsection base base.html
#
# The base HTML template defines all common elements for the web application.  It includes
# the navigation, images, styling, and layout which all other pages inherit.  It also
# defines the dynamic blocks which inheriting templates will define.
#
# @subsection day day.html
#
# The day HTML template renders calendar elements associated with the day view, including data
# from the calendar object and forms/buttons for interacting with the application.
#
# @subsection login login.html
#
# The login HTML template renders a login form and any feedback messages passed along via flash.
#
# @subsection month month.html
#
# The month HTML template renders calendar elements associated with the month view, including data
# from the calendar object and forms/buttons for interacting with the application.
#
# @subsection week week.html
#
# The week HTML template renders calendar elements associated with the week view, including data
# from the calendar object and forms/buttons for interacting with the application.
#
# @subsection year year.html
#
# The year HTML template renders calendar elements associated with the year view, including data
# from the calendar object and forms/buttons for interacting with the application.
#
