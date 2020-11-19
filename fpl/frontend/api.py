import requests
import numpy as np
import pandas as pd

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

def select_player_row(userInput):
    return slim_elements_df.loc[slim_elements_df['second_name'] == userInput].to_string(index=False)

def high_value_players():
    return slim_elements_df.sort_values('value',ascending=False).head(15).to_string(index=False)

def highest_points():
    return slim_elements_df.sort_values('total_points',ascending=False).head(15).to_string(index=False)

def most_valuable_teams():
    return team_pivot.sort_values('value',ascending=False).to_string(index=False)

def high_value_defenders():
    return def_df.sort_values('value',ascending=False).head(15).to_string(index=False)