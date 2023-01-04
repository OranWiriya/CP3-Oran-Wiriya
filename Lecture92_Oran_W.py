from  tkinter import *

def sayHelloWorld():
    print("Hello World")

MainWindow = Tk()
button = Button(MainWindow,text="Click me",command= sayHelloWorld)
button.place(x = 50, y = 20)
MainWindow.mainloop()