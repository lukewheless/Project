import pandas as pd
import numpy as np

# import data
strava = pd.read_csv("StravaData.csv")
df = pd.DataFrame(strava)
print(df)

# manipulate dataset
df['Ave_Pace'] = (df['Time']/df['Distance (m)'])

# extracting seconds from time  
df['Total_Seconds'] = df['Time'].dt.second
df['Avg_Seconds'] = df['Avg_Pace'].dt.second

def speed(col):
    if col['Avg_Seconds'] >= 430: # 7:10 time
        return "Fast"
    else:
        return "Slow"

df['Speed'] = df.apply(speed, axis=1)

# displaying DataFrame with new columns
print(df)

# moving df to a new csv
df.to_csv("Strava.csv")