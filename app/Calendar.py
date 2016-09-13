from Year import Year

def __init__ (self,firstYear,secondYear):
    self.currentDay = year1.months[0].days[0]
    self.currentWeek = year1.months[0].week[0]
    self.year1 = Year(firstYear)
    self.year2 = Year(secondYear)
    year1.setNext(self.year2)
    year2.setprev(self.year1)

def currentDay(self):
    return self.currentDay

def currentWeek(self):
    for week in self.currentDay.month.weeks:
        for day in week:
            if day == currentDay:
                return week

def currentMonth(self):
    # Find which year we are in
    if self.year1.name = self.currentDay.year:
        for month in self.year1.months:
            if month.name = self.currentDay.month:
                return month
    else:
        for month in self.year2.months:
            if month.name = self.currentDay.month:
                return month

    return None
