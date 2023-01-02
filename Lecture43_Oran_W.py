correctNumber = 17
while True:
    userGuess = int(input("Please guess a number : "))
    if userGuess > correctNumber:
        print("Too Large")
    elif userGuess < correctNumber:
        print("Too Small")
    elif userGuess == correctNumber:
        print("Congrest It Correct !!")
        break
