# PASSWORD MANAGER
from tkinter import *
from tkinter import messagebox
import random
import json


# import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def generate_password():
	password_entry.delete(0, END)
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
	           'v',
	           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
	           'R',
	           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	password_letters = [random.choice(letters) for char in range(random.randint(8, 10))]
	password_symbols = [random.choice(symbols) for sym in range(random.randint(2, 4))]
	password_numbers = [random.choice(numbers) for num in range(random.randint(2, 4))]
	password_list = password_letters + password_symbols + password_numbers
	random.shuffle(password_list)
	password = "".join(password_list)
	password_entry.insert(0, password)


# pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_info():
	global website_entry, user_entry, password_entry
	website = website_entry.get().upper()
	user = user_entry.get()
	password = password_entry.get()
	new_data = {
		website: {
			"user": user,
			"password": password,
		},
	}
	if len(website) == 0 or len(user) == 0 or len(password) == 0:
		messagebox.showinfo(title = "Oops!", message = "Please don't leave any fields empty!")
	else:
		is_okay = messagebox.askokcancel(title = f"{website}", message = f"These are the details entered:\nUsername: "
		                                                                 f"{user}\nPassword: {password}\nIs it "
		                                                                 f"okay to save?")
		if is_okay:
			try:
				with open(file = "password_data.json", mode = "r") as info_file:
					data = json.load(info_file)  # Reading old data
			except:
				with open(file = "password_data.json", mode = "w") as info_file:
					json.dump(new_data, info_file, indent = 4)
			else:
				data.update(new_data)  # Updating old data with new data
				with open(file = "password_data.json", mode = "w") as info_file:
					json.dump(data, info_file, indent = 4)  # #Saving new data
			finally:
				website_entry.delete(0, END)
				password_entry.delete(0, END)


# ------------------------------- FIND PASSWORD ------------------------------- #
def find_password():
	website = website_entry.get().upper()
	try:
		with open(file = "password_data.json", mode = "r") as info_file:
			data = json.load(info_file)
	except:
		messagebox.showinfo(title = "Error!", message = "No Data File Found")
	else:
		if website in data:
			user_info = data[website]["user"]
			password_info = data[website]["password"]
			messagebox.showinfo(title = website, message = f"User: {user_info}\nPassword: {password_info}")
		else:
			messagebox.showinfo(title = "Error!", message = "No details for the website exists")


# ---------------------------- UI SETUP ------------------------------- #
# Creating window
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

# Creating canvas
canvas = Canvas(width = 200, height = 200)
logo = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo)
canvas.grid(row = 0, column = 1)

# Creating labels
website_label = Label(text = "Website:")
website_label.grid(row = 1, column = 0)
user_label = Label(text = "Email/Username:")
user_label.grid(row = 2, column = 0)
password_label = Label(text = "Password:")
password_label.grid(row = 3, column = 0)

# Creating entries
website_entry = Entry(width = 33)
website_entry.focus()
website_entry.grid(row = 1, column = 1)
user_entry = Entry(width = 52)
user_entry.insert(0, "example@email.com")
user_entry.grid(row = 2, column = 1, columnspan = 2)
password_entry = Entry(width = 33)
password_entry.grid(row = 3, column = 1)

# Creating buttons
search_btn = Button(text = "Search", width = 14, command = find_password)
search_btn.grid(row = 1, column = 2, columnspan = 2)
generate_btn = Button(text = "Generate password", command = generate_password)
generate_btn.grid(row = 3, column = 2)
add_btn = Button(text = "Add", width = 44, command = add_info)
add_btn.grid(row = 4, column = 1, columnspan = 2)

##
##
##
window.mainloop()
