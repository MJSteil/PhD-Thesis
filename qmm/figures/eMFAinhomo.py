# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 11:23:11 2024

@author Martin Jakob Steil
@brief Naive BC eMFA result
"""

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../graphics/'))
from plot_utils import *

import numpy as np
import pandas as pd
import json

names=[400,450,500]
pts=[5,12,281]
labels=[["\\textbf{(a)} $\Lambda'=400\,\mathrm{MeV}$","\\textbf{(b)}"],#
        ["\\textbf{(c)} $\Lambda'=450\,\mathrm{MeV}$","\\textbf{(d)}"],#
        ["\\textbf{(e)} $\Lambda'=500\,\mathrm{MeV}$","\\textbf{(f)}"]]

box_style=dict(boxstyle='round',alpha=1,facecolor='1',edgecolor='0.8')

fig, ((ax00,ax01),(ax10,ax11),(ax20,ax21)) = plt.subplots(3, 2, sharey=True, sharex=True,gridspec_kw = {'height_ratios':[1,1,1],'width_ratios':[0.8, 1.4]})
axi=[[ax00,ax01],[ax10,ax11],[ax20,ax21]]

ax00.set_xlim([250,350])
ax00.set_ylim([0,100])

ax01.set_xlim([250,350])
ax01.set_xticks([250,275,300,325,350])
ax01.set_ylim([0,100])

ax00.set_ylabel("$T\,(\mathrm{MeV})$")
ax10.set_ylabel("$T\,(\mathrm{MeV})$")
ax20.set_ylabel("$T\,(\mathrm{MeV})$")

ax20.set_xlabel("$\mu\,(\mathrm{MeV})$")
ax21.set_xlabel("$\mu\,(\mathrm{MeV})$")

# Customize grid lines


for j in [0,1,2]:
    [ax0,ax1]=axi[j]
    dat= np.genfromtxt('eMFAinhomo'+str(names[j])+'.csv', delimiter=',',skip_header=0)
    
  
    pd=ax1.tripcolor(dat[::,0],dat[::,1],dat[::,3], shading='flat',edgecolor='none',cmap='plasma',rasterized=True,vmin=0,vmax=400)
    cbar=fig.colorbar(pd, ax=ax1, pad=0.125,shrink=1)
    cbar.ax.get_yaxis().labelpad = 5
    cbar.ax.set_ylabel('$q\,(\mathrm{MeV})$', rotation=90)
    
    pd2=ax0.tripcolor(dat[::,0],dat[::,1],dat[::,2]*300/88, shading='flat',edgecolor='none',cmap='viridis',rasterized=True,vmin=0,vmax=300)
    cbar=fig.colorbar(pd2, ax=ax1, pad=0.05,shrink=1)
    cbar.ax.get_yaxis().labelpad = 5
    cbar.ax.set_ylabel('$M\,(\mathrm{MeV})$', rotation=90)
    
    
    datPts= np.genfromtxt('eMFApt'+str(names[j])+'.csv', delimiter=',',skip_header=0)
    i=pts[j]
    ax0.plot(datPts[2:i+1:,0],datPts[2:i+1:,1],color='white',linewidth=1,linestyle='dashdot',zorder=10)
    ax0.plot(datPts[i:i+1:,0],datPts[i:i+1:,1],color='white',marker='s',markersize=5,markeredgecolor='white',zorder=10)
    ax0.plot(datPts[i::,0],datPts[i::,1],color='white',linewidth=1,zorder=10)
    ax1.plot(datPts[2:i+1:,0],datPts[2:i+1:,1],color='white',linewidth=1,linestyle='dashdot',zorder=10)
    ax1.plot(datPts[i:i+1:,0],datPts[i:i+1:,1],color='white',marker='s',markersize=5,markeredgecolor='white',zorder=10)
    ax1.plot(datPts[i::,0],datPts[i::,1],color='white',linewidth=1,zorder=10)
    
    ax0.text(0.945, 0.88, labels[j][0],
              horizontalalignment='right', verticalalignment='bottom', transform=ax0.transAxes,
              bbox=box_style,fontsize=8)
    
    ax1.text(0.945, 0.88, labels[j][1],
              horizontalalignment='right', verticalalignment='bottom', transform=ax1.transAxes,
              bbox=box_style,fontsize=8)
    
    ax0.grid(visible=True, which='major', linestyle='--',alpha=0.5, linewidth=0.5, color='gray',dashes=[5,5])
    ax1.grid(visible=True, which='major', linestyle='--',alpha=0.5, linewidth=0.5, color='gray',dashes=[5,5])

# Export
set_height_twoCol(fig, height=15)
save_plot(fig, 'eMFAinhomo.pdf',300)