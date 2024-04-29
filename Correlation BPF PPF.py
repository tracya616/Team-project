import pandas as pd
<<<<<<< HEAD
=======
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
>>>>>>> 24ca29eabcffb4a9cb1db3a411d5cc0a6515c382

<<<<<<< HEAD
# Load the CSV files with 'latin1' encoding
teams_data = pd.read_csv(r'C:\Users\atrac\Downloads\lahman_1871-2023_csv\Teams.csv', encoding='latin1')
parks_data = pd.read_csv(r'C:\Users\atrac\Downloads\lahman_1871-2023_csv\Parks.csv', encoding='latin1')
=======
# Load the Excel sheet into a DataFrame
df = pd.read_excel(r'C:\Users\atrac\Documents\tem.xlsx')
>>>>>>> 24ca29eabcffb4a9cb1db3a411d5cc0a6515c382

<<<<<<< HEAD
# Merge the dataframes based on park name
merged_data = pd.merge(teams_data, parks_data, left_on='park', right_on='parkname', how='inner')
=======
# List of parks
parks = ["Miller Park", "Wrigley Field", "Citizens Bank Park", "Fenway Park", "Nationals Park", "Coors Field",
         "Kauffman Stadium", "Chase Field", "Minute Maid Park", "Oracle Park"]
>>>>>>> 24ca29eabcffb4a9cb1db3a411d5cc0a6515c382

<<<<<<< HEAD
# Save the merged data to an Excel file
merged_data.to_excel(r'C:\Users\atrac\Documents\tem.xlsx', index=False)
=======
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
    
    # Calculate R^2
    r_squared = model.score(X, y)
    
    # Display results
    print("Park:", park_name)
    print("Coefficients:", model.coef_)
    print("Intercept:", model.intercept_)
    print("Mean Squared Error:", mse)
    print("R^2:", r_squared)
    print()
>>>>>>> 24ca29eabcffb4a9cb1db3a411d5cc0a6515c382

<<<<<<< HEAD
=======
# Perform regression analysis for each park
for park in parks:
    park_regression(park)

>>>>>>> 24ca29eabcffb4a9cb1db3a411d5cc0a6515c382