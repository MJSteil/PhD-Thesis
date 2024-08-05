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
import matplotlib.image as mpimg
from scipy.interpolate import make_interp_spline, BSpline
from labellines import labelLine, labelLines
import matplotlib.transforms as transforms

from matplotlib.path import Path
from matplotlib.patches import FancyArrowPatch

from matplotlib.patches import FancyBboxPatch

## ************ Data import and processing ************ ##
img = mpimg.imread("qcd_phasediagram_defense.png")
img_shape = img.shape
img_aspect=img_shape[0]/img_shape[1]


## ************ Styles ************ ##
c=['black',colors[1]]

plot_styles=list(map(lambda i : {
    'color':c[i],
    'linestyle': '-',
    'linewidth': 1.5
    },range(2)))
point_styles=list(map(lambda i : {
    'color':'0',
    'linestyle': 'none',
    'marker': '.',
    'markersize': 5
    },range(2)))

## ************ Figure ************ ##

fig, ax00 = plt.subplots()
ax00.imshow(img, extent=[0, 12, 0, img_aspect*12],zorder=0) # background image

## Axes
ax00.set_xlabel("Baryonendichte $n\\left(n_0=0.16\,\mathrm{fm}^{-3}\\right)$")
ax00.set_xlim(0,12)
ax00.set_xticks([0,1.6,5.4,8],[0,1,5,8])


ax00.set_ylabel("Temperatur $T\,(\mathrm{MeV})$")
ax00.set_ylim(0,img_aspect*12)
ax00.set_yticks([0,3,6],[0,100,200])

# Cut x-axes
d = 2.  # proportion of vertical to horizontal extent of the slanted line
r1=0.8
r2=r1+0.013
dr=0.001
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=8,
              linestyle="none", color='k', mec='k', mew=1, zorder=6,clip_on=False)
ax00.axhline(y=0, xmin=r1+dr, xmax=r2-dr, color='white', linewidth=1,zorder=5,clip_on=False)
ax00.axhline(y=img_aspect*12, xmin=r1+dr, xmax=r2-dr, color='white', linewidth=1,zorder=5,clip_on=False)
ax00.plot([r1,r2,r1,r2], [0,0,1,1], transform=ax00.transAxes, **kwargs)

# Cut y-axes
d = 2.  # proportion of vertical to horizontal extent of the slanted line
r1=0.85
r2=r1+0.02
dr=0.001
kwargs = dict(marker=[(-d, -1), (d, 1)], markersize=7,
              linestyle="none", color='k', mec='k', mew=1, zorder=6,clip_on=False)
ax00.axvline(x=0, ymin=r1+dr, ymax=r2-dr, color='white', linewidth=1,zorder=5,clip_on=False)
ax00.axvline(x=12, ymin=r1+dr, ymax=r2-dr, color='white', linewidth=1,zorder=5,clip_on=False)
ax00.plot([0,0,1,1], [r1,r2,r1,r2], transform=ax00.transAxes, **kwargs)

## Laboratories
def gen_bezier(control_points,n=100):
    # Generate points along the Bézier curve
    t = np.linspace(0, 1, n)
    x_curve = (1 - t)**3 * control_points[0, 0] + 3 * (1 - t)**2 * t * control_points[1, 0] + 3 * (1 - t) * t**2 * control_points[2, 0] + t**3 * control_points[3, 0]
    y_curve = (1 - t)**3 * control_points[0, 1] + 3 * (1 - t)**2 * t * control_points[1, 1] + 3 * (1 - t) * t**2 * control_points[2, 1] + t**3 * control_points[3, 1]
    return x_curve,y_curve,control_points

# RHIC/LHC
x_curve,y_curve,control_points = gen_bezier(np.array([[1.7, 0.8], [2,3], [1.25, 5.25],[1.25,5.25]]))
#ax00.plot(control_points[:, 0], control_points[:, 1], 'ro-')
ax00.plot(x_curve[:18], y_curve[:18],**plot_styles[1])
plt.text(1.65,2.04,'RHIC/LHC',rotation=-85, ha='center', va='bottom',zorder=10, size=9, color=c[1])
ax00.plot(x_curve[51:], y_curve[51:],**plot_styles[1])
spline=make_interp_spline(x_curve[:5],y_curve[:5], k=2)
ax00.arrow(x_curve[-1]-0.01,y_curve[-1]+0.02, -0.033,0.1,**plot_styles[1], shape='full', lw=0, length_includes_head=True, head_width=.2)

