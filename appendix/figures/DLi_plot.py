# -*- coding: utf-8 -*-
"""
@author Martin Jakob Steil
@date 2023-08-11T16:01
@brief Plots for polylogarithms DLi[2n,z]=Li^(1,0)[-2n,-E^z]+Li^(1,0)[-2n,-E^-z] for n=0,1,2,3
"""

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../graphics/'))
from plot_utils import *

import numpy as np
import json

## ************ Data import and processing ************ ##

with open('DLi0.json') as json_file:
    DLi0 = json.load(json_file)

with open('DLi2.json') as json_file:
    DLi2 = json.load(json_file)

with open('DLi4.json') as json_file:
    DLi4 = json.load(json_file)

with open('DLi6.json') as json_file:
    DLi6 = json.load(json_file)
    
data=[[DLi0,DLi2],[DLi4,DLi6]]

## ************ Figure ************ ##

plot_style={
    'color':colors[0],
    'linestyle': '-',
    'linewidth': 1.5    
}

roots_style = {
    'color':colors[0],
    'linestyle': 'none',
    'marker': '.',
    'markersize': 5
}

asympt_style = {
    'color': gray,
    'linestyle': (0,(2,2)),
    'linewidth': 1.5
}

zero_style = {
    'color': black,
    'linestyle': '-',
    'linewidth': 1.0
}

fig, ax = plt.subplots(2, 2,  gridspec_kw={'height_ratios': [1, 1]})

for i in range(2):
    for j in range(2):            
        DLiz=np.array(data[i][j]['data'])
        ax[i][j].semilogx([1E-10,1E10],[0,0],**zero_style)
        ax[i][j].semilogx(DLiz[:,0],DLiz[:,1],**plot_style)
        ax[i][j].set_facecolor('none')
        
        ax[i][j].set_xlim(1E-4, 2E3)
        ax[i][j].set_xlabel(r'$z=\mu\,\beta$')
        
        ax[i][j].set_ylim(data[i][j]['yRange'])
        ax[i][j].set_ylabel(r"{}".format(data[i][j]['name']))
        
        if len(data[i][j]['zInfData'])>0:
            DLizInf=np.array(data[i][j]['zInfData'])
            ax[i][j].semilogx(DLizInf[:,0],DLizInf[:,1],label=data[i][j]['zInfLabel'],**asympt_style)
            ax[i][j].legend(handlelength=1.5, numpoints=1,loc='lower left')
            
        if len(data[i][j]['roots'])>0:
            axij_roots = ax[i][j].twiny()
            ax[i][j].semilogx(data[i][j]['roots'],[0]*len(data[i][j]['roots']),**roots_style)            
            axij_roots.set_xlim(1E-4, 2E3)
            axij_roots.semilogx([],[])
            axij_roots.set_xticks(data[i][j]['roots'])
            axij_roots.tick_params(
                axis='x',
                which='both',    
                bottom=False,     
                top=True,       
                labelbottom=False,
                labeltop=False
            )
            axij_roots.set_zorder(-1)
            
        axij_z0 = ax[i][j].twinx()
        axij_z0.set_xlim(1E-4, 2E3)
        axij_z0.semilogx([],[])
        axij_z0.set_ylim(data[i][j]['yRange'])
        axij_z0.set_yticks([data[i][j]['z0']])
        axij_z0.set_yticklabels([data[i][j]['z0Label']])
        axij_z0.set_zorder(-1)
        
# Export
set_height_twoCol(fig, height=10,w_pad=0,h_pad=1)
save_plot(fig, 'DLi_plots.pdf')