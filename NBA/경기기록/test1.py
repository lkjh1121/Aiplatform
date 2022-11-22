import pandas as pd 

gamedata = pd.read_csv("./gamedate_list.csv")
print(gamedata.head())
gamedata =  gamedata.sort_values(by='GAME_DATE', ascending=True)
print(gamedata) 