# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 15:49:41 2023

@author: Martin Jakob Steil
@brief: Plots of different solutions of the heat equation (he)
"""

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../graphics/'))
from plot_utils import *

import numpy as np
import json

## ************ Data import and processing ************ ##

with open('he_P1s.json') as json_file:
    dataP1 = json.load(json_file)
    
with open('he_P2s.json') as json_file:
    dataP2 = json.load(json_file)
    
## ************ Figure ************ ##

fig, ((ax00, ax01)) = plt.subplots(1, 2, sharey=True)
fig.subplots_adjust(hspace=0.025)  # adjust space between axes
# *------*------*
# | ax00 | ax01 |
# *------*------*

t0=min(dataP1['ti'])
t1=max(dataP1['ti'])
dt=t1-t0
c=get_color_list(colors[0],colors[1],101)
cP1=[c[math.ceil((t-t0)/dt*100)] for t in dataP1['ti']]
c4=blend_color(cP1[-1],black)

plot_styles={'linewidth': 1.,'linestyle':'-'}
point_styles={'linestyle': 'none','marker': '.','markersize': 3}
   

for i in range(len(cP1)):
    ax00.plot(dataP1['xi'],dataP1['uitRef'][i],color=cP1[i],label=dataP1['labels'][i],**plot_styles)
    ax00.plot(dataP1['xi'],dataP1['uit'][i],color=cP1[i],**point_styles)     

for i in range(len(cP1)):
    # ax01.plot(dataP2['xi'],dataP2['uitRef'][i],color=cP2[i],**plot_styles)
    ax01.plot(dataP2['xi'],dataP2['uit'][i],color=cP1[i],**point_styles,label=dataP2['labels'][i]) 
i=3
ax01.plot(dataP2['xi'],dataP2['uit'][i],color=c4,**point_styles,label=dataP2['labels'][i]) 


ax00.set_ylabel("$u(t,x)$")
ax00.set_ylim(0.45,1.75)
ax00.set_xlabel("$x$")
ax00.set_xlim(0,1)
ax01.set_xlabel("$x$")
ax01.set_xlim(0,1)

ax00.legend(numpoints=1,loc='lower left')
ax00.text(0.97, 0.88, '\\textbf{(a)} Dirichlet BC -- Heat bath',
          horizontalalignment='right', verticalalignment='bottom', transform=ax00.transAxes,
          bbox=end_box_style)


ax01.legend(numpoints=1,loc='lower left') 
ax01.text(0.97, 0.88, '\\textbf{(b)} Neumann BC -- Isolated',
          horizontalalignment='right', verticalalignment='bottom', transform=ax01.transAxes,
          bbox=end_box_style)


# Export
set_height_twoCol(fig, height=5.5)

save_plot(fig, 'hes.pdf')