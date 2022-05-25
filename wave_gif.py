# -*- coding: utf-8 -*-
"""
Created on Wed May 25 18:19:24 2022

@author: matthew.panicker
"""

import waves
import numpy as np
import imageio
from tqdm import tqdm as tq
from matplotlib import pyplot as plt
import cv2
if __name__ == "__main__":
    ############
    """let 1 px = 1um"""
    LAMBDA = 100
    HEIGHT = 300
    WIDTH  = 300
    ############
    disp = np.zeros((HEIGHT,WIDTH))
    raw_frames = []
    heat_map = []
    p = waves.Point_Source(WIDTH/2, HEIGHT/2, LAMBDA)
    p.gen_wave(disp)
    raw_frames.append(disp)
    for phi in tq(np.arange(2*np.pi,0,-0.01), desc = "generating frames"):
        p.alter_phase(phi)
        disp = np.zeros((HEIGHT,WIDTH))
        p.gen_wave(disp)
        raw_frames.append(disp)
    
    for f in range(len(raw_frames)):
        raw_frames[f] = raw_frames[f]**2
        raw_frames[f] = 255 * raw_frames[f] / np.max(raw_frames[f])
        heat = cv2.applyColorMap(raw_frames[f].astype(np.uint8), cv2.COLORMAP_JET)
        heat_map.append(heat)  
    
    imageio.mimwrite("single_source.gif", np.array(heat_map).astype(np.uint8), format= '.gif', fps = 30)

        