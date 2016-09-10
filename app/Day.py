class Day():

	def __init__(self, month, weekday, date, details):
		self.month = month
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
