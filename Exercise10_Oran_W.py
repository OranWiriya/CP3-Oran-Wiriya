result = ""
start = int(input("start : "))
step =  int(input("step : "))

for i in range(5):
    result+=str(start+step*i+1)
print(result)