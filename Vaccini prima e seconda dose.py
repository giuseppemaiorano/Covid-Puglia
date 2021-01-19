#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[15]:


df = pd.read_csv("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-summary-latest.csv")


# In[20]:


df.head(30)


# In[23]:


df = df.loc[df['area']=='PUG']


# In[24]:


df


# In[25]:


df = df[["data_somministrazione", "prima_dose", "seconda_dose"]]


# In[26]:


df


# In[30]:


for i in range(0,df.shape[0]-6):
    df.loc[df.index[i+6],'SMA_7'] = np.round(((df.iloc[i,1]+ df.iloc[i+1,1] +df.iloc[i+2,1]+df.iloc[i+3,1]+ df.iloc[i+4,1]+ df.iloc[i+5,1]+ df.iloc[i+6,1])/7),1)


# In[31]:


df['pandas_SMA_7'] = df.iloc[:,1].rolling(window=7).mean()


# In[33]:


df.head(10)


# In[36]:


plt.figure(figsize=[15,10])
plt.grid(True)
plt.plot(df['data_somministrazione'], df['seconda_dose'], label='seconda dose', linewidth=5, color='green')
plt.plot(df['data_somministrazione'], df['SMA_7'], label='Media Mobile 7 giorni prima dose', linewidth=5, color='blue')
plt.xlabel('Data')
plt.xticks(rotation=30)
plt.ylabel('Dosi somministrate')
plt.title("Dosi vaccino covid somministrate in Puglia", fontsize=20)
plt.legend(loc=2)


# In[ ]:




