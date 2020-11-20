import pandas as pd
import numpy as np

# import data
strava = pd.read_csv("StravaData.csv")
df = pd.DataFrame(strava)

df['Ave_Pace'] = (df['Time']/df['Distance (m)'])

def speed(col):
    if col['Ave_Pace'] >= 7:
        return "Fast"
    else:
        return "Slow"

df['Speed'] = df.apply(speed, axis=1)

# extracting seconds from time  
df['Seconds'] = df['Time'].dt.second
df['Avg_Seconds'] = df['avg_pace'].dt.second

# displaying DataFrame with new seconds columns
print(df)

# moving df to a new csv
#df.to_csv("Strava.csv")