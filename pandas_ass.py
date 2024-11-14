import streamlit as st
import pandas as pd

# 1. Load the dataset
st.title("Video Game Sales Analysis")
st.write("This app analyzes video game sales data from the `vgsales.csv` dataset.")
#
df = pd.read_csv("data/vgsales.csv")
#OR
# File upload
#uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
#if uploaded_file is not None:
    #df = pd.read_csv(uploaded_file)

    # 2. Display the first 10 rows of the dataset
st.header("First 10 Rows of the Dataset")
st.write(df.head(10))

    # 3. Display the shape and basic information about the dataset
st.header("Dataset Shape and Basic Information")
st.write(f"Shape of the dataset: {df.shape}")
st.write("Basic Information about the dataset:")
buffer = st.text("Loading data info...")
buffer.text(df.info())

    # 4. Check for missing data and handle it appropriately
st.header("Missing Data")
missing_data = df.isnull().sum()
st.write(missing_data)

    # Optionally handle missing data - drop rows with any missing data
df = df.dropna()
st.write("Missing data has been handled by dropping rows with any missing values.")

    # 5. Display the top 5 video games by global sale
st.header("Top 5 Video Games by Global Sales")
top_5_games = df.nlargest(5, 'Global_Sales')
st.write(top_5_games[['Name', 'Global_Sales']])

    # 6. Calculate the total sales in North America for the 'Action' genre
st.header("Total Sales in North America for 'Action' Genre")
na_sales_action = df[df['Genre'] == 'Action']['NA_Sales'].sum()
st.write(f"Total North America sales for 'Action' genre: {na_sales_action}")

    # 7. Find the top 3 publishers by global sales
st.header("Top 3 Publishers by Global Sales")
top_publishers = df.groupby('Publisher')['Global_Sales'].sum().nlargest(3)
st.write(top_publishers)

    # 8. Calculate the average sales in Europe for the 'Shooter' genre
st.header("Average Sales in Europe for 'Shooter' Genre")
avg_eu_sales_shooter = df[df['Genre'] == 'Shooter']['EU_Sales'].mean()
st.write(f"Average Europe sales for 'Shooter' genre: {avg_eu_sales_shooter}")

    # 9. Find the game with the highest sales in Japan in the 'Sports' genre
st.header("Game with the Highest Sales in Japan for 'Sports' Genre")
top_jp_sports = df[df['Genre'] == 'Sports'].nlargest(1, 'JP_Sales')
st.write(top_jp_sports[['Name', 'JP_Sales']])
#else:
 #   st.write("Please upload a CSV file to analyze.")
