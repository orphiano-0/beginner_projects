from prettytable import PrettyTable
# creating lists of menu
def lists():
    my_lists = PrettyTable(["Menu", "Price"])
    my_lists.add_row(["Menudo", "P" + str(60)])
    my_lists.add_row(["Adobo", "P" + str(55)])
    my_lists.add_row(["Kaldereta", "P" + str(50)])
    my_lists.add_row(["Munggo", "P" + str(30)])
    my_lists.add_row(["Sinigang", "P" + str(40)])
    my_lists.add_row(["Fillet", "P" + str(70)])
    my_lists.add_row(["Exit", "Press X"])
    print(my_lists)

# welcome message
print("------------ WELCOME TO PY-RECEIPT SERVICE ------------")
table = PrettyTable(["Dish", "Price", "Quantity"])
total = 0
lists()
try:
    while(1):
        # try-except block for unseen variables
        try:
            name_dish = input("Enter a dish: ")
            # exit condition if the user press 'x'
            if name_dish != "x":
                price = int(input("Enter a price: "))
                quantity = int(input("How many? "))

                # store all value in total
                total += price * quantity
                table.add_row([name_dish, price, quantity])
                quantity += quantity
                continue
            elif name_dish == "x":
                break
        except ValueError as error:
            print(error)

    # tables with new calculated values
    table.add_row(["TOTAL", total, quantity])
    print(table)
except NameError as nerror:
    print(nerror)
# end program
print("Thanks! Come Again!")
