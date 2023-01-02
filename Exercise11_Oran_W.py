num1 = int(input("Number : "))
for x in range(num1):
    text = ""
    for y in range(x+1):
        text += "*"  
    print((num1-(x+1))*" " , text)