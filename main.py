from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password_gen = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password_gen)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = website_input.get()
    email = email_user_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="Please fill out all entry fields!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading the old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
            messagebox.showinfo(title="Successful", message="Your information was successfully saved!")

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file was found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password:{password}")
        else:
            messagebox.showinfo(title="Error", message=f"No password has been created for website: {website}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.eval('tk::PlaceWindow . center')

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# labels
website_label = Label(text="Website:              ")
website_label.grid(row=1, column=0)
email_user_label = Label(text="Username/Email:")
email_user_label.grid(row=2, column=0)
password_label = Label(text="Password:          ")
password_label.grid(row=3, column=0)

# Entry Fields
website_input = Entry(width=21)
website_input.grid(row=1, column=1)
website_input.focus()
email_user_input = Entry(width=38)
email_user_input.grid(row=2, column=1, columnspan=2)
email_user_input.insert(0, "jordan@email.com")
password_input = Entry(width=21)
password_input.grid(row=3, column=1)

# Buttons
generate_password = Button(text="Generate Password", command=generator)
generate_password.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)


window.mainloop()