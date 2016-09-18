## @file Month.py
# @author Grant Jurgensen
# @brief A month which possesses a list of days, and calculates lists of weeks
#

from Day import Day

## @class Month
# @author Grant Jurgensen
# @brief A month which possesses a list of days, and calculates lists of weeks
#
# @details
#
# A container for a month, holds the associated days, as well as weeks within it.
# In order for the weeks to all be full (7 days, sunday-saturday), the month must
# be made aware of its previous and next months.
#
class Month():

	## @fn __init__
	# @brief Initializes a month object
	# @param [in] name A string value of the month's name, e.g 'January'
	# @param [in] days A list of days which the month contains
	# @param [in] year The year object that the month belongs to
	# @param [out] return The initialized month object
	#
	# @details
	#
	# Initializes a Month object. Stores its name, year, and days. Creates a first
	# draft of its weeks (The weeks won't neccessary be full until the month is made
	# aware of its previous and next month).
	#
	def __init__(self, name, days, year):
		self.name = name
		self.days = days
		self.numDays = len(days)
		self.year = year

		for day in days:
			day.month = self

		self.weeks = [[]]
		for day in self.days:
			if day.weekday == 'Sunday':
				self.weeks.append([])

			self.weeks[-1].append(day)

	## @fn setPrev
	# @brief sets the previous month, updates the first week
	# @param [in] month The month object which proceeds this month
	# @param [out] return Returns true if it was able to complete the first week,
	# false otherwise
	#
	# @details
	#
	# Sets the previous month, and then if the first week of the month isn't already
	# full, it will work backwards and continuously add to the front of the first
	# week until it reaches "Sunday". Returns true if successful, false otherwise
	#
	def setPrev(self, month):
		self.prev = month
		try:
			i = self.prev.numDays - 1
			while self.weeks[0][0].weekday != 'Sunday':
				self.weeks[0].insert(0, self.prev.days[i])
				i -= 1
			return True
		except IndexError:
			return False

	## @fn setNext
	# @brief sets the next month, updates the last week
	# @param [in] month The month object which imidiately follows this month
	# @param [out] return Returns true if it was able to complete the last week,
	# false otherwise
	#
	# @details
	#
	# Sets the next month, and then if the last week of the month isn't already
	# full, it will work forward and continuously add to the back of the last
	# week until it reaches "Saturday". Returns true if successful, false otherwise
	#
	def setNext(self, month):
		self.next = month
		try:
			i = 0
			while self.weeks[-1][-1].weekday != 'Saturday':
				self.weeks[-1].append(self.next.days[i])
				i += 1
			return True
		except IndexError:
			return False

	## @fn getDay
	# @brief Gets the day at a certain date
	# @param [in] date An integer value, the date of the day, e.g 5 for the 5th
	# @param [out] return Returns the day if the date was within the bounds of the month
	# 					  otherwise it returns None
	#
	def getDay(self, date):
		if (date-1) < len(self.days) and (date-1) >= 0:
			return self.days[date-1]
		else:
			return None
