#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[27]:


df = pd.DataFrame({"Giorni" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
    'accessi_ps' : [293, 243, 363, 263, 374, 289, 332, 296, 205, 298, 269, 443, 379, 321, 288, 365, 251, 278, 282, 294, 278]})
                                   
                                   


# In[28]:


df.head(30)


# In[29]:


for i in range(0,df.shape[0]-2):
    df.loc[df.index[i+2],'SMA_3'] = np.round(((df.iloc[i,1]+ df.iloc[i+1,1] +df.iloc[i+2,1])/3),1)


# In[30]:


df['pandas_SMA_3'] = df.iloc[:,1].rolling(window=3).mean()


# In[31]:


plt.figure(figsize=[15,10])
plt.grid(True)
plt.plot(df['Giorni'], df['accessi_ps'], label='Accessi Pronto Soccorso CoViD', linewidth=2, linestyle='--')
plt.plot(df['SMA_3'],label='Media Mobile 3 giorni', linewidth=8)
plt.xlabel('Giorni')
plt.ylabel('Accessi PS')
plt.title("Andamento Accessi Pronto Soccorso Sospetto Covid Puglia", fontsize=20)
plt.legend(loc=2)


# In[32]:


for i in range(0,df.shape[0]-6):
    df.loc[df.index[i+6],'SMA_7'] = np.round(((df.iloc[i,1]+ df.iloc[i+1,1] +df.iloc[i+2,1]+df.iloc[i+3,1]+ df.iloc[i+4,1]+ df.iloc[i+5,1]+ df.iloc[i+6,1])/7),1)


# In[33]:


df['pandas_SMA_7'] = df.iloc[:,1].rolling(window=7).mean()


# In[37]:


plt.figure(figsize=[20,10])
plt.grid(True)
plt.plot(df['Giorni'], df['accessi_ps'], label='Accessi Pronto Soccorso CoViD', linewidth=2, linestyle='--')
plt.plot(df['SMA_7'],label='Media Mobile 7 giorni', linewidth=8)
plt.xlabel('Giorni')
plt.ylabel('Accessi PS')
plt.title("Andamento Accessi Pronto Soccorso Sospetto Covid Puglia", fontsize=20)
plt.legend(loc=2)


# In[47]:


plt.figure(figsize=[20,10])
plt.bar(df["Giorni"], df["accessi_ps"], color=(1, 0, 0, 0.4),  edgecolor='blue')
plt.plot(df['SMA_7'],label='Media Mobile 7 giorni', linewidth=6, color='blue')
plt.xlabel('Giorni', fontsize=20)
plt.ylabel('Accessi PS', fontsize=20)
plt.title("Andamento accessi pronto soccorso sospetto covid Puglia", fontsize=30)
plt.legend(loc=2)

