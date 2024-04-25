import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the Excel sheet into a DataFrame
df = pd.read_excel(r'C:\Users\atrac\Documents\tem.xlsx')

# Get unique team IDs
unique_teams = df['teamID'].unique()

# Function to perform regression analysis for each team
def team_regression(team_id):
    # Filter data for the specified team
    team_df = df[df['teamID'] == team_id]
    
    # Define predictors (X) and target (y)
    X = team_df[['BPF', 'PPF']]  # Ballpark factors
    y = team_df['R']  # Runs scored
    
    # Initialize and fit the linear regression model
    model = LinearRegression()
    model.fit(X, y)
    
    # Get coefficients and intercept
    coef_bpf = model.coef_[0]
    coef_ppf = model.coef_[1]
    intercept = model.intercept_
    
    # Display results
    print(f"Team: {team_id}")
    print(f"Coefficient for BPF: {coef_bpf:.2f}")
    print(f"Coefficient for PPF: {coef_ppf:.2f}")
    print(f"Intercept: {intercept:.2f}")
    print()

# Perform regression analysis for each team
for team in unique_teams:
    team_regression(team)
