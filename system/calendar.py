import calendar
print("---Calendar---")


# create a prompt that take users input of year and month
# displaying the specific of month of a year
while True:
    try:
        year = int(input("Please enter a year: "))
        month = int(input("Please enter a month: "))
        print(calendar.month(year, month))
        break
    except ValueError:
        print("Invalid input!")
        continue
    except IndexError:
        print("Invalid input!")
        continue

# displaying the whole calendar of a year

year_calendar = int(input("Enter a year: "))
print(calendar.calendar(year_calendar))