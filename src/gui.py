from tkinter import *
from main import select_player_row
from main import high_value_players

window = Tk()
window.geometry("400x400")
window.title("FPL Statistics")

topLabel = Label(window, text="FPL Stats App")
topLabel.pack()

middleLabel = Label(window, text="Enter the surname of a footballer:")
middleLabel.pack()

e = Entry(window, width="50")
e.pack()

submitButton = Button(window, text="Enter", command=lambda: select_player_row(e.get()))
submitButton.pack()

valueLabel = Label(window, text="Click below to receive the top 10 most value-for-cost players!")
valueLabel.pack()

valueButton = Button(window, text="Enter", command=high_value_players)
valueButton.pack()

window.mainloop()