#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


df = pd.read_csv("Coronavirus Italia_Main Dashboard_Time series (59).csv")


# In[7]:


df.head()


# In[8]:


for i in range(0,df.shape[0]-9):
    df.loc[df.index[i+9],'SMA_10'] = np.round(((df.iloc[i,1]+ df.iloc[i+1,1] +df.iloc[i+2,1]+df.iloc[i+3,1]+ df.iloc[i+4,1]+ df.iloc[i+5,1]+ df.iloc[i+6,1]+ df.iloc[i+7,1]+ df.iloc[i+8,1]+ df.iloc[i+9,1])/10),1)


# In[9]:


df['pandas_SMA_10'] = df.iloc[:,1].rolling(window=10).mean()


# In[11]:


plt.figure(figsize=[15,10])
plt.grid(True)
plt.plot(df['Daily Deaths'],label='Morti giornalieri', linewidth=3, )
plt.plot(df['SMA_10'],label='Media Mobile 10 giorni', linewidth=6,)
plt.xlabel('Data')
plt.ylabel('Morti giornalieri')
plt.title("Andamento Morti Puglia (Seconda Ondata)", fontsize=20)
plt.legend(loc=2)


# In[ ]:




