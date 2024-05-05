# กำหนดค่า List ต่างๆที่จะใช้ 
menuList = []
priceList = []

# กำหนด Function ที่จะใช้ 
def ShowBill():
    TotalPrice = 0
    print("My Foods".center(20,"-"))
    for i in range(len(menuList)):
        print(menuList[i],priceList[i])
        TotalPrice += int(priceList[i])
    print("total : %d" %(TotalPrice))

# กำหนด Loop ที่ผู้ใช้กรอกค่าเมนู, ราคาลงไป
while True:
    menuName = input("Please Enter Menu : ")
    if menuName.lower() == "exit":
        break
    else:
        price = input("Price : ")
        menuList.append(menuName)
        priceList.append(price)
        
# แสดงเมนูต่างๆพร้อมราคา รวมไปถึงคำนวณราคาทั้งหมด จาก Function
ShowBill()