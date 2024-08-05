# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 11:23:11 2024

@author Martin Jakob Steil
@brief sMFA result
"""

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../graphics/'))
from plot_utils import *

import numpy as np
import pandas as pd
import json

emorot = gu_colors['emoRot']

fig, ax = plt.subplots()

homo1st=pd.read_csv('sMFA_homo1st.csv',sep=',',header=None).values
inhomo1st=pd.read_csv('sMFA_inhomo1st.csv',sep=',',header=None).values
inhomo2nd=pd.read_csv('sMFA_inhomo2nd.csv',sep=',',header=None).values
inhomoWindow=pd.read_csv('sMFA_inhomoWindow.csv',sep=',',header=None).values


ax.plot(homo1st[:,0],homo1st[:,1], linestyle='-', c='black', linewidth=1.0,zorder=11)

ax.fill_between(inhomoWindow[:,0],inhomoWindow[:,1],inhomoWindow[:,2], facecolor=emorot, alpha=0.5, linewidth=0.0,zorder=10)
ax.plot(inhomo1st[:,0],inhomo1st[:,1], linestyle='-', c=emorot, linewidth=1.0)
ax.plot(inhomo2nd[:,0],inhomo2nd[:,1], linestyle='--', c=emorot, linewidth=1.0, dashes=[5, 5])

ax.text(0.33, 0.685, "$\\mathrm{sMF\ (no\\text{-}sea)}$\n$\Lambda'=0\,\mathrm{GeV},\,\Lambda=5\,\mathrm{GeV},\,\lambda_k^\\mathrm{exp}$\n$f_\pi=88\,\\mathrm{MeV},\,M_\psi=300\,\\mathrm{MeV},\,m_\sigma=600\,\\mathrm{MeV}$",
          horizontalalignment='left', verticalalignment='bottom', transform=ax.transAxes,
          bbox=end_box_style,fontsize=8)

plt.grid(True)

plt.xlabel("$\mu\, (\mathrm{MeV})$")
plt.xticks([0,50,100,150,200,250,300,350,400])
plt.xlim((0,410))

plt.ylabel("$T\, (\mathrm{MeV})$")
plt.yticks([0,50,100,150,200])
plt.ylim((0,200))



fig.set_size_inches(11*cm,5*cm)
plt.tight_layout(pad=pad_default)
 
save_plot(fig,'sMFA_QMMCDW_PD_BC_0_5_88_300_600.pdf')
#plt.show()