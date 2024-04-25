# Problem 1
import pandas as pd

# File paths to CSV files
teams_file = 'C:/Users/atrac/Downloads/lahman_1871-2023_csv/Teams.csv'
batting_file = 'C:/Users/atrac/Downloads/lahman_1871-2023_csv/Batting.csv'
home_games_file = 'C:/Users/atrac/Downloads/lahman_1871-2023_csv/HomeGames.csv'
parks_file = 'C:/Users/atrac/Downloads/lahman_1871-2023_csv/Parks.csv'
pitching_file = 'C:/Users/atrac/Downloads/lahman_1871-2023_csv/Pitching.csv'

# Read CSV files into pandas DataFrames
teams = pd.read_csv(teams_file)
batting = pd.read_csv(batting_file)
home_games = pd.read_csv(home_games_file)
parks = pd.read_csv(parks_file)
pitching = pd.read_csv(pitching_file)

# Merge tables based on common identifiers
merged_data = pd.merge(teams, batting, on=['yearID', 'teamID', 'lgID'], how='left')
merged_data = pd.merge(merged_data, home_games, on=['yearID', 'teamID', 'lgID'], how='left')
merged_data = pd.merge(merged_data, parks, on='parkkey', how='left')
merged_data = pd.merge(merged_data, pitching, on=['yearID', 'teamID', 'lgID'], how='left')

# View the merged dataset
print(merged_data.head())
