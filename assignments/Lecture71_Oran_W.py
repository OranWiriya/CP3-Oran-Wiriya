# กำหนดค่า List ต่างๆที่จะใช้ 
manuList = []
priceList = []

# กำหนด Function ที่จะใช้ 
def ShowBill():
    TotalPrice = 0
    print("My Foods".center(20,"-"))
    for i in range(len(manuList)):
        print(manuList[i],priceList[i])
        TotalPrice += int(priceList[i])
    print("total : %d" %(TotalPrice))

# กำหนด Loop ที่ผู้ใช้กรอกค่าเมนู, ราคาลงไป
while True:
    manuName = input("Please Enter Manu : ")
    if manuName.lower() == "exit":
        break
    else:
        price = input("Price : ")
        manuList.append(manuName)
        priceList.append(price)
        
# แสดงเมนูต่างๆพร้อมราคา รวมไปถึงคำนวณราคาทั้งหมด จาก Function
ShowBill()