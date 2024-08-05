# -*- coding: utf-8 -*-
"""
@author Martin Jakob Steil (parts of the original code are due to Niklas Zorbach)
@date 2023-08-10T00:52
@brief Utilities and variables 
"""

import matplotlib.pyplot as plt
import matplotlib
plt.ioff()

import math
import os

## Parameters and variables
# initial plot settings:
cm = 1/2.54 #inch per centimeter

width_full = 14.0 #cm -- full width figure
width_half = 6.9 #cm -- one column figure
width_single = 8.6 #cm

pad_default=0.1 # 0.1*10pt=1pt=0.35mm
w_pad_default=1.0 # 1.0*10pt=10pt=3.5mm
h_pad_default=1.0 # 1.0*10pt=10pt=3.5mm

## Colors 
# Goethe CD RGB colors (https://www.puk.uni-frankfurt.de/53182959/Poster-Goethe-Spektrum-web.pdf)
# gu_colors={
#     'dunkelgrau':'#4d4b46',
#     'emoRot':'#b3062c',
#     'goetheBlau':'#00618f',
#     'gruen':'#737c45',
#     'hellesGruen':'#a5ab52',
#     'hellgrau':'#f8f6f5',
#     'lichtblau':'#48a9da',
#     'magenta':'#ad3b76',
#     'orange':'#c96215',
#     'purple':'#860047',
#     'sandgrau':'#e4e3dd',
#     'senfgelb':'#e3ba0f',
#     'sonnengelb':'#f7d926'    
# }
# CMYK converted RGBs (brigter/more vibrant)
gu_colors={
    'goetheBlau':'#007b99',
    'lichtBlau':'#31f5e7',
    'gruen':'#598c1f',
    'hellesGruen':'#8fc52e',
    'sonnenGelb':'#ffe10d',
    'senfGelb':'#f0b600',
    'orange':'#f54a00',
    'emoRot':'#e40030',
    'magenta':'#cf20c6',
    'purple':'#970073',
    'hellGrau':'#f0f0ee',
    'sandGrau':'#e1e9de',
    'dunkelGrau':'#30302d'
}

# TU Darmstadt CD RGB colors (https://www.intern.tu-darmstadt.de/media/medien_stabsstelle_km/services/medien_cd/das_bild_der_tu_darmstadt.pdf)
tuda_colors = {
    'a0': '#dcdcdc',    'a1': '#5d85c3',    'a10': '#c9308e',    'a11': '#804597',
    'a2': '#009cda',    'a3': '#50b695',    'a4': '#afcc50',    'a5': '#dddf48',
    'a6': '#ffe05c',    'a7': '#f8ba3c',    'a8': '#ee7a34',    'a9': '#e9503e',
    'b0': '#b5b5b5',    'b1': '#005aa9',    'b10': '#a60084',    'b11': '#721085',
    'b2': '#0083cc',    'b3': '#009d81',    'b4': '#99c000',    'b5': '#c9d400',
    'b6': '#fdca00',    'b7': '#f5a300',    'b8': '#ec6500',    'b9': '#e6001a',
    'c0': '#898989',    'c1': '#004e8a',    'c10': '#951169',    'c11': '#611c73',
    'c2': '#00689d',    'c3': '#008877',    'c4': '#7fab16',    'c5': '#b1bd00',
    'c6': '#d7ac00',    'c7': '#d28700',    'c8': '#cc4c03',    'c9': '#b90f22',
    'd0': '#535353',    'd1': '#243572',    'd10': '#732054',    'd11': '#4c226a',
    'd2': '#004e73',    'd3': '#00715e',    'd4': '#6a8b37',    'd5': '#99a604',
    'd6': '#ae8e00',    'd7': '#be6f00',    'd8': '#a94913',    'd9': '#9c1c26'
}

def fromRGBToColor(r, g, b):
    return '#%02x%02x%02x' % (abs(math.floor(r)), abs(math.floor(g)), abs(math.floor(b)))

def fromColorToRG(color):
    return tuple(int((color.lstrip('#'))[i:i+2], 16) for i in (0, 2, 4))

def blend_color(rgb1, rgb2,s=0.5):
    if isinstance(rgb1, str):
        r1, g1, b1 = fromColorToRG(rgb1)
    else:
        r1, g1, b1 = rgb1
    
    if isinstance(rgb2, str):
        r2, g2, b2 = fromColorToRG(rgb2)
    else:
        r2, g2, b2 = rgb2
    r3, g3, b3 = r1+(r2-r1)*s, g1+(g2-g1)*s, b1+(b2-b1)*s
    return fromRGBToColor(abs(math.floor(r3)), abs(math.floor(g3)), abs(math.floor(b3)))
                   
