import requests
import numpy as np
import pandas as pd

url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

r = requests.get(url)

myJSON = r.json()

myJSON.keys()

elements_df = pd.DataFrame(myJSON['elements'])
elements_types_df = pd.DataFrame(myJSON['element_types'])
teams_df = pd.DataFrame(myJSON['teams'])

slim_elements_df = elements_df[['second_name','team','element_type','selected_by_percent','now_cost','minutes','transfers_in','value_season','total_points']]

slim_elements_df['position'] = slim_elements_df.element_type.map(elements_types_df.set_index('id').singular_name)

slim_elements_df['team'] = slim_elements_df.team.map(teams_df.set_index('id').name)

print(slim_elements_df.head())