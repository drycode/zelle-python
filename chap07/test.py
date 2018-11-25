dateStr = '09/24/1956'

monthStr, dayStr, yearStr = dateStr.split("/")
month = int(monthStr)
day = int(dayStr)
year = int(yearStr)

print(month, day, year)
