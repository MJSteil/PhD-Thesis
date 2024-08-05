# -*- coding: utf-8 -*-
"""
@author Martin Jakob Steil
@date 2023-08-04T11:51
@brief Plots of different solutions of the euler equation with gravity (ee_grav)
"""

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../graphics/'))
from plot_utils import *

import numpy as np
import json
import matplotlib.patches as patches

## ************ Data import and processing ************ ##

with open('gn_gl_ntPD.json') as json_file:
    raw = json.load(json_file)

dat=raw["dat"]

## ************ Figure ************ ##
fig, ax00 = plt.subplots()
    
# Styling
plot_styles={'linewidth': 1.,'linestyle':'-'}
plot_styles2={'linewidth': 1.,'linestyle':'--'}
point_styles={'linestyle': 'none','marker': '*','markersize': 5}


ax00.semilogx(dat[0][0],dat[0][1],c=colors[1],**plot_styles2)

ax00.semilogx(dat[1][0],dat[1][1],c=colors[2],**plot_styles)
ax00.semilogx(dat[2][0],dat[2][1],c=colors[2],**plot_styles)
ax00.semilogx([dat[0][0][-1]],[dat[0][1][-1]],c=colors[1],**point_styles)

ax00.set_ylim(0.24,0.6)
ax00.set_xlabel("$n$")
ax00.set_ylabel("$T$")


ax00.text(0.025, 0.44, r'BP', fontsize=font_size)
ax00.text(0.16, 0.55, r'SP', fontsize=font_size)

ax00.text(0.14, 0.25, r'C', fontsize=font_size)

# Export
set_height_singleCol(fig, height=6)

save_plot(fig, 'gn_gl_ntPD.pdf')