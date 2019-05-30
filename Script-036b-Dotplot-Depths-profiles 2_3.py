#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import os
sns.set_style('whitegrid')

os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Bathy.csv")
#df

fig, axes = plt.subplots(3, 2, figsize=(12,14), sharex=True, sharey=False)
plt.suptitle('Geomorphology of the Mariana Trench: cross-section of the 25 bathymetric profiles', 
             x=0.54, y=.92, fontsize=14,)

fig = df.plot(x='observ', y=['profile1', 'profile2', 'profile3', 'profile4', 'profile5'], 
              linestyle=':', ax=axes[0, 0])
axes[0, 0].annotate('A', xy=(-.05, .94), xycoords="axes fraction", fontsize=12,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
axes[0, 0].legend(loc='upper right', bbox_to_anchor=(1.12, 1.05),
          ncol=1, fancybox=True, shadow=False)

fig = df.plot(x='observ', y=[ 'profile6', 'profile7', 'profile8', 'profile9', 'profile10'], 
              linestyle=':', ax=axes[0, 1])
axes[0, 1].annotate('B', xy=(-.05, .94), xycoords="axes fraction", fontsize=12,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
axes[0, 1].legend(loc='upper right', bbox_to_anchor=(1.13, 1.05),
          ncol=1, fancybox=True, shadow=False)

fig = df.plot(x='observ', y=['profile11', 'profile12', 'profile13', 'profile14',], 
              linestyle=':', ax=axes[1, 0])
axes[1, 0].annotate('C', xy=(-.05, .94), xycoords="axes fraction", fontsize=12,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
axes[1, 0].legend(loc='upper right', bbox_to_anchor=(1.13, 1.05),
          ncol=1, fancybox=True, shadow=False)

fig = df.plot(x='observ', y=['profile15', 'profile16', 'profile17', 'profile18'], 
              linestyle=':', ax=axes[1, 1])
axes[1, 1].annotate('D', xy=(-.05, 1.0), xycoords="axes fraction", fontsize=12,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
axes[1, 1].legend(loc='upper right', bbox_to_anchor=(1.13, 1.05),
          ncol=1, fancybox=True, shadow=False)

fig = df.plot(x='observ', y=['profile19', 'profile20', 'profile21', 'profile22',], 
              linestyle=':', ax=axes[2, 0])
axes[2, 0].annotate('E', xy=(-.05, .96), xycoords="axes fraction", fontsize=12,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
axes[2, 0].legend(loc='upper right', bbox_to_anchor=(1.13, 1.05),
          ncol=1, fancybox=True, shadow=False)

fig = df.plot(x='observ', y=['profile23', 'profile24', 'profile25'], 
              linestyle=':', ax=axes[2, 1])
axes[2, 1].annotate('F', xy=(-.05, .94), xycoords="axes fraction", fontsize=12,
           bbox=dict(boxstyle='round, pad=0.3', fc='w', edgecolor='grey', linewidth=1, alpha=0.9))
axes[2, 1].legend(loc='upper right', bbox_to_anchor=(1.13, 1.05),
          ncol=1, fancybox=True, shadow=False)

plt.xticks(np.arange(0, 518, step=50))
plt.xlabel('Observation samples', fontsize=10, fontfamily='sans-serif')
plt.ylabel('Depths, m', fontsize=10, fontfamily='sans-serif')
plt.show()


# In[ ]:




