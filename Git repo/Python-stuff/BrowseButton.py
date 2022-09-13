# Import the required Libraries
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile

# Create an instance of tkinter frame
win = Tk()

# Set the geometry of tkinter frame
win.geometry("700x350")

def open_file():
    file = filedialog.askopenfile(mode='r', filetypes=[('Python Files', '*.py')])
    if file:
        content = file.read()
        file.close()
    newwin = Toplevel(win,background="Black")
    newwin.title("File content")
    Label1 = Label(newwin,text=content).grid(column=0,row=0)
# Add a Label widget
label = Label(win, text="Click the Button to browse the Files", font=('Georgia 13'))
label.pack(pady=10)

# Create a Button
ttk.Button(win, text="Browse", command=open_file).pack(pady=20)

win.mainloop()