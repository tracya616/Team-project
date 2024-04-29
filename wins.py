import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the Excel sheet into a DataFrame
df = pd.read_excel(r'C:\Users\atrac\Documents\tem.xlsx')

# List of team IDs
team_ids = df['teamID'].unique()

# Function to perform regression analysis for each team
def team_regression(team_id):
    # Filter data for the specified team
    team_df = df[df['teamID'] == team_id]
    
    # Define predictors (X) and target (y)
    X = team_df[['BPF', 'PPF']]  # Ballpark factors
    y = team_df['W']  # Wins
    
    # Initialize and fit the linear regression model
    model = LinearRegression()
    model.fit(X, y)
    
    # Make predictions
    y_pred = model.predict(X)
    
    # Calculate Mean Squared Error
    mse = mean_squared_error(y, y_pred)
    
    # Calculate R^2
    r_squared = model.score(X, y)
    
    # Print regression statistics
    print(f"Team {team_id} Regression Statistics:")
    print(f"R^2: {r_squared:.2f}")
    print(f"Mean Squared Error: {mse:.2f}")
    print("Coefficients:", [round(coef, 2) for coef in model.coef_])
    print("Intercept:", round(model.intercept_, 2))
    print("")

# Perform regression analysis for each team
for team_id in team_ids:
    team_regression(team_id)
