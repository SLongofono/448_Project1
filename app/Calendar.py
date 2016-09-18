## @file Calendar.py
# @author Grant Jurgensen
# @brief Holds two years, and keeps track of the currently selected day
#

from Year import Year

## @class Calendar
# @author Grant Jurgensen
# @brief Holds two years, and keeps track of the currently selected day
#
# @details
#
# Because there are multiple years to keep track of, this class acts as a container
# of all the years (and therefore acts as a bridge to the associated months/weeks/days).
# It is through this class that you can keep track of and access all your calendar related
# objects, and select a current day on which to focus.
#
class Calendar():

    ## @fn __init__
    # @brief Initializes a Calendar object
    # @param [in] firstYear An integer value of the first year to be created
    # @param [in] secondYear An integer value of the second year to be created
    # @param [in] fileName The file name which will be used to save and load information
    #                      in order to rebuild the Calendar object in the future
    # @param [out] return The initialized Calendar object
    #
    # @details
    #
    # Initializes a Calendar object. Initializes two Year objects based on the firstYear
    # and secondYear arguments and stores the fileName which will be used to save and
    # load information from a local file.
    #
    def __init__ (self, firstYear, secondYear, fileName):
        self.year1 = Year(firstYear)
        self.year2 = Year(secondYear)
        self.year1.setNext(self.year2)
        self.year2.setPrev(self.year1)

        self.fileName = fileName

        self.currentDay = self.year1.months[0].days[0]

    ## @fn getCurrentDay
    # @brief Gets the currentDay
    # @param [out] return The currentDay member variable
    #
    def getCurrentDay(self):
        return self.currentDay

    ## @fn getCurrentWeek
    # @brief Gets the week associated with the current day
    # @param [out] return A list of days ordered as a consecutive week (sunday-saturday),
    #                     with currentDay being one of the days in the list.
    #
    def getCurrentWeek(self):
        for week in self.currentDay.month.weeks:
            for day in week:
                if day == self.currentDay:
                    return week

    ## @fn getCurrentMonth
    # @brief Gets the month which the currentDay belongs to
    # @param [out] return the month object which owns currentDay
    #
    def getCurrentMonth(self):
        return self.currentDay.month

    ## @fn getCurrentYear
    # @brief Gets the year which the currentDay belongs to
    # @param [out] return the year object which owns currentDay
    #
    def getCurrentYear(self):
        if self.currentDay.month.year == self.year1.name:
            return self.year1
        return self.year2

    ## @fn getYear
    # @brief Gets a year based on the integer value
    # @param [in] yearName An integer value of the year you are looking for
    # @param [out] return The year object associated with the integer value if one exists
    #
    def getYear(self, yearName):
        if self.year1.name == yearName:
            return self.year1
        elif self.year2.name == yearName:
            return self.year2

        return None

    ## @fn getYear
    # @brief Gets a month based on the integer value for the year and string of the month name
    # @param [in] monthName A string value of the month name for the month you are looking for
    # @param [in] yearName An integer value of the year you are looking for
    # @param [out] return The month object associated with monthName and yearName
    #
    def getMonth(self, monthName, yearName):
        if self.year1.name == yearName:
            y = self.year1
        elif self.year2.name == yearName:
            y = self.year2

        if(y != None):
            return y.getMonth(monthName)
        else:
            return None

    ## @fn load
    # @brief reads through a file, interpets the data, and edits it own contents to match
    #
    # @details
    #
    # Trys to open the file. If it succeeds, it proceeds to read through the textfile,
    # look for day data and details for that day, and as it recognises this data,
    # add the details to the days it currently possesses.
    #
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

    ## @fn save
    # @brief creates/overwrites a file and saves the details of its days
    #
    # @details
    #
    # Creates a new file or overwrites an existing file. It then scans through its owns
    # days, and for each day with at least one detail, logs information about the day
    # and its details in order to replicate the data in the future.
    #
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
