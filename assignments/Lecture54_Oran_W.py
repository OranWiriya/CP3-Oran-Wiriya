def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():
    userSelected = int(input(">>"))
    return userSelected

def vatProgram():
    totalPrice = int(input("Total Price : "))
    return vatCalculator(totalPrice)

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return print('result: ', result)

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

print("Wlecome to ishop")
if(login()):
    showMenu()
    x = menuSelect()
    if (x == 1):
        vatProgram()
    elif (x == 2):
        priceCalculator()
else:
    print("incorrect")
