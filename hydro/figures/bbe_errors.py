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
  
with open('bbe_errors.json') as json_file:
    dataError = json.load(json_file)
    
## ************ Figure ************ ##

fig, ((ax00, ax01)) = plt.subplots(1, 2, sharey=False)
fig.subplots_adjust(hspace=0.025)  # adjust space between axes
# *------*------*
# | ax00 | ax01 |
# *------*------*

cti=get_color_list(colors[0],colors[1],len(dataError['forward'][0]))

plot_styles={'linewidth': 1.5,'linestyle':'--'}
point_styles={'linestyle': 'none','marker': '.','markersize': 3}
   

segs=[]
for i in range(len(cti)-1):
    x1 = dataError['CTVD'][0][i]
    y1 = dataError['CTVD'][1][i]
    x2 = dataError['CTVD'][0][i+1]
    y2 = dataError['CTVD'][1][i+1]
    segs.append(((x1, y1), (x2, y2)))

ln_coll = matplotlib.collections.LineCollection(segs,colors=cti, linewidth=1.5, linestyle='solid', capstyle='round')
ax00.add_collection(ln_coll)

ax00.set_xlabel("$2\,\\uppi\,t$")
ax00.set_xlim(0,2)
ax00.set_ylim(0,0.25)
ax00.set_ylabel("$\\mathcal{C}_\\mathrm{TV}[ \{ \\bar{u}_j (t) \} ] $")

segs=[]
for i in range(len(cti)-1):
    x1 = dataError['forward'][0][i]
    y1 = dataError['forward'][1][i]
    x2 = dataError['forward'][0][i+1]
    y2 = dataError['forward'][1][i+1]
    segs.append(((x1, y1), (x2, y2)))

ln_coll = matplotlib.collections.LineCollection(segs,colors=cti,linewidth=1.5, linestyle='solid', capstyle='round')
ax01.add_collection(ln_coll)


ax01.plot(dataError['backward1'][0],dataError['backward1'][1],color=cti[math.floor(len(dataError['forward'][0])*1.0/2.0)],**plot_styles)
ax01.plot(dataError['backward2'][0],dataError['backward2'][1],color=cti[-1],**plot_styles)
ax01.plot(dataError['backward1.25'][0],dataError['backward1.25'][1],color=cti[math.floor(len(dataError['forward'][0])*1.25/2.0)],**plot_styles)

ax01.set_xlabel("$2\,\\uppi\,t$")
ax01.set_xlim(-0.05,2.05)
ax01.set_xticks([0,0.5,1,1.5,2])
ax01.set_ylabel("$\\epsilon_{L^1}(t)$")
ax01.set_yscale("log")
# ax01.set_ylim(1E-5,1E-2)

ax00.text(0.97, 0.88, '\\textbf{(a)}',
          horizontalalignment='right', verticalalignment='bottom', transform=ax00.transAxes,
          bbox=end_box_style)

ax01.text(0.97, 0.88, '\\textbf{(b)}',
          horizontalalignment='right', verticalalignment='bottom', transform=ax01.transAxes,
          bbox=end_box_style)

# Export
set_height_twoCol(fig, height=5.5)

save_plot(fig, 'bbe_errors.pdf')