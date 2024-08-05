# -*- coding: utf-8 -*-
"""
@author Martin Jakob Steil
@data 2023-12-06
@brief 1st order GL - U
"""

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../graphics/'))
from plot_utils import *
import matplotlib.ticker as mticker

import numpy as np
import json

## ************ Data import and processing ************ ##

with open('gn_gl_1st_U.json') as json_file:
    data = json.load(json_file)

with open('gn_gl_1st_Umin.json') as json_file:
    dataMin = json.load(json_file)
    
l=len(data['data'])
muTi=data['muTi']
Ux=np.array(data['data'])
Uxext=data['extrema']

i=0 # select variable 0=mu or 1=T

#ax00
x0=muTi[0][i]
x1=muTi[-1][i]

dx=x1-x0
c=get_color_list(colors[0],colors[1],l)
cgrad=get_color_list(colors[0],colors[1],100)

## ************ Figure ************ ##
fig, ((ax00, ax01),(ax10, ax11)) = plt.subplots(2, 2, sharex=True, sharey=False)
fig.subplots_adjust(hspace=0.025)  # adjust space between axes
# *------*------*
# | ax00 | ax01 |
# *------*------*
# | ax10 | ax11 |
# *------*------*

plot_styles={'linewidth': 1.,'linestyle':'-'}
plot_styles2={'linewidth': 1.,'linestyle': '-'} #(0, (4, 4)
point_styles={'linestyle': 'none','marker': '.','markersize': 3}

formatter = mticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-1,1))

#ax01

for i in range(l):
    ax01.plot(Ux[i,:,0],Ux[i,:,1],color=c[i],label='',**plot_styles)
    ax01.plot(np.array(Uxext[i])[:,0],np.array(Uxext[i])[:,1],color=c[i],label='',**point_styles)

ax01.set_ylim(-.003,0.003)

ax01.set_ylabel("$\mathcal{V}^{(6)}(\mu,T_1;\Delta)-\mathcal{V}^{(6)}(\mu,T_1;0)$")


ax01.yaxis.set_major_formatter(formatter)

#ax11
ci=[cgrad[x] for x in dataMin['xiR']]
xi=np.array(dataMin['datR'])
for j in range(len(xi)):
    segs=[]
    for i in range(len(ci)-1):
        x1 = xi[j][i][0]
        y1 = xi[j][i][1]
        x2 = xi[j][i+1][0]
        y2 = xi[j][i+1][1]
        segs.append(((x1, y1), (x2, y2)))
    ln_coll = matplotlib.collections.LineCollection(segs,colors=ci,capstyle='round',**plot_styles)
    ax11.add_collection(ln_coll)
ci=[cgrad[x] for x in dataMin['xiL']]
xi=np.array(dataMin['datL'])
for j in range(len(xi)):
    segs=[]
    for i in range(len(ci)-1):
        x1 = xi[j][i][0]
        y1 = xi[j][i][1]
        x2 = xi[j][i+1][0]
        y2 = xi[j][i+1][1]
        segs.append(((x1, y1), (x2, y2)))
    ln_coll = matplotlib.collections.LineCollection(segs,colors=ci,capstyle='round',**plot_styles2)
    ax11.add_collection(ln_coll)
 
ax11.set_ylim(-0.0254901,0.0168696)    
ax11.set_ylabel("$\mu-\mu_1$")
ax11.set_xlabel("$\Delta$")  
ax11.yaxis.set_major_formatter(formatter)

with open('gn_gl_2nd_U.json') as json_file:
    data = json.load(json_file)

with open('gn_gl_2nd_Umin.json') as json_file:
    dataMin = json.load(json_file)
    
l=len(data['data'])
muTi=data['muTi']
Ux=np.array(data['data'])
Uxext=data['extrema']

i=1 # select variable 0=mu or 1=T

#ax00
x0=muTi[0][i]
x1=muTi[-1][i]

dx=x1-x0
c=get_color_list(colors[0],colors[1],l)
cgrad=get_color_list(colors[0],colors[1],100)

#ax00
for i in range(l):
    ax00.plot(Ux[i,:,0],Ux[i,:,1],color=c[i],label='',**plot_styles)
    ax00.plot(np.array(Uxext[i])[:,0],np.array(Uxext[i])[:,1],color=c[i],label='',**point_styles)

ax00.set_ylim(-.002,0.001)  
# ax00.set_yticks([])
ax00.set_ylabel("$\mathcal{V}^{(4)}(0,T;\Delta)-\mathcal{V}^{(4)}(0,T;0)$")
ax00.yaxis.set_major_formatter(formatter)
    
#ax10
ci=[cgrad[x] for x in dataMin['xiR']]
xi=np.array(dataMin['datR'])
for j in range(len(xi)):
    segs=[]
    for i in range(len(ci)-1):
        x1 = xi[j][i][0]
        y1 = xi[j][i][1]
        x2 = xi[j][i+1][0]
        y2 = xi[j][i+1][1]
        segs.append(((x1, y1), (x2, y2)))
    ln_coll = matplotlib.collections.LineCollection(segs,colors=ci,capstyle='round',**plot_styles)
    ax10.add_collection(ln_coll)
ci=[cgrad[x] for x in dataMin['xiL']]
xi=np.array(dataMin['datL'])
for j in range(len(xi)):
    segs=[]
    for i in range(len(ci)-1):
        x1 = xi[j][i][0]
        y1 = xi[j][i][1]
        x2 = xi[j][i+1][0]
        y2 = xi[j][i+1][1]
        segs.append(((x1, y1), (x2, y2)))
    ln_coll = matplotlib.collections.LineCollection(segs,colors=ci,capstyle='round',**plot_styles2)
    ax10.add_collection(ln_coll)
 

ax10.set_ylim(-.05,0.05)
ax10.set_xlim(-1.05,1.05)    
ax10.set_ylabel("$T-T_c$")
ax10.set_xlabel("$\Delta$")
ax10.yaxis.set_major_formatter(formatter)


# Subplot marker
ax00.text(0.97, 0.88, '\\textbf{(a)}',
          horizontalalignment='right', verticalalignment='bottom', transform=ax00.transAxes,
          bbox=end_box_style)


ax01.text(0.97, 0.88, '\\textbf{(b)}',
          horizontalalignment='right', verticalalignment='bottom', transform=ax01.transAxes,
          bbox=end_box_style)


ax10.text(0.97, 0.88, '\\textbf{(c)}',
          horizontalalignment='right', verticalalignment='bottom', transform=ax10.transAxes,
          bbox=end_box_style)


ax11.text(0.97, 0.88, '\\textbf{(d)}',
          horizontalalignment='right', verticalalignment='bottom', transform=ax11.transAxes,
          bbox=end_box_style)
    
# Export
set_height_twoCol(fig, height=12)

save_plot(fig, 'gn_gl_1st_U.pdf')