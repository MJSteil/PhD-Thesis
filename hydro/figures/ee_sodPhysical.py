# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 15:49:41 2023

@author Martin Jakob Steil
@brief Plots of different solutions of the Euler equation (ee) for the
       sod shock tube problem with physical ICs
@see https://www.comsol.com/blogs/studying-shock-wave-phenomena-with-a-shock-tube-application/
"""


import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../graphics/'))
from plot_utils import *

import numpy as np
import json

## ************ Data import and processing ************ ##

with open('ee_sodPhysical.json') as json_file:
    raw = json.load(json_file)

xi=np.array(raw['xi'])
x0=min(xi)
x1=max(xi)

tj=np.array(raw['tj'])
t0=min(tj)
t1=max(tj)

rho_ij=np.array(raw['rho_ij'])
p_ij=np.array(raw['p_ij'])
v_ij=np.array(raw['v_ij'])
T_ij=np.array(raw['T_ij'])
cs_ij=np.array(raw['cs_ij'])
epsilon_ij=np.array(raw['epsilon_ij'])

# #tricolor alternative data
# data_rho=np.array([[0.,0.,0.]]*len(xi)*len(tj))
# data_p=np.array([[0.,0.,0.]]*len(xi)*len(tj))
# data_v=np.array([[0.,0,0.]]*len(xi)*len(tj))
# data_T=np.array([[0.,0.,0.]]*len(xi)*len(tj))
# for j in range(len(tj)):
#     for i in range(len(xi)):
#         data_rho[j*len(xi)+i]=[xi[i],tj[j],rho_ij[j,i]]
#         data_p[j*len(xi)+i]=[xi[i],tj[j],p_ij[j,i]]
#         data_v[j*len(xi)+i]=[xi[i],tj[j],v_ij[j,i]]
#         data_T[j*len(xi)+i]=[xi[i],tj[j],T_ij[j,i]]
        
## ************ Figure ************ ##

fig, ((ax00,ax01),(ax10,ax11),(ax20,ax21)) = plt.subplots(3, 2, sharey=True, sharex=True)
axi=(ax00,ax01,ax10,ax11,ax20,ax21)
# *------*------*
# | ax00 | ax01 |
# *------*------*
# | ax10 | ax11 |
# *------*------*
# | ax20 | ax21 |
# *------*------*

imshow_style={
    'interpolation':'none',
    'extent':[x0,x1,t0,t1],
    'origin':'lower', 
    'aspect':'auto',
    'rasterized':'True'
}
# tricolor_style={
#     'shading':'flat',
#     'rasterized':True
# }
contour_style={
    'colors':black,
    'linewidths':.25
}
colorbar_style={
    # 'extend':'both',
    'shrink':1,
    'pad':0.05
}

for a in axi:
    a.set_xlim(0,20)
    a.set_ylim(0,60)
    a.grid(False)

## rho ##
ax00.set_title("\\textbf{(a)} $\\rho\,(\mathrm{kg}\mkern1mum^{-3})$")    
plt=ax00.imshow(rho_ij,cmap='jet',**imshow_style)
# plt=ax00.tripcolor(data_rho[:,0],data_rho[:,1],data_rho[:,2],
#                    cmap='jet',**tricolor_style)
cbar=fig.colorbar(plt, ax=ax00, **colorbar_style)

ax00.contour(xi, tj, rho_ij,12,**contour_style)

## P ##
ax01.set_title("\\textbf{(b)} $p\,(\mathrm{Pa})$")   
plt=ax01.imshow(p_ij,cmap='jet',**imshow_style)
# plt=ax01.tripcolor(data_p[:,0],data_p[:,1],data_p[:,2],
#                    cmap='jet',**tricolor_style)
cbar=fig.colorbar(plt, ax=ax01, **colorbar_style)
#https://stackoverflow.com/a/15572691/6644522
from matplotlib import ticker
formatter = ticker.ScalarFormatter(useMathText=False)
formatter.set_scientific(True) 
formatter.set_powerlimits((-1,1)) 
cbar.ax.yaxis.set_major_formatter(formatter) 
cbar.ax.yaxis.set_offset_position('left')
#cbar.ax.yaxis.get_offset_text().set_size(fontsize) 
#https://stackoverflow.com/a/45766598/6644522
#cbar.ax.yaxis.offsetText.set_visible(False)

ax01.contour(xi, tj, p_ij,12,**contour_style)

## v ##
ax10.set_title("\\textbf{(c)} $v\,(\mathrm{m}\mkern1mus^{-1})$")   
plt=ax10.imshow(v_ij,
                norm=matplotlib.colors.TwoSlopeNorm(0,-55,305),
                cmap='coolwarm',**imshow_style)  
# plt=ax10.tripcolor(data_v[:,0],data_v[:,1],data_v[:,2],
#                    norm=matplotlib.colors.TwoSlopeNorm(0,-55,305),
#                    cmap='coolwarm',**tricolor_style)    
cbar=fig.colorbar(plt, ax=ax10, ticks=[-50,-25,0,100,200,300], **colorbar_style)

ax10.contour(xi, tj, v_ij,12,**contour_style)

## T ##
ax11.set_title("\\textbf{(d)} $T\,(\mathrm{K})$")
T0=T_ij[0,0]      
plt=ax11.imshow(T_ij,
                norm=matplotlib.colors.TwoSlopeNorm(T0),
                cmap='coolwarm',**imshow_style)
# plt=ax11.tripcolor(data_T[:,0],data_T[:,1],data_T[:,2],
#                    norm=matplotlib.colors.TwoSlopeNorm(300),
#                    cmap='coolwarm',**tricolor_style)    
cbar=fig.colorbar(plt, ax=ax11, ticks=[200,250,300,400,500,600],**colorbar_style)

ax11.contour(xi, tj, T_ij,12,**contour_style)

## cs ##
ax20.set_title("\\textbf{(e)} $c_s\,(\mathrm{m}\mkern1mus^{-1})$")
cs0=cs_ij[0,0]   
plt=ax20.imshow(cs_ij,
                norm=matplotlib.colors.TwoSlopeNorm(cs0,cs0-120,cs0+120),
                cmap='coolwarm',**imshow_style)
# plt=ax11.tripcolor(data_T[:,0],data_T[:,1],data_T[:,2],
#                    norm=matplotlib.colors.TwoSlopeNorm(300),
#                    cmap='coolwarm',**tricolor_style)    
cbar=fig.colorbar(plt, ax=ax20, ticks=[250,300,350,400,450],**colorbar_style)

ax20.contour(xi, tj, cs_ij,12,**contour_style)

## epsilon ##
ax21.set_title("\\textbf{(f)} $\epsilon\,(\mathrm{J}\mkern1mum^{-3})$")   
plt=ax21.imshow(epsilon_ij,
                cmap='jet',**imshow_style)
# plt=ax11.tripcolor(data_T[:,0],data_T[:,1],data_T[:,2],
#                    norm=matplotlib.colors.TwoSlopeNorm(300),
#                    cmap='coolwarm',**tricolor_style)    
cbar=fig.colorbar(plt, ax=ax21,**colorbar_style)
#https://stackoverflow.com/a/15572691/6644522
from matplotlib import ticker
formatter = ticker.ScalarFormatter(useMathText=False)
formatter.set_scientific(True) 
formatter.set_powerlimits((-1,1)) 
cbar.ax.yaxis.set_major_formatter(formatter) 
cbar.ax.yaxis.set_offset_position('left')
#cbar.ax.yaxis.get_offset_text().set_size(fontsize) 
#https://stackoverflow.com/a/45766598/6644522
#cbar.ax.yaxis.offsetText.set_visible(False)

ax21.contour(xi, tj, epsilon_ij,12,**contour_style)


## Labeling ##
ax00.set_ylabel("$t\,(\mathrm{ms})$")
ax10.set_ylabel("$t\,(\mathrm{ms})$")
ax20.set_ylabel("$t\,(\mathrm{ms})$")
ax20.set_xlabel("$x\,(\mathrm{m})$")
ax21.set_xlabel("$x\,(\mathrm{m})$")

for i in range(len(axi)):
    a=axi[i]
    draw_contoured_annotation(a,0.35,0.3,"\\ding{192}",font_size,0.8) # Rarefraction fan
    draw_contoured_annotation(a,0.88,0.22,"\\ding{194}",font_size,0.8) # Shock
    draw_contoured_annotation(a,0.93,0.37,"\\ding{195}",font_size,0.8) # Reflected Shock
    if (i==0)|(i==3)|(i==4)|(i==5):
        draw_contoured_annotation(a,0.68,0.2,"\\ding{193}",font_size,0.8) # Contact discontinuity


    
# Export
set_height_twoCol(fig, height=17)
save_plot(fig, 'ee_sodPhysical.pdf',300)