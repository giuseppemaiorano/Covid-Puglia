#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[38]:


df = pd.read_csv("Nuovi-ingressi-terapia-intensiva-Puglia.csv", sep=";")
df.head(10)


# In[44]:


plt.figure(figsize=[15,10])
plt.grid(True)
plt.plot(df['giorno'], df['ingressi_terapia_intensiva'], label='ingressi_terapia_intensiva', linewidth=2, linestyle='--')
plt.xlabel('Giorni')
plt.ylabel('Ingressi TI')
plt.title("ingressi_terapia_intensiva", fontsize=20)
plt.legend(loc=2)


# In[41]:


for i in range(0,df.shape[0]-2):
    df.loc[df.index[i+2],'SMA_3'] = np.round(((df.iloc[i,1]+ df.iloc[i+1,1] +df.iloc[i+2,1])/3),1)


# In[42]:


df['pandas_SMA_3'] = df.iloc[:,1].rolling(window=3).mean()


# In[43]:


df.head()


# In[52]:


plt.figure(figsize=[15,10])
plt.grid(True)
plt.plot(df['giorno'], df['ingressi_terapia_intensiva'], label='Ingressi terapia intensiva Puglia ', linewidth=2, linestyle='--')
plt.plot(df['SMA_3'],label='Media Mobile 3 giorni', linewidth=8)
plt.xlabel('Giorni')
plt.xticks(rotation=90)
plt.ylabel('Ingressi TI')
plt.title("Ingressi terapia intensiva Puglia", fontsize=20)
plt.legend(loc=2)


# In[46]:


for i in range(0,df.shape[0]-6):
    df.loc[df.index[i+6],'SMA_7'] = np.round(((df.iloc[i,1]+ df.iloc[i+1,1] +df.iloc[i+2,1]+df.iloc[i+3,1]+ df.iloc[i+4,1]+ df.iloc[i+5,1]+ df.iloc[i+6,1])/7),1)


# In[47]:


df['pandas_SMA_7'] = df.iloc[:,1].rolling(window=7).mean()


# In[53]:


plt.figure(figsize=[15,10])
plt.grid(True)
plt.plot(df['giorno'], df['ingressi_terapia_intensiva'], label='Ingressi terapia intensiva Puglia', linewidth=2, linestyle='--', color='red')
plt.plot(df['SMA_7'],label='Media Mobile 7 giorni', linewidth=8)
plt.xlabel('Giorni')
plt.xticks(rotation=90)
plt.ylabel('Ingressi TI')
plt.title("Ingressi terapia intensiva Puglia", fontsize=20)
plt.legend(loc=2)


# In[ ]:




