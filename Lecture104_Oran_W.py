class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to " +self.name+ " " +self.lastName + "'s cart")

customer1 = Customer()
customer1.name = "Bob"
customer1.lastName = "Baby"
customer1.age = 8

customer2 = Customer()
customer2.name = "Angy"
customer2.lastName = "Angle"
customer2.age = 15

customer3 = Customer()
customer3.name = "Toy"
customer3.lastName = "Rector"
customer3.age = 1

customer1.addCart()
customer2.addCart()
customer3.addCart()