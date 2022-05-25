# -*- coding: utf-8 -*-
"""
Created on Wed May 25 14:08:42 2022

@author: mathew.panicker
"""

import waves
import numpy as np
from tqdm import tqdm
from matplotlib import pyplot as plt
from random import randint as ri
import cv2

if __name__ == "__main__":
    ############
    """let 1 px = 1um"""
    LAMBDA = 50
    HEIGHT = 400
    WIDTH  = 400
    TOWERS = 3
    ############
    towers = []
    f_buf = []
    for i in range(TOWERS):
        towers.append(waves.Point_Source(ri(0,WIDTH), ri(0,HEIGHT), LAMBDA))
    
    for phi in tqdm(np.arange(0, np.pi, 0.1)):#sweep each tower's phase
        disp = np.zeros((HEIGHT,WIDTH))
        for i in range(len(towers)):
            towers[i].alter_phase(phi)
            disp = towers[i].gen_wave(disp)
        f_buf.append(disp**2)
    
    disp = np.zeros((HEIGHT,WIDTH))
    for f in f_buf:
        disp += f
    disp = 255 * disp / np.max(disp)
    for tower in towers:
        disp = cv2.circle(disp, (tower.x, tower.y), 5, (255,0,255), 5)
    plt.imshow(disp, cmap = 'viridis')
