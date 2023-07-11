from prettytable import PrettyTable
def select_dish(menu):
    print("Select a dish from the menu:")
    for index, dish in enumerate(menu, start=1):
        print(f"{index}. {dish} - P{menu[dish]}")

    choice = input("Enter the number of the dish (or 'x' to exit): ")
    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(menu):
            dish = list(menu.keys())[choice - 1]
            price = menu[dish]
            quantity = int(input("How many? "))
            return dish, price, quantity
        else:
            print("Invalid choice.")
    elif choice.lower() == "x":
        return "x", 0, 0
    else:
        print("Invalid choice. Try again!")

    return None, 0, 0

def print_receipt(receipt):
    table = PrettyTable(["Dish", "Price", "Quantity"])
    total = 0
    for dish, price, quantity in receipt:
        table.add_row([dish, price, quantity])
        total += price * quantity

    table.add_row(["TOTAL", total, ""])
    print(table)

    amount = int(input("Enter your pay: "))
    change = amount - total
    # issue: create a loop in case the user's input is not sufficient...
    # it will continue asking for right amount
    if change < 0:
        print("Your pay is not sufficient. You can't have the dish!")
    else:
        print(f"Your change is {change}")

def main():
    menu = {
        "Menudo": 60,
        "Adobo": 55,
        "Kaldereta": 50,
        "Munggo": 30,
        "Sinigang": 40,
        "Fillet": 70,
    }
    receipt = []
    while True:
        dish, price, quantity = select_dish(menu)
        if dish == "x":
            break
        elif dish:
            receipt.append((dish, price, quantity))

    print_receipt(receipt)
    print("Thanks! Come Again!")


# Run the main function
if __name__ == "__main__":
    print("------------ WELCOME TO PY-RECEIPT SERVICE ------------")
    main()
