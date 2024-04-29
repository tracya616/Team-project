import pandas as pd

# Load the CSV file
file_path = r"C:\Users\atrac\Documents\tem.xlsx"
teams_data = pd.read_excel(file_path)

# Specified parks
specified_parks = [
       "Miller Park", "Wrigley Field", "Citizens Bank Park", "Fenway Park",
    "Nationals Park", "Oracle Park", "Coors Field", "Kauffman Stadium",
    "Chase Field", "Minute Maid Park",
    "T-Mobile Park", "Progressive Field", "O.co Coliseum", "Marlins Park", "Busch Stadium"
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

