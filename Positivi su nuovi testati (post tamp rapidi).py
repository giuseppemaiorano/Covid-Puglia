#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns


# In[6]:


df = pd.read_csv("Coronavirus Italia_Main Dashboard_Time series (71).csv")


# In[7]:


df


# In[9]:


plt.figure(figsize=[15,10])
plt.grid(True)
plt.plot(df['Date'] , df['Tested Positive (weekly)'], label='Positivi settimanali', linewidth=5, color='blue')
plt.xlabel('Data')
plt.xticks(rotation=30)
plt.ylabel('Positivi settimanali')
plt.title("Positivi settimanali", fontsize=20)
plt.legend(loc=2)


# In[14]:


x = np.array(range(0,27))
m, b = np.polyfit(x, df['Tested Positive (weekly)'], 1)


# In[27]:


plt.figure(figsize=[15,10])
plt.grid(True)
plt.plot(df['Date'] , df['Tested Positive (weekly)'], label='Positivi su nuovi testati (settimanali)', linewidth=8, color='blue')
plt.plot(x, m*x + b, label='fit', color='orange', linewidth=6)
plt.xlabel('Data')
plt.xticks(rotation=30)
plt.ylabel('Positivi su nuovi testati (settimanali)')
plt.title("Positivi su nuovi testati (settimanali) in Puglia", fontsize=23)
plt.legend(loc=1)

