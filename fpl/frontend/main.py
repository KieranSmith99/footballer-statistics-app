import requests
import numpy as np
import pandas as pd
from tkinter import *
from tkinter import ttk

pd.options.mode.chained_assignment = None

url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

r = requests.get(url)

myJSON = r.json()

myJSON.keys()

elements_df = pd.DataFrame(myJSON['elements'])
elements_types_df = pd.DataFrame(myJSON['element_types'])
teams_df = pd.DataFrame(myJSON['teams'])

slim_elements_df = elements_df[['second_name','team','element_type','selected_by_percent','now_cost','transfers_in','value_season','total_points']]

slim_elements_df['position'] = slim_elements_df.element_type.map(elements_types_df.set_index('id').singular_name)

slim_elements_df['team'] = slim_elements_df.team.map(teams_df.set_index('id').name)

slim_elements_df['value'] = slim_elements_df.value_season.astype(float)

team_pivot = slim_elements_df.pivot_table(index='team',values='value',aggfunc=np.mean).reset_index()

fwd_df = slim_elements_df.loc[slim_elements_df.position == 'Forward']
mid_df = slim_elements_df.loc[slim_elements_df.position == 'Midfielder']
def_df = slim_elements_df.loc[slim_elements_df.position == 'Defender']
goal_df = slim_elements_df.loc[slim_elements_df.position == 'Goalkeeper']

window = Tk()
playerLabel = Label(window, text="")

def select_player_row(userInput):
    global playerLabel
    if userInput.isdigit():
        print("That's a number!")
    else:
        playerRowResult = slim_elements_df.loc[slim_elements_df['second_name'] == userInput].to_string(index=False)

        playerLabel.pack_forget()
        playerLabel = Label(window, text=playerRowResult)
        playerLabel.pack()

def high_value_players():
    return slim_elements_df.sort_values('value',ascending=False).head(15).to_string(index=False)

def highest_points():
    global playerLabel

    playerLabel.pack_forget()
    playerLabel = Label(window, text=slim_elements_df.sort_values('total_points',ascending=False).head(15).to_string(index=False))
    playerLabel.pack()

def most_valuable_teams():
    global playerLabel

    playerLabel.pack_forget()
    playerLabel = Label(window, text=team_pivot.sort_values('value',ascending=False).to_string(index=False))
    playerLabel.pack()

def high_value_defenders():
    global playerLabel

    playerLabel.pack_forget()
    playerLabel = Label(window, text=def_df.sort_values('value',ascending=False).head(15).to_string(index=False))
    playerLabel.pack()

"""window.geometry("700x700")
window.title("FPL Statistics")

topLabel = Label(window, text="FPL Stats App")
topLabel.pack()

middleLabel = Label(window, text="Enter the surname of a current Premier League footballer:")
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

window.mainloop()"""