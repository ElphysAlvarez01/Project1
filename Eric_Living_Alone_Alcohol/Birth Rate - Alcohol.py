#!/usr/bin/env python
# coding: utf-8

# In[55]:


import pandas as pd


# In[ ]:





# In[56]:


# Paths to the datasets
birth_rates_path = r"C:\Users\ericd\Downloads\NCHS_-_Birth_Rates_for_Females_by_Age_Group__United_States.csv"
alcohol_use_path = r"C:\Users\ericd\Downloads\Alcohol.csv"


# In[57]:


# Load the datasets
birth_rates_df = pd.read_csv(birth_rates_path)
alcohol_use_df = pd.read_csv(alcohol_use_path)


# In[ ]:





# In[58]:


# Preprocess the alcohol use data: convert DATE to year and average the data by year
alcohol_use_df['Year'] = pd.to_datetime(alcohol_use_df['DATE']).dt.year
alcohol_use_agg = alcohol_use_df.groupby('Year')['CUSR0000SAF116'].mean().reset_index()


# In[59]:


# Calculate the correlation between birth rate and alcohol use
correlation = merged_data[['CUSR0000SAF116', 'Birth Rate']].corr()


# In[47]:


# Aggregate the birth rates data: calculate the average birth rate across all age groups for each year
birth_rates_agg = birth_rates_df.groupby('Year')['Birth Rate'].mean().reset_index()


# In[48]:


# Merge the alcohol use data with the birth rates data on 'Year'
merged_data = pd.merge(alcohol_use_agg, birth_rates_agg, on='Year', how='inner')


# In[49]:


# Display the merged DataFrame and the correlation matrix
print(merged_data)
print(correlation)


# In[ ]:





# In[ ]:




