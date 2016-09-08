import Day

class Month():
	
	def __init__(self, name, numDays, pastMonth, nextMonth, year):
		self.name = name
		self.pastMonth = pastMonth
		self.nextMonth = nextMonth
		self.year = year
		
		for i in range(numDays - 1):
			days[i] = Day(self, WEEKDAY, i+1, None)
			
		#generate weeks
		
		
	def makeWeek(self, startDay):
		currentMonth = startDay.Month
		currentDate = startDay.date
		
		for i in range(6):
			if currentDate > currentMonth.numDays:
				currentMonth = currentMonth.nextMonth
				currentDate = 1
				
			week[i] = currentMonth.getDay(currentDate-1)
			currentDate++
		
		return week #scope problem?
		
		
	def getDay(self, day):
		return days[day]
	
	def getWeek(self, idx):
		return weeks[idx]