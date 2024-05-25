# Exchange Rate Example Program
# import libery to create widget and data Currency
from tkinter import *
from forex_python.converter import CurrencyRates

#create object for currencyrate
currency_rate = CurrencyRates()
currency =currency_rate.get_rates("USD")

#function for list of currency around the world
def getcurrency_list(currency):
    currency_list = ["USD"]
    for key in currency.keys():
        currency_list.append(key)
    return currency_list

#event when leftclick button calculate currency and show the result
def left_click_button(event):
    amount = float(input_box_amount.get())
    first_currency_input = first_currency.get()
    second_currency_input = second_currency.get()
    currency_rate_selected = round(currency_rate.get_rate(first_currency_input, second_currency_input), 2)
    result_amount = f"{round(currency_rate.convert(first_currency_input, second_currency_input, amount), 2):,}"

    label_currency_rate.configure(text="อัตราแลกเปลี่ยน : " + str(currency_rate_selected))
    label_result.configure(text=result_amount)

#list of currency
currency_list = getcurrency_list(currency)              

#GUI 
main_window = Tk()

#header
label_welcome = Label(main_window, text = "Welcome to Currencycoverter Program\n Currency Exchange rate",font=("Helvetica",18))
label_welcome.grid(row=0,columnspan=3)

#list of currency that you can selected
first_currency = StringVar(main_window)
first_currency.set(currency_list[0])  # default value
second_currency = StringVar(main_window)
second_currency.set(currency_list[0])  # default value
dropdown_first_currency = OptionMenu(main_window, first_currency, *currency_list)
dropdown_first_currency.grid(row=2,column=0)
dropdown_second_currency = OptionMenu(main_window, second_currency, *currency_list)
dropdown_second_currency.grid(row=5,column=0)

#label of first currency 
label_currencyrates_first = Label(main_window, text="First currency",font=("Helvetica",14))
label_currencyrates_first.grid(row=2,column=1)

#space to insert number
input_box_amount = Entry(main_window)
input_box_amount.grid(row=4,column=0,columnspan=3)

#label of second currency 
label_currencyrates_second = Label(main_window, text="Second currency",font=("Helvetica",14))
label_currencyrates_second.grid(row=5,column=1)

#label of result
label_result = Label(main_window, text="จำนวนเงิน")
label_result.grid(row=6, columnspan=3)
label_currency_rate = Label(main_window, text="")
label_currency_rate.grid(row=7, columnspan=3)

#button to calculate
calculated_button = Button(main_window, text = "Exchange!!")
calculated_button.grid(row=9,columnspan=3)
calculated_button.bind("<Button-1>", left_click_button)
main_window.mainloop()