# FAIR SIS 300
x_curve,y_curve,control_points = gen_bezier(np.array([[2.2, 0.65], [4,2], [6,2.5],[6,2.5]]))
# ax00.plot(control_points[:, 0], control_points[:, 1], 'ro-')
ax00.plot(x_curve[:8], y_curve[:8],**plot_styles[1])
plt.text(3.6,.8,'FAIR SIS 100',rotation=28, ha='center', va='bottom',zorder=10, size=9, color=c[1])
ax00.plot(x_curve[46:], y_curve[46:],**plot_styles[1])
spline=make_interp_spline(x_curve[:5],y_curve[:5], k=2)
ax00.arrow(x_curve[-1],y_curve[-1], 0.2,0.2*np.tan(16*2*np.pi/360),**plot_styles[1], shape='full', lw=0, length_includes_head=True, head_width=.2)

# Early universe
ax00.plot([0.15,0.15], [3,10],**plot_styles[1])
plt.text(0.45,3.5,'Frühes Universum',rotation=-90, ha='center', va='bottom',zorder=10, size=9, color=c[1])
ax00.arrow(0.15,2.85, 0, -0.01,**plot_styles[1], shape='full', lw=0, length_includes_head=True, head_width=.2)

# Neutron stars
plt.text(6.3,.2,'Neutronensterne ',rotation=0, ha='center', va='bottom',zorder=10, size=9, color=c[1])

## Phase diagram

plt.text(3.5,3,'Deconf. \&',rotation=-40, ha='center', va='bottom',zorder=10, size=9, color='0')
plt.text(4.55,2.05,'chiraler',rotation=-50, ha='center', va='bottom',zorder=10, size=9, color='0')
plt.text(5.5,0.4,'Übergang?!',rotation=-60, ha='center', va='bottom',zorder=10, size=9, color='0')

plt.text(4.0,4.7,'Kritischer Punkt?',rotation=-0, ha='center', va='bottom',zorder=10, size=9, color='0')
#plt.text(7.2,2.2,'Quarkyonic matter?',rotation=-15, ha='center', va='bottom',zorder=10, size=9, color='0')

plt.text(6.9,1.8,'Inhomo. Phase?',rotation=0, ha='center', va='bottom',zorder=10, size=9, color='0')
plt.text(6.9,1.8-0.5,'$\\langle\\bar{q}q\\rangle(\\vec{x})\\neq 0$',rotation=-0, ha='center', va='bottom',zorder=10, size=9, color='0')


plt.text(9.9,.9,'Farbsupraleiter',rotation=-0, ha='center', va='bottom',zorder=10, size=9, color='0')
plt.text(9.9,0.9-0.5,'$\\langle q q\\rangle\\neq 0$',rotation=-0, ha='center', va='bottom',zorder=10, size=9, color='0')

plt.text(9.9,6.6,'Quark–Gluon-Plasma',rotation=-0, ha='center', va='bottom',zorder=10, size=9, color='0')
plt.text(9.9,6.6-0.5,'$\\langle\\bar{q}q\\rangle\\approx 0$',rotation=-0, ha='center', va='bottom',zorder=10, size=9, color='0')

plt.text(2.8,2.9,'Hadronen',rotation=-0, ha='center', va='bottom',zorder=10, size=9, color='0')
plt.text(2.8,2.9-0.5,'$\\langle\\bar{q}q\\rangle\\neq 0$',rotation=-0, ha='center', va='bottom',zorder=10, size=9, color='0')

plt.text(2.95,0.2,'Nukleare Materie',rotation=-0, ha='center', va='bottom',zorder=10, size=9, color='0')
ax00.plot([1.6,1.6], [0,0.15], **plot_styles[0])
ax00.plot([1.6], [0.15], **point_styles[0])

plt.grid(False)


fig.set_size_inches(14 * cm, 8 * cm)
plt.tight_layout(pad=pad_default)
save_plot(fig, 'qcd_phasediagram_defense.pdf',300)