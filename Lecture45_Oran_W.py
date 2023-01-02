inputRound = int(input("Please Enter Number : "))
sum = 0
print(list(inputRound+1))
for x in range(inputRound):
    inputNumber = int(input("x"+x+":"))
    sum += inputNumber
print("summary = ",sum)