from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_pass():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for n in range(nr_letters)]
    password_symbols = [random.choice(symbols) for n in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for n in range(nr_numbers)]

    password_list = password_symbols + password_numbers + password_letter
    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    password = "".join(password_list)
    pyperclip.copy(password)
    password_input.delete(0,END)
    password_input.insert(0,password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = web_input.get()
    email = email_input.get()
    passwrd = password_input.get()

    if len(website) == 0 or len(email) == 0 or len(passwrd) == 0:
        messagebox.showinfo(title="ERROR", message="Don't leave any field empty")
    else:
        is_okay = messagebox.askokcancel(title=website,
                                         message=f"The info added are:\n Email:{email} \n password:{passwrd}\n")
        if is_okay:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} || {email} || {passwrd}\n")

    web_input.delete(0, END)
    email_input.delete(0, END)
    password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

# canvas and its height and width
canvas = Canvas(width=200, height=200)

# using canvas in-built method for uploading image
lock_pic = PhotoImage(file="logo.png")
# using canvas to display pic and specify its height and width
canvas.create_image(100, 100, image=lock_pic)
canvas.grid(column=1, row=0)

web = Label(text="Website: ", font=("san-fracis", 12, "bold"))
web.grid(column=0, row=1)

web_input = Entry(width=35)
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()

Email = Label(text="Email/Username:  ", font=("san-fracas", 12, "bold"))
Email.grid(column=0, row=2)

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "harsh.kanodiya@gmail.com")

password = Label(text="Password:  ", font=("san-fracas", 12, "bold"))
password.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3, columnspan=1)

Generate = Button(text="Generate Password",command=generate_pass)
Generate.grid(column=2, row=3)

Add = Button(width=36, text="Add", command=save)
Add.grid(column=1, row=4, columnspan=2)

window.mainloop()
