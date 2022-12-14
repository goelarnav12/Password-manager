from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

window=Tk()
window.title("Password-Manager")
window.config(padx=50,pady=50)


canvas=Canvas(width=200,height=200)
logo_image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=0,column=1)

website_label=Label(text="Website: ")
website_label.grid(row=1,column=0)

website=Entry(width=21)
website.focus()
website.grid(row=1,column=1)

def searchDetails():

    try:
        with open("password.json") as file:
            data=json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(message="You did not enter details for this website")
    else:
        if website.get() in data:
            email = data[website.get()]["username"]
            password_val=data[website.get()]["password"]
            messagebox.showinfo(message=f"Username: {email}\nPassword: {password_val}")
        else:
            messagebox.showinfo(message="You did not enter details for this website")

search=Button(text="Search",width=13,command=searchDetails)
search.grid(column=2,row=1)

username_label=Label(text="Email/Username: ")
username_label.grid(row=2,column=0)

username=Entry(width=38)
username.insert(0,"goelarnav12@gmail.com")
username.grid(row=2,column=1,columnspan=2)

password_label=Label(text="Password: ")
password_label.grid(row=3,column=0)

password=Entry(width=21)
password.grid(row=3,column=1)

def generatePassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    generated_password = ""
    for char in password_list:
        generated_password += char
    pyperclip.copy(generated_password)

    password.delete(0,END)
    password.insert(0,generated_password)


generate=Button(text="Generate Password",command=generatePassword)
generate.grid(column=2,row=3)


def save_password():

    new_data={
        website.get():{
            "username": username.get(),
            "password": password.get()
        }
    }

    if len(website.get())==0 or len(password.get())==0 :
        messagebox.showerror(title="OOPS",message="You have left some fields empty!!!")
    else:
        # is_ok=messagebox.askyesno(title=website.get(),message=f"These are the details you entered :\nEmail: {username.get()}\nPassword: {password.get()}\nIs it ok to save?")
        is_ok=1
        if is_ok:

            try:
                file = open("password.json", "r")
                data=json.load(file)
                file.close()
            except FileNotFoundError:
                file = open("password.json", "w")
                data = json.dump(new_data,file,indent=4)
                file.close()
            else:
                data.update(new_data)
                file=open("password.json","w")
                json.dump(data,file,indent=4)
                file.close()

            website.delete(0,END)
            username.delete(0, END)
            password.delete(0, END)

            website.insert(0, "")
            username.insert(0, "goelarmav12@gmail.com")
            password.insert(0, "")

            website.focus()
        else:
            pass


add_button=Button(text="Add",width=36,command=save_password)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()