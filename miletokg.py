from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=300, height=250)
window.config(padx=20, pady=20)

def calc():
    mile=float(mile_entry.get())
    km = mile * 1.609344
    km_result_label.config(text=km)


mile_entry  = Entry(width=10)
mile_entry.grid(row=0,column=1)

mile_label = Label(text="Miles")
mile_label.grid(row=0,column=2)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1,column=0)

km_result_label = Label(text="0")
km_result_label.grid(row=1,column=1)

km_label = Label(text="Km")
km_label.grid(row=1,column=2)

calc_button = Button(text="Calculate", command=calc)
calc_button.grid(row=2,column=1)


window.mainloop()