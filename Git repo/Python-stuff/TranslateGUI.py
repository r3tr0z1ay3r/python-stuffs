from tkinter import *
from Translator import translate
root = Tk()

root.title("Translator")
root.geometry("600x480")
root.iconbitmap("J:\Downloads\Google-Translate-icon.png")
from_lang = StringVar()
from_lang.set("English")
from_language = ""
to_lang = StringVar()
to_lang.set("English")
to_language = ""
test = StringVar()
text = ""
langs = ["English","Tamil","French","German","Italian","Malay","Persian","Portuguese","Romanian","Russian","Spanish","Tamil","Telugu","Japanese"]

def submit_button():
    translated.delete(0,END)
    text = test.get()
    from_language = from_lang.get()
    to_language = to_lang.get()
    translated_text = translate(text,from_language,to_language)
    print(translated_text)
    translated.insert(0,translated_text)
#OTHER WIDGETS

texts = Entry(root,width=50,textvariable=test).grid(row=0,column=1)
translated = Entry(root,width=50)
translated.grid(row=4,column=1)
label1 = Label(root,text = "Enter text to translate here:").grid(row=0,column=0)
label2 = Label(root,text="Translated text will be:").grid(row=4,column=0)
button_submit = Button(root,text="Submit",width=5,command=submit_button).grid(row=0,column=2)

#RADIO BUTTON DEFENITIONS
text_from = Label(root,text="From").grid(row=1,column=1)
drop1_from = OptionMenu(root,from_lang,*langs).grid(row=2,column=1)
drop2_to = OptionMenu(root,to_lang,*langs).grid(row=2,column=2)


text_to = Label(root,text="To").grid(row=1,column=2)



root.mainloop()