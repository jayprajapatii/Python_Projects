from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator


def translate():
    try:
        src = comb_sor.get()
        dest = comb_dest.get()
        text = sor_txt.get(1.0, END).strip()

        if not text:
            return

        translated = GoogleTranslator(source=src, target=dest).translate(text)

        dest_txt.delete(1.0, END)
        dest_txt.insert(END, translated)

    except Exception as e:
        dest_txt.delete(1.0, END)
        dest_txt.insert(END, str(e))


root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='Red')

Label(root, text="Translator",
      font=("Arial", 40, "bold"),
      bg='Red', fg='White').place(x=100, y=40, width=300)

Label(root, text="Source Text",
      font=("Arial", 20, "bold"),
      bg='Red', fg='White').place(x=100, y=100, width=300)

sor_txt = Text(root, font=("Arial", 20), wrap=WORD)
sor_txt.place(x=10, y=130, height=150, width=480)

languages = ["en", "hi", "gu", "fr", "de"]

comb_sor = ttk.Combobox(root, values=languages, font=("Arial", 15))
comb_sor.place(x=10, y=300, height=40, width=150)
comb_sor.set("en")

Button(root, text="Translate",
       font=("Arial", 15, "bold"),
       bg='White', fg='Red',
       command=translate).place(x=170, y=300, height=40, width=150)

comb_dest = ttk.Combobox(root, values=languages, font=("Arial", 15))
comb_dest.place(x=330, y=300, height=40, width=150)
comb_dest.set("gu")

Label(root, text="Destination Text",
      font=("Arial", 20, "bold"),
      bg='Red', fg='White').place(x=100, y=360, width=300)

dest_txt = Text(root, font=("Arial", 20), wrap=WORD)
dest_txt.place(x=10, y=400, height=150, width=480)

root.mainloop()
