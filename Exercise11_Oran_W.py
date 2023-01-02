num1 = int(input("Number : "))
for x in range(num1):
    text = "*"*(x*2+1)  
    print((num1-(x+1))*" " , text)