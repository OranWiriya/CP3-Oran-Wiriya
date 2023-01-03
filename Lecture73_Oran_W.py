# กำหนดค่า List ต่างๆที่จะใช้ 
Systemlist = {"ข้าวมันไก่":40, "ข้าวหมกไก่":45, "ข้าวขาหมู":40, "น้ำเปล่า":10}
manuList = []

# กำหนด Function ที่จะใช้ 
def ShowBill():
    TotalPrice = 0
    print("My Foods".center(20,"-"))
    for i in range(len(manuList)):
        print(manuList[i][0],manuList[i][1])
        TotalPrice += int(manuList[i][1])
    print("total : %d" %(TotalPrice))

#ประกาศหัวข้อว่ามีเมนูอะไรบ้าง
print(" Manu ".center(20,"*"))
for i in Systemlist.keys():
    print(i,end=" ")
print(" ")
# กำหนด Loop ที่ผู้ใช้กรอกค่าเมนู, ราคาลงไป
while True:
    manuname = input("Plese enter Manu : ")
    if manuname.lower() == "exit":
        break
    else:
        manuList.append([manuname,Systemlist[manuname]])
        
# แสดงเมนูต่างๆพร้อมราคา รวมไปถึงคำนวณราคาทั้งหมด จาก Function
ShowBill()