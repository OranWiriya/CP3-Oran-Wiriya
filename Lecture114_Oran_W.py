# Exchange Rate Example Program
# import libery to create widget and data Currency
from tkinter import *
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter

main_window = Tk()
label_welcome = Label(main_window, text = "Welcome to Currencycoverter Program\n Please select your program",font=("Helvetica",18))
label_welcome.grid(row=0,columnspan=3)
label_currencyrates = Label(main_window, text="1.Currency Exchangerate",font=("Helvetica",14))
label_currencyrates.grid(row=2,columnspan=3)
label_currencyrates = Label(main_window, text="2.Bitcoin Exchangerate",font=("Helvetica",14))
label_currencyrates.grid(row=3,columnspan=3)
text_box_selected = Entry(main_window)
text_box_selected.grid(row=4,column=0,columnspan=3)

main_window.mainloop()