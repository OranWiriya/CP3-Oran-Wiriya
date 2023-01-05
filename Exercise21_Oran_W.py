from tkinter import *
import math

def leftClickbutton(event):
    result = 0
    W = float(textBoxWeight.get())
    H = float(textBoxHeight.get())
    result = labelResult.configure(text = (W/((H/100)**2)))
    if (result < 18.5 ):
        labelResultText = Label(MainWindow,text = "ผอมเกินไป")
        labelResultText.grid(row=2,column=2)
    elif (result <= 22.9):
        labelResultText = Label(MainWindow,text = "น้ำหนักปกติ เหมาะสม")
        labelResultText.grid(row=2,column=2)
    elif (result <= 24.9):
        labelResultText = Label(MainWindow,text = "น้ำหนักเกิน")
        labelResultText.grid(row=2,column=2)
    elif (result <= 29.9):
        labelResultText = Label(MainWindow,text = "อ้วน")
        labelResultText.grid(row=2,column=2)
    elif (result > 22.9):
        labelResultText = Label(MainWindow,text = "อ้วนมาก")
        labelResultText.grid(row=2,column=2)

MainWindow = Tk()
labelHeight = Label(MainWindow, text = "ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(MainWindow, text = "น้ำหนัก (Kg.)")
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
CalculateButton = Button(MainWindow, text = "คำนวณ")
CalculateButton.bind("<Button-1>", leftClickbutton)
CalculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text = "ผลลัพธ์")
labelResult.grid(row=2,column=1)

MainWindow.mainloop()