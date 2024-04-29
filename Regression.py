# Step 1: Import necessary libraries
import pandas as pd
import statsmodels.api as sm

# Step 2: Read the data from the spreadsheet into a pandas DataFrame
file_path = "/User/Hulveyk03/Downloads/HomeGames.xlsx"
data = pd.read_excel(file_path)

# Step 3: Filter the DataFrame based on the specified criteria: years 2018, 2019, 2021-2023 and specific parkkeys
filtered_data = data[(data['yearkey'].isin([2018, 2019, 2021, 2022, 2023])) &
                     (data['parkkey'].isin(['ML06', 'CHI11', 'PHI12', 'BOS07', 'WAS11', 'SFO03', 'DEN02', 'KAN06', 'PHO01', 'HOU03']))]

# Step 4: Select the independent variables ('spanlast', 'games', 'openings') and the dependent variable ('attendance')
X = filtered_data[['spanlast', 'games', 'openings']]  # Independent variables
y = filtered_data['attendance']  # Dependent variable

# Step 5: Perform multiple regression analysis using statsmodels
X = sm.add_constant(X)  # Add a constant term to the independent variables
model = sm.OLS(y, X).fit()  # Fit the multiple regression model

# Step 6: Print the summary statistics including R squared
print(model.summary())
