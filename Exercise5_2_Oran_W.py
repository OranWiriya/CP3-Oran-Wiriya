#กำหนดตัวแปรในการเก็บข้อมูลจากผู้ใช้
velocity = 0
distance = int(input("Distance (m) : "))
time = int(input("Time (second) : "))
#คำนวณค่าความเร็วที่ได้เบื้องหลัง
velocity = distance/time
#แสดงค่าที่ได้
print(velocity, "m/s")