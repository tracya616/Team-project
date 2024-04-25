import pandas as pd

# Load the CSV file
file_path = r'C:\Users\atrac\Downloads\lahman_1871-2023_csv\Teams.csv'
teams_data = pd.read_csv(file_path)

# Specified parks
specified_parks = [
    'American Family Field', 'Wrigley Field', 'Citizens Bank Park', 
    'Fenway Park', 'Nationals Park', 'Oracle Park', 'Coors Field', 
    'Kauffman Stadium', 'Chase Field', 'Minute Maid Park'
]

# Filter data for specified parks
filtered_data = teams_data[teams_data['park'].isin(specified_parks)]

# Filter data for relevant columns
filtered_data = filtered_data[['park', 'W', 'L']]

# Calculate total games played (sum of wins and losses)
filtered_data['Total Games Played'] = filtered_data['W'] + filtered_data['L']

# Group data by park and sum wins, losses, and total games played
park_stats = filtered_data.groupby('park').sum()

print("Wins, Losses, and Total Games Played by Park:")
print(park_stats)

