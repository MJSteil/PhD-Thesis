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

with open('gn_gl_2nd_datthermo.json') as json_file:
    data2 = json.load(json_file)

with open('gn_gl_1st_datthermo.json') as json_file:
    data1 = json.load(json_file)
mu0=data1["mu0"]
mu1=data1["mu1"]
mu1st=data1["mu1st"]
Tc=0.566933
data1=data1["dat"]
## ************ Figure ************ ##
fig, ((ax00, ax01),(ax20, ax21)) = plt.subplots(2, 2, sharex='col', sharey=False)
fig.subplots_adjust(hspace=0.0)  # adjust space between axes
# *------*------*
# | ax00 | ax01 |
# *------*------*
# | ax10 | ax11 |
# *------*------*
# | ax20 | ax21 |
# *------*------*

def plot_vline(ax,val):
    ax.plot([val,val],[-10,10],color=black,**plot_styles)
    
plot_styles={'linewidth': 1.,'linestyle':'-'}
plot_styles2={'linewidth': 1.,'linestyle': '--'} #(0, (4, 4)
point_styles={'linestyle': 'none','marker': '.','markersize': 3}
c=[colors[0],colors[1]]

formatter = mticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-1,1))


ax00.plot(data2["datLthermo"][0],data2["datLthermo"][4],color=c[0],**plot_styles)
ax00.plot(data2["datRthermo"][0],data2["datRthermo"][4],color=c[1],**plot_styles)
ax00.set_ylabel("$n$")

ax01.plot(data1[0][0],data1[0][4],color=c[0],**plot_styles)
ax01.plot(data1[1][0],data1[1][4],color=c[0],**plot_styles2)
ax01.plot(data1[2][0],data1[2][4],color=c[1],**plot_styles)
ax01.plot(data1[3][0],data1[3][4],color=c[1],**plot_styles2)


ax20.plot(data2["datLthermo"][0],data2["datLthermo"][5],color=c[0],**plot_styles)
ax20.plot(data2["datRthermo"][0],data2["datRthermo"][5],color=c[1],**plot_styles)
ax20.set_ylabel("$\\chi_q$")
ax20.set_xlabel("$T$")
ax20.set_xlim(Tc-0.05,Tc+0.05)

ax21.plot(data1[0][0],data1[0][5],color=c[0],**plot_styles)
ax21.plot(data1[1][0],data1[1][5],color=c[0],**plot_styles2)
ax21.plot(data1[2][0],data1[2][5],color=c[1],**plot_styles)
ax21.plot(data1[3][0],data1[3][5],color=c[1],**plot_styles2)
ax21.set_ylim(0,4)
ax21.set_xlim(mu0,mu1)
ax21.set_xlabel("$\mu$")

# Subplot marker
ax00.text(0.97, 0.84, '\\textbf{(a)}',
          horizontalalignment='right', verticalalignment='bottom', transform=ax00.transAxes,
          bbox=end_box_style)


ax01.text(0.97, 0.84, '\\textbf{(b)}',
          horizontalalignment='right', verticalalignment='bottom', transform=ax01.transAxes,
          bbox=end_box_style)


ax20.text(0.97, 0.84, '\\textbf{(c)}',
          horizontalalignment='right', verticalalignment='bottom', transform=ax20.transAxes,
          bbox=end_box_style)


ax21.text(0.97, 0.84, '\\textbf{(d)}',
          horizontalalignment='right', verticalalignment='bottom', transform=ax21.transAxes,
          bbox=end_box_style)


# Export
set_height_twoCol(fig, height=8)

save_plot(fig, 'gn_gl_thermo2.pdf')