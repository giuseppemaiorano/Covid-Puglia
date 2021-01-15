#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib


# In[3]:


df = pd.read_csv("Coronavirus Italia_Main Dashboard_Time series (49).csv")
df.head()


# In[4]:


for i in range(0,df.shape[0]-13):
    df.loc[df.index[i+13],'SMA_14'] = np.round(((df.iloc[i,1]+ df.iloc[i+1,1] +df.iloc[i+2,1]+df.iloc[i+3,1]+ df.iloc[i+4,1]+ df.iloc[i+5,1]+ df.iloc[i+6,1]+ df.iloc[i+7,1]+ df.iloc[i+8,1]+ df.iloc[i+9,1]+ df.iloc[i+10,1]+ df.iloc[i+11,1]+ df.iloc[i+12,1]+ df.iloc[i+13,1])/14),1)


# In[5]:


df['pandas_SMA_14'] = df.iloc[:,1].rolling(window=14).mean()


# In[6]:


plt.figure(figsize=[15,10])
plt.grid(True)
plt.plot(df['Daily Recovered'],label='Guariti Giornalieri', linewidth=2, linestyle='--')
plt.plot(df['SMA_14'],label='Media Mobile 14 giorni', linewidth=8)
plt.xlabel('Data')
plt.ylabel('Guariti Giornalieri')
plt.title("Andamento Guariti Puglia (Seconda Ondata)", fontsize=20)
plt.legend(loc=2)

