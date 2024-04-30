import pandas as pd
from sklearn.linear_model import LinearRegression

# Read the Excel file
file_path = r'C:\Users\atrac\Documents\tem.xlsx'
df = pd.read_excel(file_path)

# Group by team ID
grouped = df.groupby('teamID')

# Perform regression for each group
for team, group in grouped:
    X = group[['BPF', 'PPF']].values
    y = group['ERA'].values
    model = LinearRegression()
    model.fit(X, y)
    print(f"Team: {team}")
    print("Coefficients:", model.coef_,2)
    print("Intercept:", model.intercept_,2)
    print("R-squared:", model.score(X, y),2)
    print()
  