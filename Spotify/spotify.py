import pandas as pd
from pandas import ExcelWriter
import json

in_file = open("Playlists.json", "r")
spotify = json.load(in_file)
writer = pd.ExcelWriter("Top_Ten_Playlists.xlsx", engine='xlsxwriter')

for playlist in spotify["playlists"]: # [:10] top ten
    names = playlist["name"]
    items = playlist["items"]
    tracks,artists,album = [],[],[]

    for item in items:
        for value, key in item["track"].items():
            if value == "trackName":
                tracks.append(key)
            if value == "artistName":
                artists.append(key) 
            if value == "albumName":
                album.append(key)

                df1 = pd.DataFrame(tracks, columns= ['Tracks'])
                index = df1.index
                index.name = names
                df1['Artists'] = artists
                df1['Albums'] = album
    print(df1)
    df1.to_excel(writer, sheet_name=names)

writer.save() 