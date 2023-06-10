from tkinter import *


def calculate_conversion():
    miles = int(input.get())
    km = miles*1.60934
    conversion_label["text"] = km
    print(km)
    # return km

# Window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=75, pady=80)

# Miles Input
input = Entry(width=10)
input.grid(column=1, row=0)

# Miles Label
miles_label = Label(text="Miles", font=("Arial", 28))
miles_label.grid(column=2, row=0)

#Is Equal To
equal_label = Label(text="is equal to", font=("Arial", 28))
equal_label.grid(column=0, row=1)

# Conversion (Km) Label
conversion_label = Label(text=0, font=("Arial", 28))
conversion_label.grid(column=1, row=1)

# Km Label
km_label = Label(text="Km", font=("Arial", 28))
km_label.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=calculate_conversion)
calc_button.grid(column=1, row=2)

window.mainloop()
