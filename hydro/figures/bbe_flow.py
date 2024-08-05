# -*- coding: utf-8 -*-
"""
@author Martin Jakob Steil
@data 2023-08-07T15:49
@brief Plot (flow) for the inviscid bateman burgers equation (bbe)
"""

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../graphics/'))
from plot_utils import *

import numpy as np
import json

## ************ Data import and processing ************ ##

with open('bbe_flow.json') as json_file:
    data = json.load(json_file)

with open('bbe_characteristics.json') as json_file:
    rawChar = json.load(json_file)
dataChar=rawChar['data']
tcChar=rawChar['tc']
    
## ************ Figure ************ ##
fig, ((ax00, ax01)) = plt.subplots(1, 2, sharey=False)
fig.subplots_adjust(hspace=0.025)  # adjust space between axes
# *------*------*
# | ax00 | ax01 |
# *------*------*

#ax00
t0=min(data['ti'])
t1=max(data['ti'])
dt=t1-t0
c=get_color_list(colors[0],colors[1],101)
cP1=[c[math.ceil((t-t0)/dt*100)] for t in data['ti']]

plot_styles={'linewidth': 1.,'linestyle':'-'}
point_styles={'linestyle': 'none','marker': '.','markersize': 3}

for i in range(len(cP1)):
    ax00.plot(data['xi'],data['uitRef'][i],color=cP1[i],label=data['labels'][i],**plot_styles)
    ax00.plot(data['xi'],data['uit'][i],color=cP1[i],**point_styles)  

ax00.set_ylim(-1.1,1.1)
ax00.set_ylabel("$u(t,x)$")
ax00.set_xlabel("$x$")
# ax00.set_xlim(0,1)
ax00.legend(numpoints=1,loc='lower left')

c=get_color_list(colors[0],colors[3],101)  

#ax01
for i in range(len(dataChar)):
    ci=[c[math.floor((l+1)/2*100)] for l in dataChar[i][0]]
    ax01.plot(np.array(dataChar[i][1][1]),np.array(dataChar[i][1][0])/tcChar,color=ci[0],**plot_styles) 
    ax01.plot(np.array(dataChar[i][1][2]),np.array(dataChar[i][1][0])/tcChar,color=ci[1],**plot_styles) 
 

ax01.set_ylim(0,2)
ax01.set_ylabel("$2\,\\uppi\,t$")
ax01.set_xlim(-.06,1.06)
ax01.set_xlabel("$x$")

ax01.axhline(y = 1, color = colors[1], linestyle='--',linewidth=1.5)

ax01.plot([0.5,0.5],[1,2],color='black',**plot_styles)

# Subplot marker
ax00.text(0.97, 0.88, '\\textbf{(a)}',
          horizontalalignment='right', verticalalignment='bottom', transform=ax00.transAxes,
          bbox=end_box_style)


ax01.text(0.97, 0.88, '\\textbf{(b)}',
          horizontalalignment='right', verticalalignment='bottom', transform=ax01.transAxes,
          bbox=end_box_style)
# Export
set_height_twoCol(fig, height=5.5)

save_plot(fig, 'bbe_flow.pdf')