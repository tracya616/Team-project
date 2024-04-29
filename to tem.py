import os
import pandas as pd

# File paths
excel_file_path = r'C:\Users\atrac\Documents\tem.xlsx'

# Check if the Excel file exists
if os.path.exists(excel_file_path):
    # If the file exists, delete it
    os.remove(excel_file_path)

# Load the CSV files with 'latin1' encoding
teams_data = pd.read_csv(r"C:\Users\atrac\Downloads\Teams.csv", encoding='latin1')
parks_data = pd.read_csv(r"C:\Users\atrac\Downloads\lahman_1871-2023_csv\Parks.csv", encoding='latin1')

# List of specified parks
specified_parks = [
    "Miller Park", "Wrigley Field", "Citizens Bank Park", "Fenway Park",
    "Nationals Park", "Oracle Park", "Coors Field", "Kauffman Stadium",
    "Chase Field", "Minute Maid Park",
    "T-Mobile Park", "Progressive Field", "O.co Coliseum", "Marlins Park", "Busch Stadium"
]

# Filter teams based on specified parks
filtered_teams = teams_data[teams_data['park'].isin(specified_parks)]

# Merge the filtered teams with parks data based on park name
merged_data = pd.merge(filtered_teams, parks_data, left_on='park', right_on='parkname', how='inner')

# Save the merged data to an Excel file
merged_data.to_excel(excel_file_path, index=False)
