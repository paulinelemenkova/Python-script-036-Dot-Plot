#!/usr/bin/env python
# coding: utf-8
import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import cm
import matplotlib.artist as martist
from matplotlib.offsetbox import AnchoredText
import seaborn as sns

sns.set_style('whitegrid')
sns.set_context("paper")

os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Bathy.csv")

fig, axes = plt.subplots(6, 1, figsize=(12,14), sharex=True, sharey=False, dpi=300)
plt.suptitle('Geomorphology of the Mariana Trench: cross-section of the 25 bathymetric profiles',
             x=0.54, y=.95, fontsize=12)

def add_at(axes, t, loc=2):
    fp = dict(size=11)
    _at = AnchoredText(t, loc=loc, prop=fp)
    axes.add_artist(_at)
    return _at

# subplot 1
fig = df.plot(x='observ', y=['profile1', 'profile2', 'profile3', 'profile4', 'profile5'],
              linestyle='-', linewidth='.8', cmap=cm.Set1, ax=axes[0])
axes[0].legend(loc='upper right', bbox_to_anchor=(1.12, 1.1),
               ncol=1, fancybox=True, shadow=False)
add_at(axes[0], "A")

# subplot 2
fig = df.plot(x='observ', y=[ 'profile6', 'profile7', 'profile8', 'profile9', 'profile10'],
              linestyle='-', linewidth='.8', cmap=cm.tab20, ax=axes[1])
axes[1].legend(loc='upper right', bbox_to_anchor=(1.13, 1.06),
               ncol=1, fancybox=True, shadow=False)
add_at(axes[1], "B")

# subplot 3
fig = df.plot(x='observ', y=['profile11', 'profile12', 'profile13', 'profile14',],
              linestyle='-', linewidth='.8', cmap=cm.tab10, ax=axes[2])
axes[2].legend(loc='upper right', bbox_to_anchor=(1.13, 1.05),
               ncol=1, fancybox=True, shadow=False)
add_at(axes[2], "C")

# subplot 4
fig = df.plot(x='observ', y=['profile15', 'profile16', 'profile17', 'profile18'],
              linestyle='-', linewidth='.8', cmap=cm.cool, ax=axes[3])
axes[3].legend(loc='upper right', bbox_to_anchor=(1.13, 1.05),
               ncol=1, fancybox=True, shadow=False)
add_at(axes[3], "D")

# subplot 5
fig = df.plot(x='observ', y=['profile19', 'profile20', 'profile21', 'profile22',],
              linestyle='-', linewidth='.8', cmap=cm.viridis, ax=axes[4])
axes[4].legend(loc='upper right', bbox_to_anchor=(1.13, 1.05),
               ncol=1, fancybox=True, shadow=False)
add_at(axes[4], "E")

# subplot 6
fig = df.plot(x='observ', y=['profile23', 'profile24', 'profile25'],
              linestyle='-', linewidth='.8', cmap=cm.jet, ax=axes[5])
axes[5].legend(loc='upper right', bbox_to_anchor=(1.13, 1.05),
               ncol=1, fancybox=True, shadow=False)
add_at(axes[5], "F")

plt.xticks(np.arange(0, 518, step=50))
plt.xlabel('Observation samples', fontsize=10, fontfamily='sans-serif')
plt.ylabel('Depths, m', fontsize=10, fontfamily='sans-serif')

# visualizing and saving
plt.tight_layout()
plt.subplots_adjust(top=0.90, bottom=0.08,
                    left=0.10, right=0.85,
                    hspace=0.3, wspace=0.3
                    )
plt.savefig('plot_LinePlot.png', dpi=300)
plt.show()
