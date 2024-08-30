import tkinter
from tkinter import END

window = tkinter.Tk()
window.title("Tkinter module ")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)
#Label

my_label = tkinter.Label(text="I am a Label.", font=("Arial", 18))
my_label.grid(row=0, column=0)
my_label["text"] = "My text"


#Button
def button_clicked():
    # my_label.config(text="Button got clicked.")
    my_text = input.get()
    my_label.config(text=my_text)


button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)


#Entry
input = tkinter.Entry(width=20)
input.grid(row=3, column=4)


button1 = tkinter.Button(text="Submit")
button1.grid(row=0, column=3)

window.mainloop()
