#!/usr/bin/env python
# coding: utf-8

# In[7]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[8]:


df = pd.read_csv("Coronavirus Italia_Main Dashboard_Time series (56).csv")


# In[9]:


df.head()


# In[10]:


for i in range(0,df.shape[0]-6):
    df.loc[df.index[i+6],'SMA_7'] = np.round(((df.iloc[i,1]+ df.iloc[i+1,1] +df.iloc[i+2,1]+df.iloc[i+3,1]+ df.iloc[i+4,1]+ df.iloc[i+5,1]+ df.iloc[i+6,1])/7),1)


# In[11]:


df['pandas_SMA_7'] = df.iloc[:,1].rolling(window=7).mean()


# In[12]:


plt.figure(figsize=[15,10])
plt.grid(True)
plt.plot( df['Intensive Care'],label='TI', linewidth=2, linestyle="--")
plt.plot(df['SMA_7'],label='Media Mobile 7 giorni', linewidth=7)
plt.xlabel('Data')
plt.ylabel('Posti occupati TI')
plt.title("Andamento Posti Occupati Terapia Intensiva Puglia", fontsize=20)
plt.legend(loc=2)


# In[13]:


for i in range(0,df.shape[0]-13):
    df.loc[df.index[i+13],'SMA_14'] = np.round(((df.iloc[i,1]+ df.iloc[i+1,1] +df.iloc[i+2,1]+df.iloc[i+3,1]+ df.iloc[i+4,1]+ df.iloc[i+5,1]+ df.iloc[i+6,1]+ df.iloc[i+7,1]+ df.iloc[i+8,1]+ df.iloc[i+9,1]+ df.iloc[i+10,1]+ df.iloc[i+11,1]+ df.iloc[i+12,1]+ df.iloc[i+13,1])/14),1)


# In[14]:


df['pandas_SMA_14'] = df.iloc[:,1].rolling(window=14).mean()


# In[15]:


plt.figure(figsize=[15,10])
plt.grid(True)
plt.plot( df['Intensive Care'],label='TI', linewidth=2, linestyle='--')
plt.plot(df['SMA_14'],label='Media Mobile 14 giorni', linewidth=7)
plt.xlabel('Data')
plt.ylabel('Posti occupati TI')
plt.title("Andamento Posti Occupati Terapia Intensiva Puglia", fontsize=20)
plt.legend(loc=2)

