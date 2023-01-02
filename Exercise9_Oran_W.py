Username = " "
Password = " "
while Username != "admin" or Password != "1234":
    Username = input("username :")
    Password = input("password :")
    if Username != "admin" or Password != "1234":
        print("Incorrect Try again")
    elif Username == "admin" and Password == "1234":
        print("Correct Done")
        break