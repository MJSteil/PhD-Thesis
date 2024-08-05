# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 15:49:41 2023

@author: Martin Jakob Steil
@brief: Plots of different solutions of the linear advection equation (lae)
"""

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../graphics/'))
from plot_utils import *

import numpy as np
import json

## ************ Data import and processing ************ ##

with open('lae_P1.json') as json_file:
    data = json.load(json_file)
    
with open('lae_P1_L1relError.json') as json_file:
    dataError = json.load(json_file)
    
## ************ Figure ************ ##

fig, ((ax00, ax01)) = plt.subplots(1, 2, sharey=False)
fig.subplots_adjust(hspace=0.025)  # adjust space between axes
# *------*------*
# | ax00 | ax01 |
# *------*------*

t0=min(data['ti'])
t1=max(data['ti'])
dt=t1-t0
cti=get_color_list(colors[0],colors[1],len(dataError['uforward'][0]))
ctiM=get_color_list(colors[2],colors[1],len(dataError['ubackward'][0]))

plot_styles={'linewidth': 1.,'linestyle':'-'}
point_styles={'linestyle': 'none','marker': '.','markersize': 3}
   

for i in range(2):
    ax00.plot(data['xi'],data['uitRef'][i],color=colors[i],label=data['labels'][i],**plot_styles)
    ax00.plot(data['xi'],data['uit'][i],color=colors[i],**point_styles)  
ax00.plot(data['xi'],data['uit'][2],color=colors[2],label=data['labels'][2],**point_styles)         
i=1
# ax01.plot(dataP2['xi'],dataP2['uitRef'][i],color=cP2[i],**plot_styles,label=dataP2['labels'][i])
# ax01.plot(dataP2['xi'],dataP2['uit'][i],color=cP2[i],**point_styles)   

segs=[]
for i in range(len(cti)-1):
    x1 = dataError['uforward'][0][i]
    y1 = dataError['uforward'][1][i]
    x2 = dataError['uforward'][0][i+1]
    y2 = dataError['uforward'][1][i+1]
    segs.append(((x1, y1), (x2, y2)))

ln_coll = matplotlib.collections.LineCollection(segs,colors=cti, linestyle='solid', capstyle='round')
ax01.add_collection(ln_coll)

segs=[]
for i in range(len(ctiM)-1):
    x1 = dataError['ubackward'][0][i]
    y1 = dataError['ubackward'][1][i]
    x2 = dataError['ubackward'][0][i+1]
    y2 = dataError['ubackward'][1][i+1]
    segs.append(((x1, y1), (x2, y2)))

ln_coll = matplotlib.collections.LineCollection(segs,colors=ctiM,linewidth=1.5, linestyle='solid', capstyle='round')
ax01.add_collection(ln_coll)

ax00.set_ylabel("$u(t,x)$")
ax00.set_ylim(-0.1,1.1)
ax00.set_xlabel("$x$")
ax00.set_xlim(0,1)

ax01.set_xlabel("$t$")
ax01.set_xlim(0,0.4)
ax01.set_ylabel("$\\epsilon_{L^1}(t)$")
ax01.set_yscale("log")
ax01.set_ylim(1E-3,1E-1)

ax00.legend(numpoints=1,loc='lower left')
ax00.text(0.97, 0.88, '\\textbf{(a)}',
          horizontalalignment='right', verticalalignment='bottom', transform=ax00.transAxes,
          bbox=end_box_style)

ax01.text(0.97, 0.88, '\\textbf{(b)}',
          horizontalalignment='right', verticalalignment='bottom', transform=ax01.transAxes,
          bbox=end_box_style)

# Export
set_height_twoCol(fig, height=5.5)

save_plot(fig, 'lae_P1.pdf')