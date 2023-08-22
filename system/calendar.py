import calendar
print("---Calendar---")

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