from data_checker import adding_data
add_data = adding_data()
class Data:
    def __int__(self, name, email, contact):
        self.name = name
        self.email = email
        self.contact = contact

    def to_store(self):
        self.name = input("Enter your name: ")
        self.email = input("Enter your email: ")
        self.contact = input("Enter your contact number: ")
        print("Name: " + self.name + "\nEmail: " + self.email + "\nContact: " + self.contact)
        print("---------------------------------")