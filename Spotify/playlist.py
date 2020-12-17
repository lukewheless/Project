import pandas as pd
import json

in_file = open("Playlists.json", "r")
spotify = json.load(in_file)

playlist = spotify["playlists"][0] # grabs playlist [0-13]
names = playlist["name"]
items = playlist["items"]

tracks,artists,album = [],[],[]

for i in items:
    for value, key in i["track"].items():
        if value == "trackName":
            tracks.append(key)
        if value == "artistName":
            artists.append(key) 
        if value == "albumName":
            album.append(key)

df = pd.DataFrame(tracks, columns= ['Tracks'])
index = df.index
index.name = names
df['Artists'] = artists
df['Albums'] = album

print(df)

#df.to_csv("Spotify_Data_Playlist.csv")