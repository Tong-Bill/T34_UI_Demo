import tkinter

# Sample Main Menu screen

# The root of the application
window = tkinter.Tk()
window.title("Main Menu") # Sets window name
window.geometry('340x440') # Sets width x height of window
window.configure(bg='#333333') # Sets background color

# Frame is a tkinter container within the window box
frame = tkinter.Frame(bg='#333333')

#  Generating Widgets
mainMenuLabel = tkinter.Label(frame, text="Main Menu", bg='#333333', fg='#FFFFFF', font=("Arial", 30))
newGameButton = tkinter.Button(frame, text="New Game", fg='#008000', width=20, font=("Arial", 14))
savedLogsButton = tkinter.Button(frame, text="Saved Logs", width=20, font=("Arial", 14))
rulesButton = tkinter.Button(frame, text="Game Rules", width=20, font=("Arial", 14))
settingsButton = tkinter.Button(frame, text="Settings", width=20, font=("Arial", 14))
systemButton = tkinter.Button(frame, text="System Information", width=20, font=("Arial", 14))
logoutButton = tkinter.Button(frame, text="Logout", fg="#FF0000", font=("Arial", 14))
quitButton = tkinter.Button(frame, text="Quit", font=("Arial", 14))

# Mapping widgets to screen
mainMenuLabel.grid(row=0, column=0, columnspan=2, sticky="news", pady=40) # sticky instructs space to be taken up as much as possible in the specified directions
newGameButton.grid(row=1,column=0,columnspan=2, pady=5)
savedLogsButton.grid(row=2,column=0,columnspan=2, pady=5)
rulesButton.grid(row=3,column=0,columnspan=2, pady=5)
settingsButton.grid(row=4,column=0,columnspan=2, pady=5)
systemButton.grid(row=5,column=0,columnspan=2, pady=5)
logoutButton.grid(row=6,column=0, pady=15)
quitButton.grid(row=6, column=1, pady=15)

frame.pack()

# Loop is required for interface to function
window.mainloop()
