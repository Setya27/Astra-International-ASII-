#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('config', 'Completer.use_jedi = False')


# In[2]:


# Import Libraries and Load Dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

ASII = pd.read_csv('ASII.JK.csv', parse_dates=True, squeeze=True)
df = ASII.copy()


# In[3]:


# Exploratory Data Analysis
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month_name()
newdf = df.iloc[2335:][['Year','Month','Close']]
newdf = newdf.reset_index()
newdf.rename({'Close': 'ASII'}, axis=1, inplace=True)
mydata = newdf.groupby(['Year', 'Month'])[['ASII']].mean()
result = mydata.unstack()
result = result.droplevel(0, axis=1)
result = result[['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']]
result = result.transpose()


# In[4]:


result.style.highlight_min(color = 'lightgreen', axis = 0)


# In[5]:


# Data Visualization
f, ax = plt.subplots(figsize=(15,8))
sns.lineplot(data=result)
plt.legend(loc='lower right')
plt.title('Astra International (ASII)')

