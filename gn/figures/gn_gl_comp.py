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

with open('gn_gl_comp.json') as json_file:
    raw = json.load(json_file)


## ************ Figure ************ ##
fig, (ax00, ax01) = plt.subplots(1, 2, sharex=False, sharey=False)
fig.subplots_adjust(hspace=0.025)  # adjust space between axes

    
# Styling
plot_styles={'linewidth': 1.,'linestyle':'-'}
plot_styles2={'linewidth': 1.,'linestyle':':'}
point_styles={'linestyle': 'none','marker': '*','markersize': 5}
point_styles2={'linestyle': 'none','marker':'.','markersize': 3,'alpha':.65}


def plot_data(ax,legQ):
    refdat=raw["ref"]
    for i in range(len(refdat)):
        dat=np.array(refdat[i])
        ax.plot(dat[:,0],dat[:,1],c=black,**plot_styles)

    ax.plot(raw["2nd"][0],raw["2nd"][1],c=colors[1],label="$\\alpha_2=0, 2^\mathrm{nd}$ PB",**plot_styles)
    ax.plot(raw["lS"][0],raw["lS"][1],c=colors[1],label="$\\alpha_2=0,$ LSL",**plot_styles2)
    ax.plot(raw["rS"][0],raw["rS"][1],c=colors[2],label="$\\eta_2=\\tfrac{1}{3},$ RSL",**plot_styles2)
    ax.plot(raw["1st"][0],raw["1st"][1],c=colors[2],label="$\\eta_2=\\tfrac{1}{4}, 1^\mathrm{st}$ PB",**plot_styles)

    ax.plot(raw["a40"][0],raw["a40"][1],c=colors[0],label="$\\alpha_4=0$",**plot_styles2)
    ax.plot(raw["a60"][0][0],raw["a60"][0][1],label="$\\alpha_6=0$",c=colors[4],**plot_styles2)
    ax.plot(raw["a60"][1][0],raw["a60"][1][1],c=colors[4],**plot_styles2)
    ax.plot(raw["testpts"][0],raw["testpts"][1],c=gu_colors['magenta'],**point_styles2)
    ax.plot(raw["cp"][0],raw["cp"][1],c=black,**point_styles)
    if legQ:
        ax.legend(loc=1)

ax00.text(0.3, 0.625, r'$\alpha_2>0$', fontsize=font_size)
ax00.text(0.3, 0.125, r'$\alpha_4<0$', fontsize=font_size)
ax00.text(0.75, 0.3, r'$\alpha_6>0$', fontsize=font_size)


ax00.set_xlabel("$\mu$")
ax01.set_xlabel("$\mu$")
ax00.set_xlim((-0.015,1))

ax00.set_ylabel("$T$")
ax01.set_ylabel("$T$")
ax00.set_ylim((0,0.7))

# Subplot marker
ax00.text(0.15, 0.88, '\\textbf{(a)}',
          horizontalalignment='right', verticalalignment='bottom', transform=ax00.transAxes,
          bbox=end_box_style)


ax01.text(0.15, 0.88, '\\textbf{(b)}',
          horizontalalignment='right', verticalalignment='bottom', transform=ax01.transAxes,
          bbox=end_box_style)

x0=0.6
dx=0.1
y0=0.2
dy=0.15
ax01.set_xlim(x0, x0+dx)  # Set zoom range for x-axis
ax01.set_ylim(y0, y0+dy)  # Set zoom range for y-axis
rect = patches.Rectangle((x0, y0), dx, dy, linewidth=1, edgecolor=gray, facecolor='none',zorder=10)
ax00.add_patch(rect)

plot_data(ax00,False)
plot_data(ax01,True)


# Export
set_height_twoCol(fig, height=6)

save_plot(fig, 'gn_gl_comp.pdf')