def get_color_list(rgb1, rgb2, steps=100):
    output = ['']*steps
    if isinstance(rgb1, str):
        r1, g1, b1 = fromColorToRG(rgb1)
    else:
        r1, g1, b1 = rgb1
    
    if isinstance(rgb2, str):
        r2, g2, b2 = fromColorToRG(rgb2)
    else:
        r2, g2, b2 = rgb2
    
    output[0]=fromRGBToColor(r1,g1,b1)
    output[-1]=fromRGBToColor(r2,g2,b2)
    if steps==2:
        return output
    
    rdelta, gdelta, bdelta = (r2-r1)/(steps-1), (g2-g1)/(steps-1), (b2-b1)/(steps-1)
    for step in range(steps-2):
        r1 += rdelta
        g1 += gdelta
        b1 += bdelta
        hexe = fromRGBToColor(abs(math.floor(r1)), abs(math.floor(g1)), abs(math.floor(b1)))
        output[step+1]=hexe
    return output

# Thesis color sheme
#colors=list(map(lambda c : tuda_colors[c],['b1', 'b9', 'c4','b10','b3','b8']))
colors=list(map(lambda c : gu_colors[c],['goetheBlau','emoRot','gruen','sonnenGelb','purple']))

gray='#898989'
white='#FFFFFF'
black='#000000'


## rcParams -- Plot styling
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"]}
)
plt.rc('text.latex', preamble=r'\usepackage{amsmath}\usepackage{amssymb}\usepackage{upgreek}\usepackage{pifont}')
		  
font_size = 10
plt.rcParams['font.size'] = font_size
plt.rcParams['font.family'] = 'Charter'
plt.rcParams['axes.labelsize'] = font_size
plt.rcParams['axes.linewidth'] = font_size / 12.
plt.rcParams['axes.titlesize'] = font_size
plt.rcParams['legend.fontsize'] = font_size
plt.rcParams['xtick.labelsize'] = font_size
plt.rcParams['ytick.labelsize'] = font_size

plt.rcParams['axes.grid'] = True

plt.rcParams["legend.loc"] = 'upper left'
plt.rcParams["legend.markerscale"] = 1.0
plt.rcParams["legend.borderpad"] = 0.2
plt.rcParams["legend.handlelength"] = 0.9
plt.rcParams["legend.handletextpad"] = 0.4
plt.rcParams["legend.borderaxespad"] = 0.2
plt.rcParams["legend.columnspacing"] = 1.0
plt.rcParams["legend.shadow"] = False
# plt.rcParams["legend.edgecolor"] = '#e0e8de'
# plt.rcParams["legend.frameon"] = False

plt.rcParams['contour.negative_linestyle'] = 'solid'

end_box_style=dict(boxstyle='round',alpha=0.8,facecolor='1',edgecolor='0.8')

import matplotlib.patheffects as PathEffects
from matplotlib.patches import Circle

def draw_circle_with_contoured_annotation(ax, x, y, label, cr=0.05,fs=font_size,lw=1,zo=10):
    circle = Circle([x,y], cr, facecolor='none', edgecolor=white,linewidth=lw,zorder=zo,transform=ax.transAxes)
    ax.add_patch(circle)
    txt=ax.text(x,y,label, fontsize=fs, ha='center', va='center_baseline',transform=ax.transAxes)
    if lw>0:
        txt.set_path_effects([PathEffects.withStroke(linewidth=lw, foreground='w')])

def draw_contoured_annotation(ax, x, y, label,fs=font_size,lw=1,zo=10):
    txt=ax.text(x,y,label, fontsize=fs, ha='center', va='center_baseline',transform=ax.transAxes)
    if lw>0:
        txt.set_path_effects([PathEffects.withStroke(linewidth=lw, foreground='w')])
        
        
def set_size(fig,width=width_single,height=10):
    fig.set_size_inches(width * cm, height * cm)
    # plt.tight_layout(pad=0.03, h_pad=1.0, w_pad=1.0)
    
def set_height_singleCol(fig,height=10,pad=pad_default):
    fig.set_size_inches(width_half * cm, height * cm)
    plt.tight_layout(pad=pad)

def set_height_twoCol(fig,height=10,
                      pad=pad_default,w_pad=w_pad_default,h_pad=h_pad_default):
    fig.set_size_inches(width_full * cm, height * cm)
    plt.tight_layout(pad=pad, w_pad=w_pad, h_pad=h_pad)
    
# plot save stuff:
def save_plot(fig, destination,dpiIn=300):
    directory = '/'.join(destination.split('/')[:-1])

    if not directory=='':
        if not os.path.exists(directory):
            os.makedirs(directory)

    plt.savefig(destination,dpi=dpiIn,transparent=False)
    plt.close()
