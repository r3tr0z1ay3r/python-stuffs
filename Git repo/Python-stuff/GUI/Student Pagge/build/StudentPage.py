
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
from re import X

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Y, OptionMenu, Tk, Canvas, Entry, Text, Button, PhotoImage ,CENTER,StringVar


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def button1_press():
    chosen = option.get()
    print(chosen)
    

window2 = Tk()

window2.title("Student Page")
window2.geometry("800x600")
window2.configure(bg = "#666666")


canvas = Canvas(
    window2,
    bg = "#666666",
    height = 600,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    51.0,
    35.0,
    anchor="nw",
    text="Student Login",
    fill="#FFFFFF",
    font=("Inter Bold", 36 * -1)
)

canvas.create_text(
    145.0,
    146.0,
    anchor="nw",
    text="Student Name:\n",
    fill="#FFFFFF",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    177.0,
    202.0,
    anchor="nw",
    text="Standard:",
    fill="#FFFFFF",
    font=("Inter Bold", 20 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    463.5,
    160.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0
)
entry_1.place(
    x=341.0,
    y=146.0,
    width=245.0,
    height=27.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    463.5,
    210.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0
)
entry_2.place(
    x=341.0,
    y=196.0,
    width=245.0,
    height=27.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))

#Button 1 is submit button
button_1 = Button(  
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: button1_press(),
    relief="flat"
)
button_1.place(
    x=574.0,
    y=265.0,
    width=119.0,
    height=35.0
)

canvas.create_text(
    177.0,
    268.0,
    anchor="nw",
    text="Select Grade Sheet:\n",
    fill="#FFFFFF",
    font=("Inter Bold", 20 * -1)
)

all = ["QUARTELY","HALF-YEARLY","FINALS"]

option = StringVar(window2)
option.set("Select an option")
drop = OptionMenu(window2,option,*all).place(x=475.0,y=265.0,anchor = CENTER)


window2.resizable(False, False)
window2.mainloop()
