from Calendar import Calendar

testCalendar = Calendar(2016, 2017)
testCalendar.currentDay = testCalendar.getCurrentYear().months[8].days[13]

print (testCalendar.currentDay.weekday + ", " + testCalendar.currentDay.month.name)

for day in testCalendar.getCurrentWeek():
    print (day.date)

print testCalendar.getCurrentMonth()
print testCalendar.getCurrentMonth().weeks[0]
print testCalendar.getCurrentMonth().weeks[0][1]
print testCalendar.getCurrentMonth().weeks[0][1].weekday
newDay = testCalendar.getMonth('august', 2016).getDay(30)
print newDay.date

