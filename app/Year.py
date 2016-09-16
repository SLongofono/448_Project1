from Month import Month
from Day import Day

class Year():

	def __init__(self, name):
		self.name = name
		self.months = []
		#self.firstDay = firstDay
		#self.lastDay = lastDay
		monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
		weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

		#tests for leap year
		if (name % 4 == 0 and name % 100 != 0) or name % 400 == 0:
			monthLengths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		else:
			monthLengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

		y = name % 100
		c = name // 100
		weekOffset = int((1.4 + name + y/4 + c/4 - 2*c)%7)

		dayCount = 0
		for i in range(12):
			days = []
			for j in range(monthLengths[i]):
				days.append(Day(weekdays[(dayCount + weekOffset)%7], j+1, []))
				dayCount += 1
			self.months.append(Month(monthNames[i], days, name))

		for i in range(12):
			if i > 0:
				self.months[i].setPrev(self.months[i-1])
			if i < 11:
				self.months[i].setNext(self.months[i+1])


	def setPrev(self, year):
		self.prev = year

		self.months[0].setPrev(year.months[11])
		year.months[11].setNext(self.months[0])

	def setNext(self, year):
		self.next = year

		year.months[0].setPrev(self.months[11])
		self.months[11].setNext(year.months[0])
