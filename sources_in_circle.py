# -*- coding: utf-8 -*-
"""
Created on Thu May 26 16:24:20 2022

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
    LAMBDA = 100
    RADIUS = 50
    HEIGHT = 400
    WIDTH  = 400
    TOWERS = 5
    ############
    towers = []
    f_buf = []
    for i in np.linspace(0, 2*np.pi, TOWERS,endpoint = False):
        dx = int(RADIUS * np.cos(i))
        dy = int(RADIUS * np.sin(i))
        towers.append(waves.Point_Source(WIDTH/2 + dx, HEIGHT/2 + dy, LAMBDA))
        
    for phi in tqdm(np.arange(0, np.pi, 0.1)):
        disp = np.zeros((WIDTH,HEIGHT))
        for t in range(len(towers)):
            towers[t].alter_phase(phi)
            towers[t].gen_wave(disp)
        f_buf.append(disp**2)

    disp = np.zeros((WIDTH,HEIGHT))
    for f in f_buf:
        disp += f
    disp = 255 * disp / np.max(disp)
    for tower in towers:
        disp = cv2.circle(disp, (tower.x, tower.y), 2, (0, 0, 0), 2)
    plt.imshow(disp, cmap = 'viridis')
    plt.show()    
        