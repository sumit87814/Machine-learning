#loading the required libraries
from turtle import color
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
fifa=pd.read_csv('players_20.csv')
fifa.head()
# for col in fifa.columns:
#     print(col)
fifa.shape
fifa['nationality'].value_counts()[0:5].keys
# plt.figure(figsize=(8,5))
# plt.bar(list(fifa['nationality'].value_counts()[0:5].keys()),list(fifa['nationality'].value_counts()[0:5]),color="red")


# player_salary=fifa[['short_name','wage_eur']]
# player_salary.head()
fifa['nationality']=='germany'

Germany=fifa[fifa['nationality']=='germany']
Germany.head(5)
Germany.sort_values(by=['height_cm'],ascending=False).head()
Germany.sort_values(by=['weight_kg'],ascending=False).head()
player_salary=Germany[['short_name','wage_eur']].sort_values(by=['wage_eur'],ascending=False)
player_salary.head()
player_shootinig=fifa['short_name','shooting']
player_shootinig.sort_values(by=['shooting'],ascending=False).head()
