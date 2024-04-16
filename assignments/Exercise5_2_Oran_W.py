velocity = 0
distance = int(input("Distance (m) : "))
if(distance < 1): print('Distance cannot be less than 1 meter') 
else :
    time = int(input("Time (second) : "))
    if(time < 1): print('Time cannot be less than 1 second')
    else :
        velocity = distance/time
        print(velocity, "m/s")