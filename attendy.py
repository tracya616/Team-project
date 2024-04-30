import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = r"C:\Users\atrac\Documents\tem.xlsx"
teams_data = pd.read_excel(file_path)

# Specified parks including "American Family Field" and "Oracle Park"
specified_parks = [
   "Miller Park", "Wrigley Field", "Citizens Bank Park", "Fenway Park",
    "Nationals Park", "Oracle Park", "Coors Field", "Kauffman Stadium",
    "Chase Field", "Minute Maid Park",
    "T-Mobile Park", "Progressive Field", "O.co Coliseum", "Marlins Park", "Busch Stadium"
]

# Filter data for specified parks and years 2010 to 2023 excluding 2020
filtered_data = teams_data[(teams_data['park'].isin(specified_parks)) & (teams_data['yearID'].between(2010, 2023)) & (teams_data['yearID'] != 2020)]

# Group data by year and park and sum attendance
attendance_by_year_park = filtered_data.groupby(['yearID', 'park'])['attendance'].sum().reset_index()

# Pivot table for better visualization
pivot_table = attendance_by_year_park.pivot(index='park', columns='yearID', values='attendance')

# Fill missing values with zeros
pivot_table.fillna(0, inplace=True)

# Calculate average attendance for each park with 2 decimal places
pivot_table['Average'] = round(pivot_table.mean(axis=1), 2)

# Print table
print("Total Attendance for Specified Parks (2010-2023, excluding 2020) and Average Attendance:\n")
print(pivot_table)




# Group data by park and calculate average attendance
average_attendance = filtered_data.groupby('park')['attendance'].mean().sort_values()

# Plot horizontal bar chart
plt.figure(figsize=(10, 8))
bars = plt.barh(average_attendance.index, average_attendance.values, color=plt.cm.tab20.colors)

# Add labels and title
plt.xlabel('Average Attendance')
plt.ylabel('Team')
plt.title('Average Attendance for Each Team')

# Add legend
plt.legend(bars, average_attendance.index, loc='lower right')

# Calculate the x-coordinate of the x-axis label
x_label_xcoord = plt.gca().xaxis.get_label().get_position()[0]

# Add annotation for x-axis meaning
plt.text(x_label_xcoord, -1, "(Each unit represents 1,000,000)", fontsize=8, ha='center')

# Show plot
plt.show()