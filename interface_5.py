import tkinter
from tkinter import Toplevel, Scale

# Sample Difficulty Setting 

# The root of the application
window = tkinter.Tk()
window.title("Main Menu") # Sets window name
window.geometry('340x440') # Sets width x height of window
window.configure(bg='#333333') # Sets background color

# Frame is a tkinter container within the window box
frame = tkinter.Frame(bg='#333333')

# Difficulty Slider
# 1.    Easy
# 2.    Normal
# 3.    Hard
def difficulty():
    newWindow = Toplevel(frame)
    newWindow.title("Difficulty")
    newWindow.geometry('200x200')

    # Slider for difficulty mode
    slider = Scale(newWindow, from_=1, to=3, orient="horizontal")
    slider.grid(row=1,column=0,columnspan=2,pady=10)
    slider.pack()
    # Save Button
    saveButton = tkinter.Button(newWindow, text="Save", font=("Arial", 14))
    saveButton.pack()

#  Generating Widgets
settingsLabel = tkinter.Label(frame, text="Settings", bg='#333333', fg='#FFFFFF', font=("Arial", 30))
difficultyButton = tkinter.Button(frame, text="Adjust Difficulty", width=20, font=("Arial", 14), command=difficulty)
displayButton = tkinter.Button(frame, text="Display", width=20, font=("Arial", 14))
personalizationButton = tkinter.Button(frame, text="Personalization", width=20, font=("Arial", 14))
backButton = tkinter.Button(frame, text="Back", fg="#FF0000", font=("Arial", 14))
moreOptionsButton = tkinter.Button(frame, text=">>", font=("Arial", 14))

# Mapping widgets to screen
settingsLabel.grid(row=0, column=0, columnspan=2, sticky="news", pady=40) # sticky instructs space to be taken up as much as possible in the specified directions
difficultyButton.grid(row=1,column=0,columnspan=2, pady=5)
displayButton.grid(row=2,column=0,columnspan=2, pady=5)
personalizationButton.grid(row=3,column=0,columnspan=2, pady=5)
backButton.grid(row=4,column=0, pady=15)
moreOptionsButton.grid(row=4, column=1, pady=15)

frame.pack()

# Loop is required for interface to function
window.mainloop()
