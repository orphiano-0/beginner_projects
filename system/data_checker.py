# importing modules for valid pattern
def adding_data():
    database = open("../files/database.txt", "a")
    database.write("Name: " + name + "\nEmail: " + email + "\nContact: " + contact)
    database.write("\n----------------------------------\n")
    database.close()
def check():
    value = input("Type the value you want to check: ")
    with open("../files/database.txt", "r") as file:
        for line in file:
            if value in line:
                print("Found it!")
                break
        # if the value does not exist, it won't return anything...
        # still figuring out the logic...
def choose():
    choose = input("Wanna check if the value exists in database? [Y, N] ")
    choose.lower()
    if choose == "y":
        check()
    else:
        print("aight!")
print("----- Welcome to Data Checker! -----")
name = input("Enter your name: ")
email = input("Enter your email: ")
contact = input("Enter your contact: ")
print("-------------------------")
adding_data()
choose()


