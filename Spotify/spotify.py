import pandas as pd
import json

in_file = open("Playlist1.json", "r")
spotify = json.load(in_file)

playlist = spotify["playlists"][0] #grabs playlist by order [0-13]

items = playlist["items"]

tracks,artists,names = [],[],[]

for i in items:
    for value, key in i["track"].items():
        if value == "trackName":
            tracks.append(key)
        if value == "artistName":
            artists.append(key) 
        if value == "albumName":
            names.append(key)

df = pd.DataFrame(tracks, columns= ['Tracks'])
df['Artists'] = artists
df['Albums'] = names

print(df)
#df.to_csv("Spotify_Data.csv")