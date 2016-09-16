## @file Calendar.py
# @author Grant
# @brief Your description here
#
# @details Your details here
#
#

from Year import Year

## @class Calendar
# @author
# @brief
#
# @details
#
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
        if self.currentDay.month.year == self.year1.name:
            return self.year1
        return self.year2

    def getMonth(self, monthName, yearName):
        if self.year1.name == yearName:
            y = self.year1
        elif self.year2.name == yearName:
            y = self.year2
        for month in y.months:
            if month.name == monthName:
                return month

        return None
