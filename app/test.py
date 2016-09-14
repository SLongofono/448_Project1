import Calendar

testCalendar = Calendar.Calendar(2016, 2017)
testCalendar.currentDay = testCalendar.getCurrentYear().months[8].days[13]

print (testCalendar.currentDay.weekday + ", " + testCalendar.currentDay.month.name)

for day in testCalendar.getCurrentWeek():
    print (day.date)
