from Calendar import Calendar

testCalendar = Calendar(2016, 2017)
testCalendar.currentDay = testCalendar.getCurrentYear().months[8].days[13]

print (testCalendar.currentDay.weekday + ", " + testCalendar.currentDay.month.name)

for day in testCalendar.getCurrentWeek():
    print (day.date)

## Month test

print 'Month details: '
print testCalendar.getCurrentMonth().name, ':'
print 'Number of days: ', len(testCalendar.getCurrentMonth().days)
for i in testCalendar.getCurrentMonth().weeks[0]:
	print i.date, i.weekday
for i in testCalendar.getCurrentMonth().weeks[1]:
	print i.date, i.weekday
for i in testCalendar.getCurrentMonth().weeks[2]:
	print i.date, i.weekday
for i in testCalendar.getCurrentMonth().weeks[3]:
	print i.date, i.weekday
for i in testCalendar.getCurrentMonth().weeks[4]:
	print i.date, i.weekday
for i in testCalendar.getCurrentMonth().weeks[5]:
	print i.date, i.weekday

newDay = testCalendar.getMonth('august', 2016).getDay(30)
print newDay.date, newDay.weekday
print '-------------------------------------------------------'


for i in testCalendar.year1.months:
	print i.name, '-- num days: ', len(i.days), '\tWeek lengths: ', len(i.weeks[0]), len(i.weeks[2]), len(i.weeks[3]), len(i.weeks[4]), len(i.weeks[5])



## Week test

theWeek = testCalendar.getCurrentWeek()
theWeek2 = testCalendar.currentWeek
print theWeek == theWeek2
for day in theWeek:
	print day.date, day.weekday

for day in theWeek2:
	print day.date, day.weekday

