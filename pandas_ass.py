# Import necessary libraries
import pandas as pd

# 1. Load the dataset
df = pd.read_csv('data/vgsales.csv')

# 2. Display the first 10 rows of the dataset
print("First 10 rows of the dataset:")
print(df.head(10))

# 3. Display the shape and basic information about the dataset
print("\nShape of the dataset:", df.shape)
print("\nBasic information about the dataset:")
print(df.info())

# 4. Check for missing data and handle it appropriately
print("\nChecking for missing data:")
missing_data = df.isnull().sum()
print(missing_data)

# Handle missing data - dropping rows with any missing data:
df = df.dropna()

# 5. Display the top 5 video games by global sale
top_5_games = df.nlargest(5, 'Global_Sales')
print("\nTop 5 video games by global sales:")
print(top_5_games[['Name', 'Global_Sales']])

# 6. Calculate the total sales in North America for the 'Action' genre
na_sales_action = df[df['Genre'] == 'Action']['NA_Sales'].sum()
print("\nTotal sales in North America for 'Action' genre:", na_sales_action)

# 7. Find the top 3 publishers by global sales
top_publishers = df.groupby('Publisher')['Global_Sales'].sum().nlargest(3)
print("\nTop 3 publishers by global sales:")
print(top_publishers)

# 8. Calculate the average sales in Europe for the 'Shooter' genre
avg_eu_sales_shooter = df[df['Genre'] == 'Shooter']['EU_Sales'].mean()
print("\nAverage sales in Europe for 'Shooter' genre:", avg_eu_sales_shooter)

# 9. Find the game with the highest sales in Japan in the 'Sports' genre
top_jp_sports = df[df['Genre'] == 'Sports'].nlargest(1, 'JP_Sales')
print("\nGame with the highest sales in Japan in the 'Sports' genre:")
print(top_jp_sports[['Name', 'JP_Sales']])