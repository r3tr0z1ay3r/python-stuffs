#CURRENCY CONVERTER GUI

from tkinter import *
from function import handle_value_error

root = Tk()
root.title("Currency Converter")
root.geometry("800x480")

avail_currencies = ["USD","INR","EURO","YEN"]

#Variables to recieve input
from_options = StringVar()
from_options.set("USD")
to_options = StringVar()
to_options.set("USD")
fromMoney = StringVar()
fromMoney.set(0)
toMoney = IntVar()

#Defs of functions
#Def od usd fns
def usdToInr(usd):
    inr = 74.38
    usd = float(usd)
    print(usd)
    converted = float(usd*inr)
    print(converted)
    return(round(converted,2))

def usdtoeuro(usd):
    euro = 0.86
    converted = float(usd*euro)
    return(round(converted,2))

def usdtoyen(usd):
    yen = 109.80
    converted = float(yen*usd)
    return(round(converted,3))

#Defs of inr fns
def InrToUsd(usd):
    inr = 74.38
    usd = float(usd)
    print(usd)
    converted = float(usd/inr)
    print(converted)
    return(round(converted,3))

def inrtoeuro(inr):
    euro = 86.92
    converted = float(inr/euro)
    return(round(converted,3))

def inrtoyen(inr):
    yen = 0.68
    converted = float(inr*yen)
    return(round(converted,3))

#Defs of euro fns
def eurotousd(euro):
    usd = 0.86
    converted = float(usd*euro)
    return(round(converted,3))

def eurotoinr(euro):
    inr = 0.012
    converted = float(inr*euro)
    return(round(converted,3))

def eurotoyen(euro):
    yen = 0.0078
    converted = float(yen*euro)
    return(round(converted,4))

#Defs of yen fns
def yentoinr(yen):
    inr = 1.48
    converted = float(inr*yen)
    return(round(converted,3))

def yentousd(yen):
    usd = 109.79
    converted = float(yen*usd)
    return(round(converted,3))

def yentoeuro(yen):
    euro = 128.29
    converted = float(euro*yen)
    return(round(converted,3))

def submitBtn():
    global from_options
    global to_options
    global to_money
    global fromMoney
    global toMoney
    
    FromMoney = float(fromMoney.get())
    to_money.delete(0,END)
    to_convert_from = from_options.get()
    to_convert_to = to_options.get()
    
    #All from USD to Other stuff
    if to_convert_from == "USD" and to_convert_to == "USD":
        to_money.insert(0,FromMoney)
    if to_convert_from == "USD" and to_convert_to == "INR":
        converted = str(usdToInr(FromMoney))
        to_money.insert(0,converted)
    if to_convert_from == "USD" and to_convert_to == "EURO":
        converted = str(usdtoeuro(FromMoney))
        to_money.insert(0,converted)
    if to_convert_from == "USD" and to_convert_to == "YEN":
        converted = str(usdtoyen(FromMoney))
        to_money.insert(0,converted)
    #All from INR to other stuff
    if to_convert_from == "INR" and to_convert_to == "INR":
        to_money.insert(0,FromMoney)
    if to_convert_from == "INR" and to_convert_to == "USD":
        converted = str(InrToUsd(FromMoney))
        to_money.insert(0,converted)
    if to_convert_from == "INR" and to_convert_to == "EURO":
        converted = str(inrtoeuro(FromMoney))
        to_money.insert(0,converted)
    if to_convert_from == "INR" and to_convert_to == "YEN":
        converted = str(inrtoyen(FromMoney))
        to_money.insert(0,converted)
    
    #All from EURO to other stuff
    if to_convert_from == "EURO" and to_convert_to == "EURO":
        to_money.insert(0,FromMoney)
    if to_convert_from == "EURO" and to_convert_to == "USD":
        converted = str(eurotousd(FromMoney))
        to_money.insert(0,converted)
    if to_convert_from == "EURO" and to_convert_to == "INR":
        converted = str(eurotoinr(FromMoney))
        to_money.insert(0,converted)
    if to_convert_from == "EURO" and to_convert_to == "YEN":
        converted = str(eurotoinr(FromMoney))
        to_money.insert(0,converted)
    #All from YEN to other stuff
    if to_convert_from == "YEN" and to_convert_to == "YEN":
        to_money.insert(0,FromMoney)
    if to_convert_from == "YEN" and to_convert_to == "USD":
        converted = str(yentousd(FromMoney))
        to_money.insert(0,converted)
    if to_convert_from == "YEN" and to_convert_to == "EURO":
        converted = str(yentoeuro(FromMoney))
        to_money.insert(0,converted)
    if to_convert_from == "YEN" and to_convert_to == "INR":
        converted = str(yentoinr(FromMoney))
        to_money.insert(0,converted)
#Defs of buttons and labels

title = Label(root,text="CURRENCY CONVERTER",font=("Helvetica",25))
title.grid(row=1,column=2,sticky="N")
empty = " "

#Empty labels to lower option
empty_top1 = Label(root,text=(empty*50))
empty_top1.grid(row=1,column=1)
empty1 = Label(root,text="             ")
empty1.grid(row=2,column=0)
empty2 = Label(root,text="             ")
empty2.grid(row=3,column=0)
empty3 = Label(root,text="             ")
empty3.grid(row=4,column=0)
empty4 = Label(root,text="             ")
empty4.grid(row=5,column=0)

from_label = Label(root,text="FROM CURRENCY",font="Helvetica")
from_label.grid(row=6,column=1)

to_label = Label(root,text="TO CURRENCY",font="Helvetica")
to_label.grid(row=6,column=2)

from_currency = OptionMenu(root,from_options,*avail_currencies)
from_currency.grid(row=7,column=1,padx=30,pady=20)

to_currency = OptionMenu(root,to_options,*avail_currencies)
to_currency.grid(row=7,column=2,padx=30,pady=20)

submit_btn = Button(root,text="Convert",borderwidth=5,command=submitBtn)
submit_btn.grid(row=9,column=3,padx=20,pady=20)

from_money_label = Label(root,text="Enter From currency: ",font="Helvetica")
from_money_label.grid(row=8,column=1)
to_money_label = Label(root,text=(f"In {to_options.get()} Currency: "),font="Helvetica")
to_money_label.grid(row=8,column=2)

from_money = Entry(root,textvariable=fromMoney,borderwidth=5)
from_money.grid(row=9,column=1,padx=30,pady=30)
to_money = Entry(root,textvariable=toMoney,borderwidth=5)
to_money.grid(row=9,column=2,padx=30,pady=30)

root.mainloop()