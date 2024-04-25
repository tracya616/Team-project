<<<<<<< HEAD
import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV files
teams_file = "C:/Users/atrac/Downloads/lahman_1871-2023_csv/Teams.csv"
batting_file = "C:/Users/atrac/Downloads/lahman_1871-2023_csv/Batting.csv"
homegames_file = "C:/Users/atrac/Downloads/lahman_1871-2023_csv/HomeGames.csv"
parks_file = "C:/Users/atrac/Downloads/lahman_1871-2023_csv/Parks.csv"
pitching_file = "C:/Users/atrac/Downloads/lahman_1871-2023_csv/Pitching.csv"

# Read CSV files into DataFrames
teams_df = pd.read_csv(teams_file)
batting_df = pd.read_csv(batting_file)
homegames_df = pd.read_csv(homegames_file)
parks_df = pd.read_csv(parks_file)
pitching_df = pd.read_csv(pitching_file)

# Define the range of years (2000 to present)
start_year = 2000end_year = pd.Timestamp.now().year

# Filter data for the specified years
teams_df_filtered = teams_df[(teams_df['yearID'] >= start_year) & (teams_df['yearID'] <= end_year)]
batting_df_filtered = batting_df[(batting_df['yearID'] >= start_year) & (batting_df['yearID'] <= end_year)]
homegames_df_filtered = homegames_df[(homegames_df['yearID'] >= start_year) & (homegames_df['yearID'] <= end_year)]
parks_df_filtered = parks_df[(parks_df['yearID'] >= start_year) & (parks_df['yearID'] <= end_year)]
pitching_df_filtered = pitching_df[(pitching_df['yearID'] >= start_year) & (pitching_df['yearID'] <= end_year)]

# Verify the filtered data
print("Teams data for the years {} to {}:".format(start_year, end_year))
print(teams_df_filtered.head())
print("\nBatting data for the years {} to {}:".format(start_year, end_year))
print(batting_df_filtered.head())
print("\nHome games data for the years {} to {}:".format(start_year, end_year))
print(homegames_df_filtered.head())
print("\nParks data for the years {} to {}:".format(start_year, end_year))
print(parks_df_filtered.head())
print("\nPitching data for the years {} to {}:".format(start_year, end_year))
print(pitching_df_filtered.head())

# Visualization example: Histogram of ERA from pitching data
plt.figure(figsize=(8, 6))
plt.hist(pitching_df_filtered['ERA'], bins=20, range=(0, pitching_df_filtered['ERA'].max()), color='salmon', edgecolor='black')
plt.title('Distribution of Earned Run Average (ERA) in 2000-{}'.format(end_year), fontsize=16)
plt.xlabel('ERA', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.grid(True)
plt.show()
=======
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
>>>>>>> 1e45669452781a7dffc9dd868a9b409384df6152
