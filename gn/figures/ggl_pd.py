# -*- coding: utf-8 -*-
"""
@author Martin Jakob Steil
@date 2024-07-01T16:20
@brief Plots of different solutions of the euler equation with gravity (ee_grav)
"""

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../graphics/'))
from plot_utils import *

import numpy as np
import json
import matplotlib.patches as patches

## ************ Data import and processing ************ ##

with open('ggl_pd.json') as json_file:
    dat = json.load(json_file)


## ************ Figure ************ ##
fig, ax00 = plt.subplots()
    
# Styling
plot_styles={'linewidth': 1.,'linestyle':'-'}
plot_styles2={'linewidth': 1.,'linestyle':'-'}
point_styles={'linestyle': 'none','marker': '*','markersize': 5}

ax00.plot(dat["refHBPtoIP"][0],dat["refHBPtoIP"][1],c=black,**plot_styles)
ax00.plot(dat["refHBPtoSP"][0],dat["refHBPtoSP"][1],c=black,**plot_styles)
ax00.plot(dat["refIPtoSP"][0],dat["refIPtoSP"][1],c=black,**plot_styles)
ax00.plot(dat["refLP"][0],dat["refLP"][1],c=black,**point_styles)

ax00.plot(dat["eta1"][0],dat["eta1"][1],label=r"$\eta_2=\frac{5}{27}$",c=colors[0],**plot_styles)
ax00.plot(dat["eta2"][0],dat["eta2"][1],label=r"$\eta_2=\frac{1}{2}$",c=colors[1],**plot_styles)
ax00.legend(loc=0)

ax00.set_xlabel("$\mu$")
ax00.set_ylabel("$T$")

x0=0.5
dx=0.5
y0=0.0
dy=0.6
ax00.set_xlim(x0,x0+dx)
ax00.set_ylim(y0,y0+dy)




# ax00.text(0.025, 0.44, r'BP', fontsize=font_size)
# ax00.text(0.16, 0.55, r'SP', fontsize=font_size)

# ax00.text(0.14, 0.25, r'C', fontsize=font_size)

# Export
set_size(fig,height=6)
plt.tight_layout(pad=0.3)
 
save_plot(fig, 'ggl_pd.pdf')