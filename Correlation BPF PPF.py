import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the Excel sheet into a DataFrame
df = pd.read_excel(r'C:\Users\atrac\Documents\tem.xlsx')

# List of parks
parks = ["Miller Park", "Wrigley Field", "Citizens Bank Park", "Fenway Park", "Nationals Park", "Coors Field",
         "Kauffman Stadium", "Chase Field", "Minute Maid Park", "Oracle Park"]

# Function to perform regression analysis for each park
def park_regression(park_name):
    # Filter data for the specified park
    park_df = df[df['park'] == park_name]
    
    # Define predictors (X) and target (y)
    X = park_df[['BPF', 'PPF']]  # Ballpark factors
    y = park_df['W']  # Wins
    
    # Initialize and fit the linear regression model
    model = LinearRegression()
    model.fit(X, y)
    
    # Make predictions
    y_pred = model.predict(X)
    
    # Calculate Mean Squared Error
    mse = mean_squared_error(y, y_pred)
    
    # Display results
    print("Park:", park_name)
    print("Coefficients:", model.coef_)
    print("Intercept:", model.intercept_)
    print("Mean Squared Error:", mse)
    print()

# Perform regression analysis for each park
for park in parks:
    park_regression(park)
