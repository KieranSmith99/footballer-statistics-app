from tkinter import *
from main import select_player_row

window = Tk()
window.geometry("250x250")

topLabel = Label(window, text="FPL Stats App")
topLabel.pack()

middleLabel = Label(window, text="Enter the surname of a footballer:")
middleLabel.pack()

e = Entry(window, width="50")
e.pack()

submitButton = Button(window, text="Enter", command=lambda: select_player_row(e.get()))
submitButton.pack()

window.mainloop()