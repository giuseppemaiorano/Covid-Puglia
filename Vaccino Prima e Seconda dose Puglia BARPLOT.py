#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Importo librerie

import numpy as np
import pandas as pd
from matplotlib import style
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns


# In[40]:


#Importo dati da ISS, scelgo solo la regione Puglia e sorto per data di somministrazione

df = pd.read_csv("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-summary-latest.csv")
df = df.loc[df['area']=='PUG']
df = df.sort_values(by=['data_somministrazione'])
df.head(400)


# In[42]:


#controllo le colonne a disposizione
df.columns


# In[53]:


#Scelgo le mie due 'y'
y1 = df['prima_dose']
y2 = df['seconda_dose']


# In[66]:


#linee di codice per il grafico

plt.figure(figsize=[15,10])
plt.style.use("ggplot")
plt.grid(True)
plt.xlabel('Data', fontsize=14)
plt.xticks([0, 15, 30, 45, 60, 75, 90, 105, 120])
plt.ylabel('Dosi somministrate', fontsize=14)
plt.title("Dosi somministrate in Puglia", fontsize=26)
plt.bar(df['data_somministrazione'], y1, label = 'prima dose', color='b')
plt.bar(df['data_somministrazione'], y2, bottom = y1, label = 'seconda dose', color='orange')
plt.legend(loc=2, fontsize=15)


# In[ ]:




