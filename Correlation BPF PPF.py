import pandas as pd

# Load the CSV file
file_path = r'C:\Users\atrac\Downloads\lahman_1871-2023_csv\Teams.csv'
teams_data = pd.read_csv(file_path)

# Filter data for specified parks
specified_parks = [
    'American Family Field', 'Wrigley Field', 'Citizens Bank Park', 
    'Fenway Park', 'Nationals Park', 'AT&T Park', 'Coors Field', 
    'Kauffman Stadium', 'Chase Field', 'Minute Maid Park'
]

filtered_data = teams_data[teams_data['park'].isin(specified_parks)]

# Filter data for relevant columns
filtered_data = filtered_data[['yearID', 'BPF', 'PPF', 'ERA', 'R']]

# Calculate Pearson correlation coefficient between ERA and BPF
correlation_era_bpf = filtered_data['ERA'].corr(filtered_data['BPF'])

# Calculate Pearson correlation coefficient between ERA and PPF
correlation_era_ppf = filtered_data['ERA'].corr(filtered_data['PPF'])

# Calculate Pearson correlation coefficient between R and BPF
correlation_r_bpf = filtered_data['R'].corr(filtered_data['BPF'])

# Calculate Pearson correlation coefficient between R and PPF
correlation_r_ppf = filtered_data['R'].corr(filtered_data['PPF'])

print("Correlation between ERA and BPF:", correlation_era_bpf)
print("Correlation between ERA and PPF:", correlation_era_ppf)
print("Correlation between R and BPF:", correlation_r_bpf)
print("Correlation between R and PPF:", correlation_r_ppf)
