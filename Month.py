from Day import Day

class Month():

	def __init__(self, name, days, year):
		self.name = name
		self.days = days
		self.numDays = len(days)
		self.year = year

		#generate weeks
		self.weeks = [[]]
		for day in self.days:
			if day.weekday == 'Sunday':
				self.weeks.append([])

			self.weeks[-1].append(day)


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

	def getPrev(self):
		return self.prev

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

	def getNext(self):
		return next

	def getNumDays(self):
		return self.numDays

	def getDay(self, day):
		return self.days[day]

	def getWeek(self, idx):
		return self.weeks[idx]
