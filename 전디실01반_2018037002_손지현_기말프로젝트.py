#!/usr/bin/env python
# coding: utf-8

# In[109]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.read_csv('../data/top50.csv')  # Top 50 Spotify Songs - 2019


# In[63]:


df1


# In[89]:


songs = df1[['Track.Name', 'Artist.Name', 'Genre', 'Beats.Per.Minute']] 


# In[90]:


songs


# In[110]:


grouped_songs= songs.groupby('Genre')['Track.Name']
grouped_songs.nunique()


# In[104]:


BPM = songs['Beats.Per.Minute']
print(BPM.mean())


# In[102]:


songs[songs['Beats.Per.Minute']>117]


# In[105]:


scatter_plot = plt.figure() 
axes1 = scatter_plot.add_subplot(1, 1, 1) 
axes1.scatter(songs['Track.Name'], songs['Beats.Per.Minute']) 
axes1.set_title('BPM') 
axes1.set_xlabel('Track.Name') 
axes1.set_ylabel('BPM')


# In[108]:


ax = plt.subplots() 
ax = sns.boxplot(y='Beats.Per.Minute', data=songs) 
ax.set_title('BPM') 
ax.set_xlabel('Track.Name') 
ax.set_ylabel('BPM')

