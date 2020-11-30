import pandas as pd

# import data
strava = pd.read_csv("StravaData.csv") # index_col=0
df = pd.DataFrame(strava)

# Converting to total minutes
df['Time (min)'] = pd.to_timedelta(df['Time'])
df['Time (min)'] = (df['Time'] / pd.offsets.Minute(1)).round(2)

# Adding new columns to dataset
df['Avg_Pace'] = (df['Time (min)'] / df['Distance (m)']).round(0)

# extracting seconds from minutes 
df['Total_Seconds'] = (df['Time (min)']*60).round(0)

# function that determines speed 
def speed(df):
    if df['Avg_Pace'] <= 7: # above 7:01 time
        return "Fast"
    else:
        return "Slow"

df['Speed'] = df.apply(speed, axis=1)

# moving df to a new csv
print(df)
df.to_csv("Strava_Data.csv")