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
from scipy.interpolate import make_interp_spline, BSpline
from labellines import labelLine, labelLines

## ************ Data import and processing ************ ##

with open('truncation.json') as json_file:
    raw = json.load(json_file)
kIR=raw['kIR']
kUV=raw['kUV']
ki=np.linspace(kIR,kUV,600) #np.concatenate()

names=raw['data']
labels=raw['labels']
data={n:np.array(raw[n]) for n in names}
splines=[make_interp_spline(data[n][:,0],data[n][:,1], k=2) for n in names]


## ************ Figure ************ ##

fig, ax00 = plt.subplots()

    
# Styling
line_styles=['-','--','-','--','-','--']
c=[colors[0],colors[0],colors[1],colors[1],colors[2],colors[2]]
plot_styles=list(map(lambda i : {
    'color':c[i],
    'linestyle': line_styles[i],
    'linewidth': 1.5
    },range(6)))
point_styles=list(map(lambda i : {
    'color':'0',
    'linestyle': 'none',
    'marker': '.',
    'markersize': 5
    },range(6)))

karrowi=[[0.5,3,7,11],[0.5,4,9,11],[0.3,4,7,10],[0.3,4,7,10],[0.7,3,7.5,10],[0.7,3,7.5,10]]
for i in range(6):    
    ax00.plot(ki,splines[i](ki), **plot_styles[i],label=labels[i])#
    
    for k in karrowi[i]:
        ax00.arrow(k,splines[i](k), -0.01, splines[i](k)-splines[i](k+0.01),
                    color=c[i], shape='full', lw=0, length_includes_head=True, head_width=.2)
   
ax00.plot([kUV],[splines[0](kUV)], **point_styles[i]) 
labelLines(ax00.get_lines(), zorder=10,xvals=(5,8,2,1.25,5,2),outline_width=6.5)



ax00.set_ylim(0, 6)
ax00.set_yticks([s(kIR) for s in splines[1:]])
ax00.set_xlim(kIR,kUV+1)
ax00.set_xticks([kIR,kUV])
ax00.set_xticklabels(['$0$','$\Lambda$'])

ax00.annotate('$\overline{\Gamma}_{\Lambda}$', xy=(kUV, splines[0](kUV)), xytext=(2,-12),textcoords='offset points')

ax00.set_yticklabels([
    '$\overline{\Gamma}_{0}$',
    '$\overline{\Gamma}_{0}^{R_1,t_1}$',
    '$\overline{\Gamma}_{0}^{R_2,t_1}$',
    '$\overline{\Gamma}_{0}^{R_1,t_2}$',
    '$\overline{\Gamma}_{0}^{R_2,t_2}$'])

# get a tick and will position things next to the last one
ticklab = ax00.xaxis.get_ticklabels()[0]
trans = ticklab.get_transform()
label = ax00.set_xlabel('$k$', ha='left', va = 'center')
ax00.xaxis.set_label_coords(kUV+1.2, 0.05, transform=trans)

ticklab = ax00.yaxis.get_ticklabels()[0]
trans = ticklab.get_transform()
label = ax00.set_ylabel('$\{\lambda_i\}$', ha='left', va = 'top',rotation=0)
ax00.yaxis.set_label_coords(-0.005, 6+0.7, transform=trans)


#plt.show()
ax00.grid(False)
ax00.spines['left'].set_position('zero')
ax00.spines['right'].set_visible(False)
ax00.spines['bottom'].set_position('zero')
ax00.spines['top'].set_visible(False)
ax00.xaxis.set_ticks_position('bottom')
ax00.yaxis.set_ticks_position('left')
# make arrows
ax00.plot((1), (0), ls="", marker=">", ms=3, color="k",
        transform=ax00.get_yaxis_transform(), clip_on=False)
ax00.plot((0), (1), ls="", marker="^", ms=3, color="k",
        transform=ax00.get_xaxis_transform(), clip_on=False)

# Export
fig.set_size_inches(14 * cm, 5 * cm)

save_plot(fig, 'truncation.pdf')