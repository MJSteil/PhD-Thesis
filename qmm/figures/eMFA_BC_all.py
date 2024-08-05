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

emorot=fromColorToRG(gu_colors['emoRot'])
sonnengelb=fromColorToRG(gu_colors['sonnenGelb'])

colors=[[((1-f)*emorot[i]+f*sonnengelb[i])/255.0 for i in range(0,3)] for f in np.arange(0, 1.1, 1./3.)]

fig, ax = plt.subplots()

file = 'eMFA_BC_400'
color=colors[3]
inhomo1st=pd.read_csv(file+'_inhomo1st.csv',sep=',',header=None).values
inhomo2nd=pd.read_csv(file+'_inhomo2nd.csv',sep=',',header=None).values
inhomoLP=pd.read_csv(file+'_inhomoLP.csv',sep=',',header=None).values
inhomo2ndupper=pd.read_csv(file+'_inhomo2ndupper.csv',sep=',',header=None).values
inhomoLP=pd.read_csv(file+'_inhomoLP.csv',sep=',',header=None).values
homoCEP=pd.read_csv(file+'_homoCEP.csv',sep=',',header=None).values
homo2nd=pd.read_csv(file+'_homo2nd.csv',sep=',',header=None).values

ax.plot(inhomo2ndupper[:,0],inhomo2ndupper[:,1], linestyle='-', c=color, linewidth=1.0)
ax.plot(inhomo1st[:,0],inhomo1st[:,1], linestyle='-', c=color, linewidth=1.0,label='$\Lambda=0.4\,\mathrm{GeV}$')
ax.plot(inhomo2nd[:,0],inhomo2nd[:,1], linestyle='--', c=color, linewidth=1.0, dashes=[5, 5])
ax.plot(homo2nd[:,0],homo2nd[:,1], linestyle='dashdot', c=color, linewidth=1.0)
ax.plot(inhomoLP[:,0],inhomoLP[:,1], linestyle=None, marker='.', markersize=10, c=color)				 
ax.plot(homoCEP[:,0],homoCEP[:,1], linestyle=None, marker='s', markersize=5, c=color,markeredgecolor=color)

file = 'eMFA_BC_600'
color=colors[2]
inhomo1st=pd.read_csv(file+'_inhomo1st.csv',sep=',',header=None).values
inhomo2nd=pd.read_csv(file+'_inhomo2nd.csv',sep=',',header=None).values
inhomoLP=pd.read_csv(file+'_inhomoLP.csv',sep=',',header=None).values
inhomo2ndupper=pd.read_csv(file+'_inhomo2ndupper.csv',sep=',',header=None).values
inhomoLP=pd.read_csv(file+'_inhomoLP.csv',sep=',',header=None).values
ax.plot(inhomo2ndupper[:,0],inhomo2ndupper[:,1], linestyle='dashdot', c=color, linewidth=1.0)
ax.plot(inhomo1st[:,0],inhomo1st[:,1], linestyle='-', c=color, linewidth=1.0,label='$\Lambda=0.6\,\mathrm{GeV}$')
ax.plot(inhomo2nd[:,0],inhomo2nd[:,1], linestyle='--', c=color, linewidth=1.0, dashes=[5, 5])
ax.plot(inhomoLP[:,0],inhomoLP[:,1], linestyle=None, marker='.', markersize=10, c=color)		

file = 'eMFA_BC_1000'
color=colors[1]
inhomo1st=pd.read_csv(file+'_inhomo1st.csv',sep=',',header=None).values
inhomo2nd=pd.read_csv(file+'_inhomo2nd.csv',sep=',',header=None).values
inhomoLP=pd.read_csv(file+'_inhomoLP.csv',sep=',',header=None).values
inhomo2ndupper=pd.read_csv(file+'_inhomo2ndupper.csv',sep=',',header=None).values
inhomoLP=pd.read_csv(file+'_inhomoLP.csv',sep=',',header=None).values
ax.plot(inhomo2ndupper[:,0],inhomo2ndupper[:,1], linestyle='dashdot', c=color, linewidth=1.0)
ax.plot(inhomo1st[:,0],inhomo1st[:,1], linestyle='-', c=color, linewidth=1.0,label='$\Lambda=1.0\,\mathrm{GeV}$')
ax.plot(inhomo2nd[:,0],inhomo2nd[:,1], linestyle='--', c=color, linewidth=1.0, dashes=[5, 5])
ax.plot(inhomoLP[:,0],inhomoLP[:,1], linestyle=None, marker='.', markersize=10, c=color)				 


file = 'eMFA_BC'
color=colors[0]
inhomo1st=pd.read_csv(file+'_inhomo1st.csv',sep=',',header=None).values
inhomo2nd=pd.read_csv(file+'_inhomo2nd.csv',sep=',',header=None).values
inhomoLP=pd.read_csv(file+'_inhomoLP.csv',sep=',',header=None).values
inhomo2ndupper=pd.read_csv(file+'_inhomo2ndupper.csv',sep=',',header=None).values
inhomoLP=pd.read_csv(file+'_inhomoLP.csv',sep=',',header=None).values
ax.plot(inhomo2ndupper[:,0],inhomo2ndupper[:,1], linestyle='dashdot', c=color, linewidth=1.0)
ax.plot(inhomo1st[:,0],inhomo1st[:,1], linestyle='-', c=color, linewidth=1.0,label='$\Lambda=5.0\,\mathrm{GeV}$')
ax.plot(inhomo2nd[:,0],inhomo2nd[:,1], linestyle='--', c=color, linewidth=1.0, dashes=[5, 5])
ax.plot(inhomoLP[:,0],inhomoLP[:,1], linestyle=None, marker='.', markersize=10, c=color)				 
		 
plt.grid(True)

plt.xlabel("$\mu\, (\mathrm{MeV})$")
plt.xlim((0,380))

plt.ylabel("$T\, (\mathrm{MeV})$")
plt.ylim((0,210))

plt.xticks([0,50,100,150,200,250,300,350])
plt.yticks([0,50,100,150,200])

ax.legend(numpoints=3,loc=1,handlelength=1.25,fontsize=8)

ax.text(0.02, 0.05, "$\\mathrm{RG\ consistent\ MF}\ (\\mathrm{BC}\mathrm{\ fitting})$\n$\Lambda'=0.4\,\mathrm{GeV},\,\lambda_k^\\mathrm{exp}$\n$f_\pi=88\,\\mathrm{MeV},\,M_\psi=300\,\\mathrm{MeV},\,m_\sigma=600\,\\mathrm{MeV}$",
          horizontalalignment='left', verticalalignment='bottom', transform=ax.transAxes,
          bbox=end_box_style,fontsize=8)


fig.set_size_inches(11*cm,5*cm)
plt.tight_layout(pad=pad_default)
plt.subplots_adjust(right=0.965)  
 
save_plot(fig,'eMFA_QMMCDW_PD_BC_04_all_88_300_600.pdf')