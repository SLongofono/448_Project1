class Day():

	def __init__(self, month, weekday, date, details):
		self.month = month
		self.weekday = weekday
		self.date = date
		self.details = details
		
	def addDetails(self, detail):
		self.details.append(detail)
		return True #when would it be false?
		
	def editDetails(self, remove, idx):
		if remove:
			if idx < details.len():
				del details[idx]
				return True
			else:
				return False
				
		#else
			#clarification on what to do?
			