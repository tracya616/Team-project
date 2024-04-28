import pandas as pd

# Load the CSV file
file_path = r'C:\Users\atrac\Downloads\lahman_1871-2023_csv\Teams.csv'
teams_data = pd.read_csv(file_path)

# Specified parks including "American Family Field" and "Oracle Park"
specified_parks = [
    'Miller Park', 'Wrigley Field', 'Citizens Bank Park', 
    'Fenway Park', 'Nationals Park', 'AT&T Park', 'Coors Field', 
    'Kauffman Stadium', 'Chase Field', 'Minute Maid Park', 'Oracle Park'
]

# Filter data for specified parks and years 2021 to 2023
filtered_data = teams_data[(teams_data['park'].isin(specified_parks)) & (teams_data['yearID'].between(2021, 2023))]

# Group data by year and park and sum attendance
attendance_by_year_park = filtered_data.groupby(['yearID', 'park'])['attendance'].sum().reset_index()

# Pivot table for better visualization
pivot_table = attendance_by_year_park.pivot(index='park', columns='yearID', values='attendance')

# Calculate average attendance for each park with 2 decimal places
pivot_table['Average'] = round(pivot_table.mean(axis=1), 2)

# Print table
print("Total Attendance for Specified Parks (2021-2023) and Average Attendance:\n")
print(pivot_table)
