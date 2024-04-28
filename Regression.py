# Step 1: Import necessary libraries
import pandas as pd
import statsmodels.api as sm


# Step 2: Read the data into a pandas DataFrame
file_path = "/User/Hulveyk03/Downloads/HomeGames.xlsx"
data = pd.read_excel(file_path)


# Step 3: Filter the DataFrame based on criteria
filtered_data = data[(data['yearkey'].isin([2021, 2022, 2023])) &
                     (data['parkkey'].isin(['ML06', 'CHI11', 'PHI12', 'BOS07', 'WAS11', 'SFO03', 'DEN02', 'KAN06', 'PHO01', 'HOU03']))]


# Step 4: Perform multiple regression analysis
X = filtered_data[['yearkey', 'leaguekey', 'teamkey', 'parkkey', 'Spanlast', 'games', 'openings']]
y = filtered_data['attendance']


X = sm.add_constant(X)  # Add a constant term to the predictor
model = sm.OLS(y, X).fit()  # Fit the model


# Step 5: Print summary statistics
print(model.summary())
