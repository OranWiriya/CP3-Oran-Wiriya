from tkinter import *
import math

def leftClickbutton(event):
    W = float(textBoxWeight.get())
    H = float(textBoxHeight.get())
    labelResult.configure(text = (W/((H/100)**2)) )

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