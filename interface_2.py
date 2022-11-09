import tkinter

# Sample Account Creation screen

# The root of the application
window = tkinter.Tk()
window.title("Create Account") # Sets window name
window.geometry('340x440') # Sets width x height of window
window.configure(bg='#333333') # Sets background color

# Delete text when input box is clicked
def GhostFirst(_):
    firstName.delete(0, 'end')

def GhostLast(_):
    lastName.delete(0, 'end')

def GhostEmail(_):
    email.delete(0, 'end')

def GhostInvite(_):
    inviteCode.delete(0, 'end')

def GhostPassword(_):
    password.delete(0, 'end')

def GhostConfirm(_):
    confirmPassword.delete(0, 'end')

# Frame is a tkinter container within the window box
frame = tkinter.Frame(bg='#333333')

#  Generating Widgets
createAccountLabel = tkinter.Label(frame, text="Create Account", bg='#333333', fg='#FFFFFF', font=("Arial", 30))
firstName = tkinter.Entry(frame, width=20, font=("Arial", 14))
lastName = tkinter.Entry(frame, width=20, font=("Arial", 14))
email = tkinter.Entry(frame, width=20, font=("Arial", 14))
inviteCode = tkinter.Entry(frame,width=20, font=("Arial", 14))
password = tkinter.Entry(frame,width=20, font=("Arial", 14))
confirmPassword = tkinter.Entry(frame,width=20, font=("Arial", 14))
backButton = tkinter.Button(frame, text="Back", fg="#FF0000", font=("Arial", 14))
createButton = tkinter.Button(frame, text="Create", font=("Arial", 14))

# Mapping widgets to screen
createAccountLabel.grid(row=0, column=0, columnspan=2, sticky="news", pady=40) # sticky instructs space to be taken up as much as possible in the specified directions
firstName.grid(row=1,column=0, columnspan=2, pady=5)
lastName.grid(row=2,column=0, columnspan=2, pady=5)
email.grid(row=3,column=0, columnspan=2, pady=5)
inviteCode.grid(row=4,column=0, columnspan=2,pady=5)
password.grid(row=5,column=0, columnspan=2,pady=5)
confirmPassword.grid(row=6,column=0, columnspan=2,pady=5)
backButton.grid(row=7,column=0, pady=15)
createButton.grid(row=7, column=1, pady=15)

# Inserts Ghost words
firstName.insert(0, "First Name")
lastName.insert(0, "Last Name")
email.insert(0, "Email Address")
inviteCode.insert(0, "Invite Code")
password.insert(0, "Password")
confirmPassword.insert(0, "Confirm Password")
firstName.bind("<Button-1>", GhostFirst)
lastName.bind("<Button-1>", GhostLast)
email.bind("<Button-1>", GhostEmail)
inviteCode.bind("<Button-1>", GhostInvite)
password.bind("<Button-1>", GhostPassword)
confirmPassword.bind("<Button-1>", GhostConfirm)

frame.pack()

# Loop is required for interface to function
window.mainloop()
