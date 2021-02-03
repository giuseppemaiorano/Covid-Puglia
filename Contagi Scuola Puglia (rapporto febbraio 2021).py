#!/usr/bin/env python
# coding: utf-8

# #                      Rapporto Covid/Scuole per Regione Puglia
# 
# I dati si rifericono ai contagi dei soli studenti dalla prima all'undicesima settimana dell'anno scolastico, ad esclusione della nona e decima, che il Ministero non ha inserito causa monitoraggio sospeso. Gli studenti presi in considerazione appartengono sia al primo che al secondo ciclo. Ringrazio la redazione di "Wired" e Riccardo Saporiti che attraverso un FOIA (Freedom of Information Act), hanno ottenuto i dati dal Ministero

# In[71]:


#Importo le librerie che mi servono
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[83]:


#Realizzo il dataframe sulla positivià degli alunni
df = pd.DataFrame({"settimane" : [1, 2, 3, 4, 5, 6, 7, 8, 11],
                   "alunni_pos" : [27, 39, 90, 232, 330, 507, 683, 518, 416]})
    #N.B. I dati della nona e decima settimana non sono stati resi pubblici dal Ministero


# In[84]:


df.head() #controllo la realizzazione del DF


# In[98]:


# Realizzo il grafico

plt.figure(figsize=[10,6])
plt.grid(True)
plt.plot(df['settimane'], df['alunni_pos'], label='Alunni Positivi', linewidth=6, linestyle='solid')
plt.xlabel('Settimane')
plt.ylabel('Alunni Positivi')
plt.title("Andamento Casi di Positività tra Alunni in Puglia", fontsize=20)
plt.legend(loc=2)


# In[100]:


#Realizzo il DF sul numero degli alunni in quarantena
quar = pd.DataFrame({"settimane" : [1, 2, 3, 4, 5, 6, 7, 8, 11],
                    "alunni_quar": [26, 154, 659, 1672, 2226, 5396, 7241, 5512, 5775]})


# In[101]:


quar.head() #controllo


# In[114]:


#Grafico
plt.figure(figsize=[10,6])
plt.grid(True)
plt.plot(quar['settimane'], quar['alunni_quar'], label='Alunni in Quarantena', linewidth=6, linestyle='solid',
        color='orange')
plt.plot(df['settimane'], df['alunni_pos'], label='Alunni Positivi', linewidth=3, linestyle='solid')
plt.xlabel('Settimane')
plt.ylabel('Alunni in Quarantena')
plt.title("Alunni positivi e in Quarantena in Puglia", fontsize=20)
plt.legend(loc=2)


# In[113]:


#Utilizzo l'estensione "XKCD" per rendere i grafici più carini
with plt.xkcd():
    plt.grid(True)
plt.plot(df['settimane'], df['alunni_pos'], label='Alunni Positivi', linewidth=6, linestyle='solid')
plt.plot(quar['settimane'], quar['alunni_quar'], label='Alunni in Quarantena', linewidth=6, linestyle='solid',
        color='orange')
plt.xlabel('Settimane')
plt.ylabel('Alunni Positivi')
plt.title("Alunni positivi e in quarantena in Puglia", fontsize=18)
plt.legend(loc=2)
plt.figure(figsize=[25,20])


# In[108]:


with plt.xkcd():
    plt.grid(True)
plt.plot(df['settimane'], df['alunni_pos'], label='Alunni Positivi', linewidth=6, linestyle='solid')
plt.xlabel('Settimane')
plt.ylabel('Alunni Positivi')
plt.title("Andamento Casi di Positività tra Alunni in Puglia", fontsize=20)
plt.legend(loc=2)
plt.figure(figsize=[25,20])

