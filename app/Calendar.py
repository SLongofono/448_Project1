



from Year import Year

class Calendar():
    def __init__ (self,firstYear,secondYear):
        self.year1 = Year(firstYear)
        self.year2 = Year(secondYear)
        self.year1.setNext(self.year2)
        self.year2.setPrev(self.year1)

        self.currentDay = self.year1.months[0].days[0]
        self.currentWeek = self.year1.months[0].weeks[0]

    def getCurrentDay(self):
        return self.currentDay

    def getCurrentWeek(self):
        for week in self.currentDay.month.weeks:
            for day in week:
                if day == self.currentDay:
                    return week

    def getCurrentMonth(self):
        return self.currentDay.month

    def getCurrentYear(self):
        return self.currentDay.month.year

    def getMonth(self, monthName, yearName):
        if self.year1.name == yearName:
            y = self.year1
        elif self.year2.name == yearName:
            y = self.year2

        if(y != None):
            return y.getMonth(monthName)
        else:
            return None
