# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 12:43:00 2021

@author: Martin Jakob Steil
@brief: Plots for different regulator shape functions and their derivatives
@see: https://matplotlib.org/stable/gallery/subplots_axes_and_figures/broken_axis.html
@see: https://stackoverflow.com/a/46921590
"""

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../graphics/'))
from plot_utils import *

import numpy as np
import json

## ************ Data import and processing ************ ##

with open('regulator_shape_functions.json') as json_file:
    data = json.load(json_file)
fkts=data['functions']

## ************ Figure ************ ##

fig, ((ax00, ax01), (ax10, ax11)) = plt.subplots(2, 2, sharex=True,  gridspec_kw={'height_ratios': [1, 3]})
fig.subplots_adjust(hspace=0.025)  # adjust space between axes
# *------*------*
# | ax00 | ax01 |
# *------*------*
# | ax10 | ax11 |
# *------*------*
    
# Styling
line_styles=['-',(0,(2,2)),'-']
plot_styles=list(map(lambda i : {
    'color':colors[i],
    'linestyle': line_styles[i],
    'linewidth': 1.5
    },range(3)))

label_names=[r'$\lambda_\mathrm{flat}(y)$',r'$\lambda_\mathrm{sharp}(y)$',r'$\lambda_\mathrm{exp}(y)$']

# Plots
f_i=0
for f in fkts:
    rby1=np.array(data[f]['rby_yi'][0])
    rby2=np.array(data[f]['rby_yi'][1])
    
    drby1=np.array(data[f]['drby_yi'][0])
    drby2=np.array(data[f]['drby_yi'][1])
    
    ax00.semilogx(rby1[:,0],rby1[:,1],**plot_styles[f_i],label=label_names[f_i])
    ax00.semilogx(rby2[:,0],rby2[:,1],**plot_styles[f_i])
    
    ax10.semilogx(rby1[:,0],rby1[:,1],**plot_styles[f_i])
    ax10.semilogx(rby2[:,0],rby2[:,1],**plot_styles[f_i])
    
    
    ax01.semilogx(drby1[:,0],drby1[:,1],**plot_styles[f_i])
    ax01.semilogx(drby2[:,0],drby2[:,1],**plot_styles[f_i])

    ax11.semilogx(drby1[:,0],drby1[:,1],**plot_styles[f_i])
    ax11.semilogx(drby2[:,0],drby2[:,1],**plot_styles[f_i])
    
    
    f_i=f_i+1

# Axes
#left upper
ax00.set_ylim(3.8, 4.05)
ax00.set_yticks([4])
ax00.set_yticklabels([r'$\infty$'])
ax00.set_xlim(1E-2, 1E3)
ax00.spines.bottom.set_visible(False)
ax00.tick_params(
    axis='x',
    which='both',    
    bottom=False,     
    top=False,       
    labelbottom=False,
    labeltop=False
) 

#left lower
ax10.set_ylim(-0.05, 1.5)
ax10.set_yticks([0,0.5,1])
ax10.set_yticklabels(['$0$',r'$\frac{1}{2}$','$1$'])
ax10.set_ylabel(r'$(\lambda(y)-1)\,y\,=\,r(y)\,y$')
ax10.yaxis.set_label_coords(-0.11, 0.75)
  
ax10.set_xlabel(r'$y=p^2/k^2$')
ax10.spines.top.set_visible(False)
ax10.tick_params(
    axis='x',
    which='both',    
    bottom=True,     
    top=False,       
    labelbottom=True,
    labeltop=False
)

#right upper
ax01.set_ylim(3.8, 4.05)
ax01.set_yticks([4])
ax01.set_yticklabels([r'$\infty$'])
ax01.set_xlim(1E-2, 1E3)

ax01.spines.bottom.set_visible(False)
ax01.tick_params(
    axis='x',
    which='both',    
    bottom=False,     
    top=False,       
    labelbottom=False,
    labeltop=False
) 

#right lower
ax11.set_ylim(-0.05, 2.5)
ax11.set_yticks([0,0.5,1,1.5,2])
ax11.set_yticklabels(['$0$',r'$\frac{1}{2}$','$1$',r'$\frac{3}{2}$','$2$'])
ax11.set_xlabel(r'$y=p^2/k^2$')

ax11.set_ylabel(r'$-2\,y\,\partial_y(r(y)\,y)$')
ax11.yaxis.set_label_coords(-0.11, 0.75)

ax11.spines.top.set_visible(False)
ax11.tick_params(
    axis='x',
    which='both',    
    bottom=True,     
    top=False,       
    labelbottom=True,
    labeltop=False
)

# y-axes cuts
d = .5  # proportion of vertical to horizontal extent of the slanted line
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=6,
              linestyle="none", color='k', mec='k', mew=1, clip_on=False)
ax00.plot([0, 1], [0, 0], transform=ax00.transAxes, **kwargs)
ax10.plot([0, 1], [1, 1], transform=ax10.transAxes, **kwargs)
ax01.plot([0, 1], [0, 0], transform=ax01.transAxes, **kwargs)
ax11.plot([0, 1], [1, 1], transform=ax11.transAxes, **kwargs)

#free floating plot legend https://stackoverflow.com/a/46921590
handles, labels = ax00.get_legend_handles_labels()
fig.legend(handles, labels, loc='upper right', handlelength=1.5, numpoints=1, bbox_to_anchor = (0,0.,.955,.96), bbox_transform = plt.gcf().transFigure)
#fig.legend(handles, labels, loc='upper right', handlelength=1.5, numpoints=1, bbox_to_anchor = (0,0.,.45,.96), bbox_transform = plt.gcf().transFigure)

#plt.show()

ax10.text(0.95,-2.9, '\\textbf{(a)}',
          horizontalalignment='right', verticalalignment='top', transform=ax00.transAxes,
          bbox=end_box_style)
ax11.text(0.95, -2.9, '\\textbf{(b)}',
          horizontalalignment='right', verticalalignment='top', transform=ax01.transAxes,
          bbox=end_box_style)

# Export
set_height_twoCol(fig, height=7)
plt.tight_layout(pad=0.5, h_pad=1.0, w_pad=1.5)

save_plot(fig, 'regulator_shape_functions.pdf')