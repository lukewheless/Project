import pandas as pd
import numpy as np

# import data
strava = pd.read_csv("StravaData.csv")
df = pd.DataFrame(strava)

def speed(col):
    if col['avg_pace'] >= 07:10:
        return "Fast"
    else:
        return "Slow"

df['Speed'] = df.apply(speed, axis=1)

# extracting seconds from time  
df['seconds'] = df['Time'].dt.second
df['avg_seconds'] = df['Avg. Pace'].dt.second

# displaying DataFrame with new seconds columns
display(df)

# moving df to a new csv
df.to_csv("Strava.csv")