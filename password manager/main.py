from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(6, 8))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters+password_symbols+password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please fill out all fields.")
        return

    is_ok = messagebox.askokcancel(title="Confirmation", message="Do you want to save the password?")

    if is_ok:
        try:
            with open("Python-Projects\password manager\data.json", "r") as f:
                data = json.load(f)
                data.update(new_data)
        except FileNotFoundError:
            data = new_data
        finally:
            with open("Python-Projects\password manager\data.json", "w") as f:
                json.dump(data, f, indent=4)
    
    website_input.delete(0, END)
    password_input.delete(0, END)
    website_input.focus()
    
# ---------------------------- SEARCHING ------------------------------- #
def find_password():
    website = website_input.get()

    try:
        with open("Python-Projects\password manager\data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {website} exists.")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="Python-Projects\password manager\logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_input = Entry(width=22)
website_input.grid(row=1, column=1)
website_input.focus()  
email_input = Entry(width=40)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0,"vaishkaalt@gmail.com")
password_input = Entry(width=22)
password_input.grid(row=3, column=1)

# Buttons
search_btn = Button(text="Search",width=14, command=find_password)
search_btn.grid(row=1, column=2, sticky="E")
generate_btn = Button(text="Generate Password",width=14, command=generate_password)
generate_btn.grid(row=3, column=2, sticky="E")
add_btn = Button(text="Add", width=34, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()