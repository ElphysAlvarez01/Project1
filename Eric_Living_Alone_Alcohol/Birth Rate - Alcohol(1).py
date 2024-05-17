#!/usr/bin/env python
# coding: utf-8

# In[83]:


import pandas as pd


# In[84]:


import matplotlib.pyplot as plt


# In[85]:


import numpy as np


# In[86]:


# Paths to the datasets
birth_rates_path = r"C:\Users\ericd\Downloads\NCHS_-_Birth_Rates_for_Females_by_Age_Group__United_States.csv"
alcohol_use_path = r"C:\Users\ericd\Downloads\Alcohol.csv"


# In[72]:


# Load the datasets
birth_rates_df = pd.read_csv(birth_rates_path)
alcohol_use_df = pd.read_csv(alcohol_use_path)


# In[ ]:





# In[73]:


# Preprocess the alcohol use data: convert DATE to year and average the data by year
alcohol_use_df['Year'] = pd.to_datetime(alcohol_use_df['DATE']).dt.year
alcohol_use_agg = alcohol_use_df.groupby('Year')['CUSR0000SAF116'].mean().reset_index()


# In[74]:


# Calculate the correlation between birth rate and alcohol use
correlation = merged_data[['CUSR0000SAF116', 'Birth Rate']].corr()


# In[75]:


# Aggregate the birth rates data: calculate the average birth rate across all age groups for each year
birth_rates_agg = birth_rates_df.groupby('Year')['Birth Rate'].mean().reset_index()


# In[76]:


# Merge the alcohol use data with the birth rates data on 'Year'
merged_data = pd.merge(alcohol_use_agg, birth_rates_agg, on='Year', how='inner')


# In[77]:


# Display the merged DataFrame and the correlation matrix
print(merged_data)
print(correlation)


# In[91]:


# Define the range of years
years = range(1967, 2019)


# In[92]:


# Define the average alcohol use data (you will replace this with your actual data)
alcohol_use_avg = [
    46.375, 48.0, 49.683, 52.083, 54.183, 56.15, 57.15, 59.025, 59.967, 60.958,
    62.583, 63.9, 64.883, 65.833, 66.792, 68.45, 68.817, 69.967, 71.183, 71.708,
    72.367, 72.7, 73.525, 74.392, 74.908, 75.4, 75.775, 76.433, 76.875, 77.417,
    77.933, 78.45, 78.833, 79.233, 79.45, 79.633, 79.725, 80.092, 80.425, 80.717,
    81.008, 81.175, 81.3, 81.392, 81.483, 81.592, 81.7, 81.792, 81.908, 81.992,
    82.075, 82.158
]


# In[93]:


# Define the average birth rate data (replace with your actual data)
birth_rate_avg = [
    63.9625, 61.6125, 61.3875, 62.0, 56.6625, 53.475, 50.85, 50.6125, 49.4375, 48.8,
    48.7875, 48.375, 47.9625, 46.9875, 46.275, 45.7875, 45.2875, 44.9875, 44.4625, 44.2,
    44.175, 44.0, 43.85, 43.6125, 43.0875, 42.6875, 42.1, 41.625, 41.1625, 40.8,
    40.4875, 40.1125, 39.9625, 39.4375, 39.2125, 39.1625, 39.175, 39.1, 39.075, 39.2,
    39.2875, 38.875, 38.4625, 38.1375, 37.8125, 37.6625, 37.5125, 37.4375, 37.2875, 37.2,
    37.075, 36.9875
]


# In[94]:


df = pd.DataFrame({
    'Year': list(years),
    'Alcohol Use (Avg)': alcohol_use_avg,
    'Birth Rate (Avg)': birth_rate_avg})


# In[95]:


# Plotting
fig, ax1 = plt.subplots()


# In[96]:


# Alcohol Use Average
ax1.set_xlabel('Year')
ax1.set_ylabel('Alcohol Use (Avg)', color='tab:red')
ax1.plot(df['Year'], df['Alcohol Use (Avg)'], color='tab:red')
ax1.tick_params(axis='y', labelcolor='tab:red')


# In[97]:


# Birth Rate Average on a secondary y-axis
ax2 = ax1.twinx()
ax2.set_ylabel('Birth Rate (Avg)', color='tab:blue')
ax2.plot(df['Year'], df['Birth Rate (Avg)'], color='tab:blue')
ax2.tick_params(axis='y', labelcolor='tab:blue')

plt.title('Comparison of Average Alcohol Use and Birth Rate by Year')
plt.show()


# In[98]:


plt.title('Alcohol Use and Birth Rate Over Years')
fig.tight_layout()
plt.show()


# In[ ]:




