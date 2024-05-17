pip install pandas

# Import the necessary libraries
import pandas as pd

# Load the datasets
living_alone_df = pd.read_csv('C:\\Users\\ericd\\Downloads\\living_alone.csv')
birth_rate_df = pd.read_csv('C:\\Users\\ericd\\Downloads\\Crude_Birth_Rate.csv')

# Display the first few rows of each dataset to understand their structure (optional)
print("Living Alone DataFrame:")
print(living_alone_df.head())

print("\nCrude Birth Rate DataFrame:")
print(birth_rate_df.head())

# Assuming the datasets have a 'year' column, filter the data for the years 1990-2020
filtered_living_alone_df = living_alone_df[(living_alone_df['year'] >= 1990) & (living_alone_df['year'] <= 2020)]
filtered_birth_rate_df = birth_rate_df[(birth_rate_df['year'] >= 1990) & (birth_rate_df['year'] <= 2020)]

# Merge the datasets on the 'year' column
merged_df = pd.merge(filtered_birth_rate_df, filtered_living_alone_df, on='year')

# Display the merged DataFrame (optional)
print("\nMerged DataFrame:")
print(merged_df.head())

# Calculate the correlation between 'birth_rate' and 'people_living_alone'
correlation = merged_df['birth_rate'].corr(merged_df['people_living_alone'])

print(f"\nCorrelation between birth rate and people living alone (1990-2020): {correlation}")
