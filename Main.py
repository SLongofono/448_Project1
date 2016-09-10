from Year import Year
from Day import Day

testYear = Year(2016, 5)
testDay = testYear.months[8].days[9]
print (str(testDay.month) + "/" + str(testDay.date) + ", " + testDay.weekday)
