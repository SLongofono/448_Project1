from Year import Year

testYear = Year(2016, 5)
testMonth = testYear.months[8]
testDay = testMonth.days[9]

print (str(testDay.month) + " " + str(testDay.date) + ", " + str(testYear.name) + ' (' + testDay.weekday + ')\n')

for week in testMonth.weeks:
    for day in week:
        print (str(day.month) + " " + str(day.date) + ", " + str(testYear.name) + ' (' + day.weekday + ')')

    print ('')
