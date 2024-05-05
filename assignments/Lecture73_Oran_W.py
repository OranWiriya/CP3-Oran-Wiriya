# กำหนดค่า List ต่างๆที่จะใช้ 
Systemlist = {"ข้าวมันไก่":40, "ข้าวหมกไก่":45, "ข้าวขาหมู":40, "น้ำเปล่า":10}
menuList = []

# กำหนด Function ที่จะใช้ 
def ShowBill():
    TotalPrice = 0
    print("My Foods".center(20,"-"))
    for i in range(len(menuList)):
        print(menuList[i][0],menuList[i][1])
        TotalPrice += int(menuList[i][1])
    print("total : %d" %(TotalPrice))

#ประกาศหัวข้อว่ามีเมนูอะไรบ้าง
print(" Menu ".center(20,"*"))
for i in Systemlist.keys():
    print(i,end=" ")
print(" ")
# กำหนด Loop ที่ผู้ใช้กรอกค่าเมนู, ราคาลงไป
while True:
    menuName = input("Please Enter Menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuList.append([menuName,Systemlist[menuName]])
        
# แสดงเมนูต่างๆพร้อมราคา รวมไปถึงคำนวณราคาทั้งหมด จาก Function
ShowBill()