from tkinter import *

window = Tk()
window.title("miles to km")
window.minsize(width=450, height=250)

is_equal = Label(text="is eqaul to")
is_equal.grid(column=0, row=2)
is_equal.config(padx=10, pady=10)

miles = Label(text="Miles")
miles.grid(column=5, row=1)
miles.config(padx=10, pady=10)

km = Label(text="km")
km.grid(column=5, row=2)
km.config(padx=10, pady=10)

con = Label(text="0")
con.grid(column=3, row=2)
con.config(padx=10, pady=10)

user_input = Entry(width=20)
user_input.grid(column=3, row=1)
user_input.focus()

def miles_to_km():
    con["text"] = round(int(user_input.get()) * 1.609)


but = Button(text="Convert",command=miles_to_km)
but.grid(column=3, row=3)
but.config(padx=10, pady=10)

window.config(padx=20, pady=20)
window.mainloop()
