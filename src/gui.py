from tkinter import *
from main import select_player_row
from main import high_value_players
from main import highest_points
from main import most_valuable_teams
from main import high_value_defenders

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

valueButton = Button(window, text="Click for the highest value-for-money players!", command=high_value_players)
valueButton.pack()

pointsButton = Button(window, text="Click to see the 15 players with the most points!", command=highest_points)
pointsButton.pack()

teamValueButton = Button(window, text="Click for the highest value-for-money teams!", command=most_valuable_teams)
teamValueButton.pack()

defValueButton = Button(window, text="Click for highest value-for-money defenders!", command=high_value_defenders)
defValueButton.pack()

window.mainloop()