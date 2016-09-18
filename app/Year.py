## @file Year.py
# @author Grant Jurgensen
# @brief Generates a year, including the months, weeks, and days contained with in it
#

from Month import Month
from Day import Day

## @class Year
# @author Grant Jurgensen
# @brief Generates a year, including the months, weeks, and days contained with in it
#
# @details
#
# Generates a full year (January 1st through December 31), and auto-fills itself
# with the months and days within it. It can "link" with other years, so that the
# weeks within its months are able to bleed over between the year boundaries.
#
class Year():

	## @fn __init__
	# @brief Initializes a Year object
	# @param [in] name An integer value corresponding to the year, e.g. 2016
	# @param [out] return The initialized Year object
	#
	# @details
	#
	# Initializes a Year object. Calculates whether it is a leap year, and adjusts the months
	# lengths if so. Calculates the weekday of the first day of the year in order to have
	# a reference point for all future days created. Iterates through 12 months, creates each
	# month and fills it with the appropriate days.
	#
	def __init__(self, name):
		self.name = name
		self.months = []
		monthNames = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
		weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

		# An algorithm to determine if it is a leap year, adapted from the
		# logic shown in this wikipedia page:
		# Accessed September, 2016
		# https://en.wikipedia.org/wiki/Leap_year#Algorithm
		if (name % 4 == 0 and name % 100 != 0) or name % 400 == 0:
			monthLengths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		else:
			monthLengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

		# An algorithm to determine the day of the week of the first day
		# of the year, adapted from the algortihm on the "disparate variation"
		# of Gauss's algorithm, shown here:
		# Accessed September, 2016
		# https://en.wikipedia.org/wiki/Leap_year#Algorithm
		y = (name % 100) - 1
		c = name // 100
		weekOffset = int((2.4 + name + y/4 + c/4 - 2*c)%7)

		dayCount = 0
		for i in range(12):
			days = []
			for j in range(monthLengths[i]):
				days.append(Day(weekdays[(dayCount + weekOffset)%7], j+1, None))
				dayCount += 1
			self.months.append(Month(monthNames[i], days, self))

		for i in range(12):
			if i > 0:
				self.months[i].setPrev(self.months[i-1])
			if i < 11:
				self.months[i].setNext(self.months[i+1])

	## @fn setPrev
	# @brief makes the year object aware of its previous year
	# @param [in] year A year object which that precedes this year object
	#
	# @details
	#
	# In order for the weeks within the months to be full weeks (sunday-saturday),
	# the year object must be aware of its previous year. This way the weeks may
	# bleed over into the previous year if neccessary
	#
	def setPrev(self, year):
		self.prev = year

		self.months[0].setPrev(year.months[11])
		year.months[11].setNext(self.months[0])

	## @fn setNext
	# @brief makes the year object aware of the next year
	# @param [in] year A year object which imidiately follows this year object
	#
	# @details
	#
	# In order for the weeks within the months to be full weeks (sunday-saturday),
	# the year object must be aware of its next year. This way the weeks may
	# bleed over into the next year if neccessary
	#
	def setNext(self, year):
		self.next = year

		year.months[0].setPrev(self.months[11])
		self.months[11].setNext(year.months[0])

	## @fn getMonth
	# @brief gets the month object via the name of the month
	# @param [in] monthName A string value for name of the month
	# @param [out] return Returns the month object of that name, or if none is found, None
	#
	# @details
	#
	# Searches all of its months looking for a match to the monthName argument.
	# If it finds one, it will return that month. Otherwise, it will return None.
	#
	def getMonth(self, monthName):
		monthNames = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
		for i in range(len(monthNames)):
			if monthName == monthNames[i]:
				return self.months[i]

		return None
