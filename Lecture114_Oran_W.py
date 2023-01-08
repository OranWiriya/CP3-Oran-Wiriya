# Exchange Rate Example Program
# import libery to create widget and data Currency
from tkinter import *
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter


def left_click_button(event):
    if(text_box_selected == 1):
        label_prefercurrency  = Label(main_window, text = "select first currency and second currency",font=("Helvetica",14))
        label_prefercurrency.grid(row=5,columnspan=3)
        text_box_selected_2 = Entry(main_window)
        text_box_selected_2.grid(row=6,columnspan=3)
        text_box_selected_3 = Entry(main_window)
        text_box_selected_3.grid(row=7,columnspan=3)
        result = currency_rate.get_rate(text_box_selected_2,text_box_selected_3)
        label_result.configure(text = result)
        label_result.grid(row=8,columnspan=3)
        reset = ""
        reset_button = Button(main_window,text = "reset",font=("Helvetica",14))
        reset_button.grid(row=9,columnspan=3)
        reset_button.bind("<Button-1>",reset = "0")
        if(reset == "0"):
            text_box_selected_2.destroy()
            text_box_selected_3.destroy()
            label_result.destroy()
            reset_button.destroy()
            return
        

currency_rate = CurrencyRates()
bitcoin_rate = BtcConverter()
main_window = Tk()
label_welcome = Label(main_window, text = "Welcome to Currencycoverter Program\n Please select your program",font=("Helvetica",18))
label_welcome.grid(row=0,columnspan=3)
label_currencyrates = Label(main_window, text="1.Currency Exchangerate",font=("Helvetica",14))
label_currencyrates.grid(row=2,columnspan=3)
label_currencyrates = Label(main_window, text="2.Bitcoin Exchangerate",font=("Helvetica",14))
label_currencyrates.grid(row=3,columnspan=3)
text_box_selected = Entry(main_window)
text_box_selected.grid(row=4,column=0,columnspan=3)
calculate_button = Button(main_window, text = "select")
calculate_button.bind("<Button-1>", left_click_button)
label_result = Label(main_window,text="")
main_window.mainloop()