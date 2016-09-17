class Day():

	def __init__(self, weekday, date, details):
		self.month = None
		self.weekday = weekday
		self.date = date
		self.details = details

	def addDetail(self, detail):
		self.details.append(detail)

	def editDetail(self, idx, detail):
		if idx < len(details) and idx >= -1*len(details):
			self.details[idx] = detail
			return True
		else:
			return False

	def removeDetail(self, idx):
		if idx < len(details) and idx >= -1*len(details):
			del self.details[idx]
			return True
		else:
			return False

	def getPrev(self):
		if self.date > 1:
			return self.month.days[self.date-2]
		else:
			return self.month.prev.days[-1]

	def getNext(self):
		if self.date < len(self.month.days):
			return self.month.days[self.date]
		else:
			return self.month.next.days[0]
