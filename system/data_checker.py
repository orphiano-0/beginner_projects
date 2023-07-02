def adding_data():
    # adding value in the database base on input
    database = open("../files/database.txt", "a")
    # writing the inputted value in this format
    database.write("Name: " + name + "\nEmail: " + email + "\nContact: " + contact)
    database.write("\n----------------------------------\n")
    database.close()
def check():
    #checking if the value exists in the file
    value = input("Type the value you want to check: ")
    with open("../files/database.txt", "r") as file:
        # read all the contents of the file
        check = file.read()
        # check if the value is present in a file
        if value in check:
            print("Found it!")
        else:
            print("The value does not exist in database.")

def choose():
    choose = input("Wanna check if the value exists in database? [Y, N] ")
    # to accept both upper and lower case value
    choose.lower()
    if choose == "y":
        check()
    else:
        print("Thank you!")

# first interaction
print("----- Welcome to Data Checker! -----")
name = input("Enter your name: ")
email = input("Enter your email: ")
contact = input("Enter your contact: ")
print("-------------------------")
adding_data()
choose()


