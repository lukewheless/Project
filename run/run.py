import pandas as pd

# Import data and create df
strava = pd.read_csv("StravaData.csv") 
df = pd.DataFrame(strava)

# Cleaning up column names
df = df.rename(columns={"Distance (mi)": "Distance", "Elevation (ft)": "Elevation"})

# Converting minutes
df['time'] = pd.to_timedelta(df['Time'])
df['time'] = (df['Time'] / pd.offsets.Minute(1)).round(2)

# Adding new columns to dataset
df['Avg_Pace'] = (df['time'] / df['Distance']).round(1)

# Extracting seconds from minutes 
df['Total_Seconds'] = (df['time']*60).round(0)

# Function that determines speed 
def speed(df):
    if df['Avg_Pace'] <= 7: # above 7:01 time
        return "Fast"
    else:
        return "Slow"

df['Speed'] = df.apply(speed, axis=1)

# Assigning df to a new csv
print(df)
df.to_csv("Strava_Data.csv")