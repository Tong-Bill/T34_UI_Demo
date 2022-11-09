import tkinter
from tkinter import messagebox

# Sample Login screen

# The root of the application
window = tkinter.Tk()
window.title("Login Screen") # Sets window name
window.geometry('340x440') # Sets width x height of window
window.configure(bg='#333333') # Sets background color

# To be connected to a database in the future
# Should not be hard coded
def login():
    username = "billtong"
    password = "abcd"
    if enterUsername.get() == username and enterPassword.get() == password:
        messagebox.showinfo(title="Success", message="You have been logged in")
    else:
        messagebox.showerror(title="Error", message="Invalid Username or Password")

# Frame is a tkinter container within the window box
frame = tkinter.Frame(bg='#333333')

#  Generating Widgets
loginLabel = tkinter.Label(frame, text="Login", bg='#333333', fg='#FFFFFF', font=("Arial", 30))
usernameLabel = tkinter.Label(frame, text="Username", bg='#333333', fg='#FFFFFF', font=("Arial", 14))
enterUsername = tkinter.Entry(frame, font=("Arial", 14))
passwordLabel = tkinter.Label(frame, text="Password", bg='#333333', fg='#FFFFFF', font=("Arial", 14))
enterPassword = tkinter.Entry(frame, show="*", font=("Arial", 14))
loginButton = tkinter.Button(frame, text="Login", font=("Arial", 14), command=login)
createButton = tkinter.Button(frame, text="Create Account", font=("Arial", 14))

# Mapping widgets to screen
loginLabel.grid(row=0, column=0, columnspan=2, sticky="news", pady=40) # sticky instructs space to be taken up as much as possible in the specified directions
usernameLabel.grid(row=1,column=0)
enterUsername.grid(row=1,column=1, pady=10)
passwordLabel.grid(row=2,column=0)
enterPassword.grid(row=2,column=1, pady=10)
loginButton.grid(row=3,column=0,columnspan=2, pady=15)
createButton.grid(row=4, column=0, columnspan=2, pady=15)

frame.pack()

# Loop is required for interface to function
window.mainloop()
