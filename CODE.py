import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Step 2: Load the Excel file
file_path = r"C:\Users\atrac\Downloads\ParkFactorData.xlsx"
df = pd.read_excel(file_path)


# Step 3: Prompt the user for two park keys
park_key1 = input("Enter the first park key: ")
park_key2 = input("Enter the second park key: ")


# Step 4: Filter the data for the specified park keys and years
park_keys = [park_key1, park_key2]
years = [2021, 2022, 2023]
filtered_data = df[df['parkkey'].isin(park_keys) & df['yearID'].isin(years)]


# Step 5: Create histograms for each specified column
columns = ["Park Factor", "Runs", "OBP", "Hits", "1B", "2B", "3B", "HR", "BB", "SO"]


for column in columns:
    plt.figure(figsize=(10, 6))
    color_map = plt.cm.get_cmap('tab10', len(park_keys))
    for i, park_key in enumerate(park_keys):
        for j, year in enumerate(years):
            subset_data = filtered_data[(filtered_data['parkkey'] == park_key) & (filtered_data['yearID'] == year)]
            bar_positions = np.arange(len(years)) + i * 0.35 - 0.175
            plt.bar(bar_positions[j], subset_data[column], width=0.35, alpha=0.5, label=f"{park_key} - {year}", color=color_map(i))


    plt.axhline(y=100, color='r', linestyle='--', label='Midline')
    plt.xlabel('Year')
    plt.ylabel("Numbers")
    plt.title(f'Histogram of {column} for {", ".join(park_keys)}')
    plt.xticks(np.arange(len(years)), years)
    plt.yticks(np.arange(90, 161, 5))  # Set y-ticks to display values from 90 to 130
    plt.legend()
    plt.grid(True)
    plt.show()


