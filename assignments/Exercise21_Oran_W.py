#import libery to create widget 
from tkinter import *

#function calculate BMI and return text result
def leftClickbutton(event):
    result = 0
    W = float(textBoxWeight.get())
    H = float(textBoxHeight.get())
    result = (W/((H/100)**2))
    if (result < 18.5 ):
        labelResult.configure(text ="ผอมเกินไป")
        labelResult.grid(row=2,column=1)
    elif (result <= 22.9):
        labelResult.configure(text ="น้ำหนักปกติ เหมาะสม")
        labelResult.grid(row=2,column=1)
    elif (result <= 24.9):
        labelResult.configure(text ="น้ำหนักเกิน")
        labelResult.grid(row=2,column=1)
    elif (result <= 29.9):
        labelResult.configure(text ="อ้วน")
        labelResult.grid(row=2,column=1)
    elif (result >  29.9):
        labelResult.configure(text ="อ้วนมาก")
        labelResult.grid(row=2,column=1)

#start program and added data what we want
MainWindow = Tk()
labelHeight = Label(MainWindow, text = "ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(MainWindow, text = "น้ำหนัก (kg.)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
CalculateButton = Button(MainWindow, text = "คำนวณ")
CalculateButton.bind("<Button-1>", leftClickbutton)
CalculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text = "ผลลัพธ์")
labelResult.grid(row=2,column=1)

MainWindow.mainloop()