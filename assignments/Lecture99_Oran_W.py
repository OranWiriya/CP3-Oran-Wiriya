from tkinter import *

def CalculateBMI():
    height = float(HeightInput.get())
    weight = float(WeightInput.get())
    BMI = weight / ((height / 100) ** 2)
    BMI = round(BMI, 2)
    if BMI < 19.00:
        labelResult.configure(text="อยู่ในเกณฑ์น้ำหนักน้อยผิดปกติ")
    elif BMI < 24:
        labelResult.configure(text ="น้ำหนักเกณฑ์มาตราฐาน")
    elif BMI < 25:
        labelResult.configure(text="น้ำหนักเกินเกณฑ์")
    elif BMI < 30:
        labelResult.configure(text="น้ำหนักอยู่ในเกณฑ์เกิดโรคอ้วน")

MainWindow = Tk()
labelHeight = Label(MainWindow, text= 'ส่วนสูง(cm.)').grid(row=0, column=0)
HeightInput = Entry(MainWindow)
HeightInput.grid(row=0, column=1)
labelWeight = Label(MainWindow, text= 'น้ำหนัก(kg.)').grid(row=1, column=0)
WeightInput = Entry(MainWindow)
WeightInput.grid(row=1, column=1)
calculateButton = Button(MainWindow, text="Calculate BMI", command=CalculateBMI)
calculateButton.bind("<Button-1>", CalculateBMI)
calculateButton.grid(row=2, column=0)
labelResult = Label(MainWindow, text="ผลลัพธ์")
labelResult.grid(row=2, column=1)
MainWindow.mainloop()