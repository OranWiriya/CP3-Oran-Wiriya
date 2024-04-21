lineNumber = int(input("how many line(s) : "))
for x in range(lineNumber):
    text = "*"*(x*2+1)  
    print((lineNumber-(x+1))*" " , text)