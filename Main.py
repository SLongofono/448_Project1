from Year import Year
from Day import Day

testYear = Year(2016, 5)
testMonth = testYear.months[8]
testDay = testMonth.days[9]

print (str(testDay.month) + "/" + str(testDay.date) + ", " + testDay.weekday)

for week in testMonth.weeks:
    for day in week:
        print (str(day.month) + "/" + str(day.date) + ", " + day.weekday)

    print ('\n')
