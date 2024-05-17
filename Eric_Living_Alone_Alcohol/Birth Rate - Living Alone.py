#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd


# In[14]:


# Load the datasets
birth_rates_path = r"C:\Users\ericd\Downloads\NCHS_-_Birth_Rates_for_Females_by_Age_Group__United_States.csv"
living_alone_path = r"C:\Users\ericd\Downloads\living_alone.csv"


# In[15]:


# Read the CSV files
birth_rates_df = pd.read_csv(birth_rates_path)
living_alone_df = pd.read_csv(living_alone_path)


# In[16]:


# Display the first few rows of each dataset to understand their structure
birth_rates_df.head(), living_alone_df.head()


# In[17]:


# Filter the datasets to include only the common years: 1940, 1960, 1980, 2000, 2018
common_years = [1940, 1960, 1980, 2000, 2018]
birth_rates_common = birth_rates_df[birth_rates_df['Year'].isin(common_years)].groupby('Year')['Birth Rate'].mean().reset_index()


# In[18]:


# Correct the column name issue for living alone data
living_alone_common = living_alone_df[living_alone_df['Year'].isin(common_years)].groupby('Year')['Percentage of Americans living alone, by age, total (IPUMS)'].mean().reset_index()
living_alone_common.rename(columns={'Percentage of Americans living alone, by age, total (IPUMS)': 'Percentage Living Alone'}, inplace=True)


# In[19]:


# Merge the datasets on the year for these common years
data_common_years = pd.merge(birth_rates_common, living_alone_common, on='Year')


# In[20]:


# Calculate the correlation for these years
correlation_common_years = data_common_years[['Birth Rate', 'Percentage Living Alone']].corr()


# In[21]:


# Show the final merged DataFrame and the correlation
data_common_years, correlation_common_years


# In[ ]:




