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
    def __init__ (self,firstYear,secondYear, fileName):
        self.year1 = Year(firstYear)
        self.year2 = Year(secondYear)
        self.year1.setNext(self.year2)
        self.year2.setPrev(self.year1)

        self.fileName = fileName

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

    def getYear(self, yearName):
        if self.year1.name == yearName:
            return self.year1
        elif self.year2.name == yearName:
            return self.year2

        return None

    def getMonth(self, monthName, yearName):
        if self.year1.name == yearName:
            y = self.year1
        elif self.year2.name == yearName:
            y = self.year2

        if(y != None):
            return y.getMonth(monthName)
        else:
            return None

    def load(self):
        try:
            log = open(self.fileName)
        except IOError:
            return

        lines = log.readlines()

        newDay = True
        day = None
        for line in lines:
            if line == ';\n':
                newDay = True
            elif newDay:
                words = line.split()
                day = self.getYear(int(words[0])).months[int(words[1])].days[int(words[2])]
                newDay = False
            else:
                day.addDetail(line.rstrip('\n'))



    def save(self):
        log = open(self.fileName, 'w+')

        m = 0
        for month in self.year1.months:
            d = 0
            for day in month.days:
                if(len(day.details) != 0):
                    log.write(str(self.year1.name) + ' ' + str(m) + ' ' + str(d))
                    for detail in day.details:
                        log.write('\n' + detail)
                    log.write('\n;\n')

                d += 1
            m += 1

        m = 0
        for month in self.year2.months:
            d = 0
            for day in month.days:
                if(len(day.details) != 0):
                    log.write(str(self.year2.name) + ' ' + str(m) + ' ' + str(d))
                    for detail in day.details:
                        log.write('\n' + detail)
                    log.write('\n;\n')

                d += 1
            m += 1

        log.close()
