



from Year import Year

def __init__ (self,1stYear,2ndYear):
    self.currentDay = year1.months[0].days[0]
    self.currentWeek = year1.months[0].week[0]
    year1 = Year(1stYear)
    year2 = Year(2ndYear)
    year1.setNext(year2)
    year2.setprev(year1)

def currentDay(self):
    return self.currentDay

def currentWeek(self):
    for week in self.currentDay.month.weeks:
        for day in week:
            if day == currentDay:
                return week
def currentMonth(self):
    return currentDay.month
