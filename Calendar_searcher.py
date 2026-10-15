import calendar

# Ask the user for the full year
y = int(input("Give the year you are interested in (full): "))
year = y

# Ask the user for the month (1-12)
m = int(input("Give the month (1-12): "))
month = m

# Generate the calendar for the selected month and year
x = calendar.month(year, month)

# Display the calendar
print(x)