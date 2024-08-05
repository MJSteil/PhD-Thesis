# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 15:49:41 2023

@author Martin Jakob Steil
@brief Plots of different solutions of the Euler equation (ee) for the 
        sod shock tube problem
"""

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../graphics/'))
from plot_utils import *

import numpy as np
import json

## ************ Data import and processing ************ ##

with open('ee_sod.json') as json_file:
    raw = json.load(json_file)
xi=np.array(raw['xi'])
data=np.array(raw['dat'])
data0=np.array(raw['dat0'])

xiRef=np.array(raw['xiRef']) 
dataRef=np.array(raw['datRef']) 
    
## ************ Figure ************ ##

fig, ((ax0)) = plt.subplots(1, 3, sharey=True)
fig.subplots_adjust(hspace=0.0)  # adjust space between axes
# *------*------*------*
# | ax00 | ax01 | ax02 |
# *------*------*------*


colors=list(map(lambda c : gu_colors[c],['goetheBlau','emoRot','gruen']))

plot_styles={'linewidth': 1.0,'linestyle':'-'}
plot0_styles={'linewidth': 1.0,'linestyle':'--'}
point_styles={'linestyle': 'none','marker': '.','markersize': 3}   
abc=['a','b','c']

for i in range(3):
    ax0[i].plot(xi,data[i],color=colors[i],**point_styles)
    ax0[i].plot(xi,data0[i],color=colors[i],label=raw['labels0'][i],**plot0_styles)
    ax0[i].plot(xiRef,dataRef[i],color=colors[i],label=raw['labels'][i],**plot_styles)
    ax0[i].set_xlabel("$x\,(\\mathrm{m})$")
    ax0[i].legend(numpoints=1,loc='upper right')
    ax0[i].set_xlim(0,1)
    ax0[i].text(0.2, 0.1, '\\textbf{('+abc[i]+')}',
              horizontalalignment='right', verticalalignment='top', transform=ax0[i].transAxes,
              bbox=end_box_style)

ax0[0].set_ylabel("$u_i(t,x)$")
ax0[0].set_ylim(-0.1,3.2)

# Export
set_height_twoCol(fig, height=7)
plt.tight_layout(pad=0.5, h_pad=1.0, w_pad=0.75)

save_plot(fig, 'ee_sod.pdf')