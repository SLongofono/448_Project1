## @file Day.py
# @author Grant Jurgensen
# @brief A day with a list of details
#

## @class Day
# @author Grant Jurgensen
# @brief A day with a list of details
#
# @details
#
# A container for a single day. It is aware of its date, weekday, and details,
# as well as the month it belongs to. It provides methods by which to modify
# its list of details
#
class Day():

	## @fn __init__
	# @brief Initializes a day object
	# @param [in] weekday A string value of day of the week this day falls on, e.g. "Saturday"
	# @param [in] date An integer value corresponding to its order in the month
	# @param [in] details A list of string values, or "details" associated with the day
	# @param [out] return The initialized day object
	#
	# @details
	#
	# Initializes a Day object. Stores its weekday, date, and initial details. If it
	# does not have any initial details, it will create an empty list for them.
	#
	def __init__(self, weekday, date, details):
		self.month = None
		self.weekday = weekday
		self.date = date
		self.details = details

		if self.details == None:
			self.details = []

	## @fn addDetail
	# @brief Adds a detail to end of the detail list
	# @param [in] detail A string value you wish to add to the list of details
	#
	def addDetail(self, detail):
		self.details.append(detail)

	## @fn editDetail
	# @brief Replaces a detail with a new string value
	# @param [in] idx The index of the detail which should be replaced
	# @param [in] detail A string value you wish to replace the detail with
	# @param [out] return Returns true if successful, false otherwise
	#
	def editDetail(self, idx, detail):
		if idx < len(details) and idx >= -1*len(details):
			self.details[idx] = detail
			return True
		else:
			return False

	## @fn removeDetail
	# @brief Removes a specific detail
	# @param [in] idx The index of the detail which should be removed
	# @param [out] return Returns true if successful, false otherwise
	#
	def removeDetail(self, idx):
		if idx < len(details) and idx >= -1*len(details):
			del self.details[idx]
			return True
		else:
			return False

	## @fn getPrev
	# @brief Gets the previous day
	# @param [out] return Returns the day object that precedes it
	#
	def getPrev(self):
		if self.date > 1:
			return self.month.days[date-2]
		else:
			return self.month.prev.days[-1]

	## @fn getNext
	# @brief Gets the next day
	# @param [out] return Returns the day object that imidiately follows it
	#
	def getNext(self):
		if self.date < len(self.month.days):
			return self.month.days[date]
		else:
			return self.month.next.days[0]
