



from Year import Year

class Calendar():
    def __init__ (self,firstYear,secondYear):
        year1 = Year(firstYear)
        year2 = Year(secondYear)
        year1.setNext(year2)
        year2.setPrev(year1)

        self.currentDay = year1.months[0].days[0]
        self.currentWeek = year1.months[0].weeks[0]

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
