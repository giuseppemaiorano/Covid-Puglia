#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


df = pd.read_csv("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-summary-latest.csv")


# In[3]:


df.head(20)


# In[4]:


df = df.loc[df["area"]=="PUG"]


# In[5]:


df.head()


# In[6]:


df = df[['area', 'totale']]


# In[7]:


df.head()


# In[8]:


for i in range(0,df.shape[0]-2):
    df.loc[df.index[i+2],'SMA_3'] = np.round(((df.iloc[i,1]+ df.iloc[i+1,1] +df.iloc[i+2,1])/3),1)


# In[9]:


df['pandas_SMA_3'] = df.iloc[:,1].rolling(window=3).mean()


# In[10]:


df.head()


# In[11]:


plt.figure(figsize=[15,10])
plt.grid(True)
plt.plot(df['totale'],label='Dosi Somministrate', linewidth=2, linestyle='--')
plt.plot(df['SMA_3'],label='Media Mobile 3 giorni', linewidth=8)
plt.xlabel('Giorni')
plt.ylabel('Dosi Somministrate')
plt.title("Andamento Dosi Somministrate Vaccino Puglia", fontsize=20)
plt.legend(loc=2)


# In[12]:


for i in range(0,df.shape[0]-6):
    df.loc[df.index[i+6],'SMA_7'] = np.round(((df.iloc[i,1]+ df.iloc[i+1,1] +df.iloc[i+2,1]+df.iloc[i+3,1]+ df.iloc[i+4,1]+ df.iloc[i+5,1]+ df.iloc[i+6,1])/7),1)


# In[13]:


df['pandas_SMA_7'] = df.iloc[:,1].rolling(window=7).mean()


# In[14]:


plt.figure(figsize=[15,10])
plt.grid(True)
plt.plot(df['totale'],label='Dosi Somministrate', linewidth=2, linestyle='--')
plt.plot(df['SMA_7'],label='Media Mobile 7 giorni', linewidth=8)
plt.xlabel('Tempo')
plt.ylabel('Dosi Somministrate')
plt.title("Andamento Dosi Somministrate Vaccino Puglia", fontsize=20)
plt.legend(loc=2)


# In[ ]:




