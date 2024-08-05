# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 11:23:11 2024

@author Martin Jakob Steil
@brief BC RGMF result
"""


import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../graphics/'))
from plot_utils import *

import numpy as np
import pandas as pd
import json

file = 'eMFA_BC_400'
color= gu_colors['emoRot']
box_style=dict(boxstyle='round',alpha=1,facecolor='1',edgecolor='0.8')

fig, ax = plt.subplots()
homo1st=pd.read_csv(file+'_homo1st.csv',sep=',',header=None).values
homo2nd=pd.read_csv(file+'_homo2nd.csv',sep=',',header=None).values
homoLspinodial=pd.read_csv(file+'_homoLspinodial.csv',sep=',',header=None).values
homoCEP=pd.read_csv(file+'_homoCEP.csv',sep=',',header=None).values

inhomo1st=pd.read_csv(file+'_inhomo1st.csv',sep=',',header=None).values
inhomo2nd=pd.read_csv(file+'_inhomo2nd.csv',sep=',',header=None).values
inhomoWindow=pd.read_csv(file+'_inhomoWindow.csv',sep=',',header=None).values
inhomoLP=pd.read_csv(file+'_inhomoLP.csv',sep=',',header=None).values
inhomo2ndupper=pd.read_csv(file+'_inhomo2ndupper.csv',sep=',',header=None).values

ax.plot(homo1st[:,0],homo1st[:,1], linestyle='-', c='white', linewidth=1.0,zorder=2)
ax.plot(homo2nd[:,0],homo2nd[:,1], linestyle='dashdot', c='white', linewidth=1.0,zorder=2)

ax.plot(inhomo2ndupper[:,0],inhomo2ndupper[:,1], linestyle='-', c=color, linewidth=1.0)
ax.plot(inhomo1st[:,0],inhomo1st[:,1], linestyle='-', c=color, linewidth=1.0)
ax.plot(inhomo2nd[:,0],inhomo2nd[:,1], linestyle='--', c=color, linewidth=1.0)
ax.plot(homo2nd[:,0],homo2nd[:,1], linestyle='dashdot', c=color, linewidth=1.0)
ax.plot(inhomoLP[:,0],inhomoLP[:,1], linestyle=None, marker='.', markersize=10, c=color)				 
ax.plot(homoCEP[:,0],homoCEP[:,1], linestyle=None, marker='s', markersize=5, c=color,markeredgecolor=color)

#ax.plot(homoLspinodial[:,0],homoLspinodial[:,1], linestyle='--', c='gray', linewidth=1.0)

ax.plot(homoCEP[:,0],homoCEP[:,1], linestyle=None, marker='s', markersize=5, c=color,markeredgecolor=color,zorder=4)
ax.plot(inhomoLP[:,0],inhomoLP[:,1], linestyle=None, marker='.', markersize=10, c=color,zorder=4)				 

data=pd.read_csv(file+'_data.csv',sep=',',header=None).values

density=ax.tripcolor(data[::,0],data[::,1],data[::,2],vmin=0, vmax=300, shading='flat',edgecolor='none',cmap='viridis',rasterized=True)
cbar=plt.colorbar(density,shrink=1)
cbar.ax.get_yaxis().labelpad = 10
cbar.ax.set_ylabel('$M\,(\mathrm{MeV})$', rotation=90,fontsize=font_size)

Lambda=pd.read_csv(file+'_Lambda.csv',sep=',',header=None).values
ax.plot(Lambda[:,0],Lambda[:,1], linestyle='dotted', c='gray', linewidth=1.0,label='$\\mu^2+\\uppi^2T^2=\Lambda^2$')

# Customize grid lines
plt.grid(visible=True, which='major', linestyle='--',alpha=0.5, linewidth=0.5, color='gray',dashes=[5,5])

plt.xlabel("$\mu\, (\mathrm{MeV})$")
plt.xlim((0,380))

plt.ylabel("$T\, (\mathrm{MeV})$")
plt.ylim((0,200))


ax.legend(numpoints=1,loc='lower left',framealpha=1,facecolor='1',edgecolor='0.8',fancybox=True,fontsize=7) 




ax.text(0.025, 0.72, "$\\mathrm{RG\ (in)consistent\ MF}\ (\\mathrm{BC}\mathrm{\ fitting})$\n$\Lambda'=\Lambda=0.4\,\mathrm{GeV},\,\lambda_k^\\mathrm{exp}$\n$f_\pi=88\,\\mathrm{MeV},\,M_\psi=300\,\\mathrm{MeV},\,m_\sigma=600\,\\mathrm{MeV}$",
          horizontalalignment='left', verticalalignment='bottom', transform=ax.transAxes,
          bbox=box_style,fontsize=7)

fig.set_size_inches(11*cm,5*cm)
plt.tight_layout(pad=pad_default)
 
save_plot(fig,'eMFA_QMMCDW_PD_BC_04_04_88_300_600.pdf')
#plt.show()