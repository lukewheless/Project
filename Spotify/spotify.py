import pandas as pd
import json

in_file = open("Playlist1.json", "r")
spotify = json.load(in_file)

for playlist in spotify["playlists"]:
    names = playlist["name"]
    items = playlist["items"]
    tracks,artists,album = [],[],[]
    #while names != "hype":
    
    for item in items:
        for value, key in item["track"].items():
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

#with open('Spotify_Playlists.csv', 'w') as f:
    #pd.concat([df], axis=0).to_csv(f, header=False)
              
#df.to_csv("Spotify_Playlists.csv")