#ส่วนการเข้าล็อกอิน
Username = input("username :")
Password = input("password :")
#check condition
if Username == "admin" and Password == "1234":
    print("completed")
    print("Welcome to Gameshop")
    print("-------------------")
    print("1.God of War(Key) : 1590 Baht")
    print("2.The last of us(Key) : 1350 Baht")
    print("3.Joystick(PS5) : 2000 Baht")
    print("-------------------")
    num1 = int(input(">"))
    print("How many you want :")
    num2 = int(input(">"))
    if num1 == 1:
        result = 1590*num2
        print("Price = ", result)
    elif num1 == 2:
        result = 1350*num2
        print("Price = ", result)
    elif num1 == 3:
        result = 2000*num2
        print("Price = ", result)
print("Thank you for shopping")