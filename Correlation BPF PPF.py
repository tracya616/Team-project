import pandas as pd
import pandas as pd
from scipy.stats import spearmanr


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



# Calculate Spearman rank correlation coefficient between ERA and BPF
spearman_era_bpf, _ = spearmanr(filtered_data['ERA'], filtered_data['BPF'])

# Calculate Spearman rank correlation coefficient between ERA and PPF
spearman_era_ppf, _ = spearmanr(filtered_data['ERA'], filtered_data['PPF'])

# Calculate Spearman rank correlation coefficient between R and BPF
spearman_r_bpf, _ = spearmanr(filtered_data['R'], filtered_data['BPF'])

# Calculate Spearman rank correlation coefficient between R and PPF
spearman_r_ppf, _ = spearmanr(filtered_data['R'], filtered_data['PPF'])

print("Spearman rank correlation coefficient between ERA and BPF:", spearman_era_bpf)
print("Spearman rank correlation coefficient between ERA and PPF:", spearman_era_ppf)
print("Spearman rank correlation coefficient between R and BPF:", spearman_r_bpf)
print("Spearman rank correlation coefficient between R and PPF:", spearman_r_ppf)




# Filter data for relevant columns
filtered_data = teams_data[['W', 'L', 'Ghome']]

# Calculate Pearson correlation coefficient between Wins (W) and Home games (Ghome)
pearson_correlation = filtered_data['W'].corr(filtered_data['Ghome'])

print("Pearson correlation coefficient between Wins and Home games:", pearson_correlation)
