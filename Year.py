from Month import Month
from Day import Day

class Year():

	def __init__(self, name, weekOffset): #could just include flag for leap
		self.name = name
		self.months = []
		#self.firstDay = firstDay
		#self.lastDay = lastDay
		monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
		weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

		#tests for leap
		if (name % 4 == 0 and name % 100 != 0) or name % 400 == 0:	
			monthLengths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		else:
			monthLengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

		dayCount = 0
		for i in range(12):
			days = []
			for j in range(monthLengths[i]):
				days.append(Day(monthNames[i], weekdays[(dayCount + weekOffset)%7], j+1, None))
				dayCount += 1
			self.months.append(Month(monthNames[i], days, name))

		for i in range(12):
			if i > 0:
				self.months[i].setPrev(self.months[i-1])
			if i < 11:
				self.months[i].setNext(self.months[i+1])
