from tkinter import Tk
import tkinter
from tkinter import ttk

FONT = ("Arial", 20)


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_label.config(text=f"{km}")


window = Tk()
window.title("Miles To Km Converter")
window.minsize(height=300, width=400)
window.config(padx=40, pady=40)

miles_input = ttk.Entry(width=20)
miles_input.grid(row=0, column=2)

miles_label = ttk.Label(text="Miles", font=FONT)
miles_label.grid(row=0, column=3)

label = ttk.Label(text="is equal to", font=FONT)
label.grid(row=1, column=0)

km_label = ttk.Label(text="0", font=FONT)
km_label.grid(row=1, column=2)

km_label1 = ttk.Label(text="Km", font=FONT)
km_label1.grid(row=1, column=3)

button = ttk.Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=2)

window.mainloop()
