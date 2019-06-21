#!/usr/bin/env python
# coding: utf-8

# In[173]:


import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
import pandas as pd
import seaborn as sns
import os
sns.set_style('whitegrid')

os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Bathy.csv")
#df

fig, axes = plt.subplots(6, 1, figsize=(12,14), sharex=True, sharey=False)
plt.suptitle('Geomorphology of the Mariana Trench: cross-section of the 25 bathymetric profiles', 
             x=0.54, y=.99, fontsize=12)

fig = df.plot(x='observ', y=['profile1', 'profile2', 'profile3', 'profile4', 'profile5'], 
              linestyle='-', linewidth='.8', cmap=cm.Set1, ax=axes[0])
axes[0].annotate('A', xy=(-.05, .94), xycoords="axes fraction", fontsize=12,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
axes[0].legend(loc='upper right', bbox_to_anchor=(1.12, 1.1),
          ncol=1, fancybox=True, shadow=False)

fig = df.plot(x='observ', y=[ 'profile6', 'profile7', 'profile8', 'profile9', 'profile10'], 
              linestyle='-', linewidth='.8', cmap=cm.tab20, ax=axes[1])
axes[1].annotate('B', xy=(-.05, .94), xycoords="axes fraction", fontsize=12,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
axes[1].legend(loc='upper right', bbox_to_anchor=(1.13, 1.06),
          ncol=1, fancybox=True, shadow=False)

fig = df.plot(x='observ', y=['profile11', 'profile12', 'profile13', 'profile14',], 
              linestyle='-', linewidth='.8', cmap=cm.tab10, ax=axes[2])
axes[2].annotate('C', xy=(-.05, .94), xycoords="axes fraction", fontsize=12,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
axes[2].legend(loc='upper right', bbox_to_anchor=(1.13, 1.05),
          ncol=1, fancybox=True, shadow=False)

fig = df.plot(x='observ', y=['profile15', 'profile16', 'profile17', 'profile18'], 
              linestyle='-', linewidth='.8', cmap=cm.cool, ax=axes[3])
axes[3].annotate('D', xy=(-.05, 1.0), xycoords="axes fraction", fontsize=12,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
axes[3].legend(loc='upper right', bbox_to_anchor=(1.13, 1.05),
          ncol=1, fancybox=True, shadow=False)

fig = df.plot(x='observ', y=['profile19', 'profile20', 'profile21', 'profile22',], 
              linestyle='-', linewidth='.8', cmap=cm.viridis, ax=axes[4])
axes[4].annotate('E', xy=(-.05, .96), xycoords="axes fraction", fontsize=12,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
axes[4].legend(loc='upper right', bbox_to_anchor=(1.13, 1.05),
          ncol=1, fancybox=True, shadow=False)

fig = df.plot(x='observ', y=['profile23', 'profile24', 'profile25'], 
              linestyle='-', linewidth='.8', cmap=cm.jet, ax=axes[5])
axes[5].annotate('F', xy=(-.05, .94), xycoords="axes fraction", fontsize=12,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
axes[5].legend(loc='upper right', bbox_to_anchor=(1.13, 1.05),
          ncol=1, fancybox=True, shadow=False)

plt.xticks(np.arange(0, 518, step=50))

plt.xlabel('Observation samples', fontsize=10, fontfamily='sans-serif')
plt.ylabel('Depths, m', fontsize=10, fontfamily='sans-serif')
plt.show()


# In[ ]:




