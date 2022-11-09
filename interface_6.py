import tkinter
from tkinter import Text, END
# Sample Game Over Screen

# The root of the application
window = tkinter.Tk()
window.title("Game Over") # Sets window name
window.geometry('340x440') # Sets width x height of window
window.configure(bg='#333333') # Sets background color

# Frame is a tkinter container within the window box
frame = tkinter.Frame(bg='#333333')

#  Generating Widgets
mainMenuLabel = tkinter.Label(frame, text="Game Over", bg='#333333', fg='#CD0000', font=("Arial", 30))
messageBox = Text(frame, width=25, height=5, font=("Arial", 12))
message = "The robot has won in 5 moves. \nPress New Game to play again or return to the main menu."

newGameButton = tkinter.Button(frame, text="New Game", fg='#008000', width=20, font=("Arial", 14))
menuButton = tkinter.Button(frame, text="Main Menu", width=20, font=("Arial", 14))

# Mapping widgets to screen
mainMenuLabel.grid(row=0, column=0, columnspan=2, sticky="news", pady=40) # sticky instructs space to be taken up as much as possible in the specified directions
messageBox.grid(row=1, column=0, pady=5)
newGameButton.grid(row=7,column=0,columnspan=2, pady=5)
menuButton.grid(row=8,column=0,columnspan=2, pady=5)
messageBox.insert(END, message)

frame.pack()

# Loop is required for interface to function
window.mainloop()
