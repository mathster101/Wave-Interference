# -*- coding: utf-8 -*-
"""
Created on Tue May 24 00:06:41 2022

@author: mathew.panicker
"""
import numpy as np
from matplotlib import pyplot as plt
from tqdm import tqdm
import cv2

class Point_Source:
    def __init__(self, x, y, lamb, phase_offset = 0, intensity = 1):
        self.x = int(x)
        self.y = int(y)
        self.lamb = lamb
        self.phase = phase_offset
        self.intensity = intensity

    def alter_phase(self, new_phase = 0):
        self.phase = new_phase
        
    def gen_wave(self,disp):        
        if len(disp) == 0:
            print("error: array size is zero")
            return [0]
        two_pi = 2*np.pi
        rows = len(disp)
        cols = len(disp[0])
        row = list(range(rows))
        col = list(range(cols))
        row_mat = np.rot90([row]*cols, -1) - self.y
        col_mat = np.array([col]*rows) - self.x
        distance_matrix = np.sqrt(np.power(row_mat,2) + np.power(col_mat,2))
        disp += np.sin(two_pi * distance_matrix / self.lamb + self.phase) * self.intensity 
        return disp


if __name__ == "__main__":
    ############
    """let 1 px = 1um"""
    LAMBDA = 60
    HEIGHT = 1000
    WIDTH  = 800
    ############
    disp = np.zeros((HEIGHT,WIDTH))
    sources = []
    for i in tqdm(range(-5,5)):
        sources.append(Point_Source(WIDTH/2 + 20*i, HEIGHT-150, LAMBDA))
        sources[-1].gen_wave(disp)
    disp = disp**2 # obtain intensity
    disp = np.array(255 * disp / np.max(disp), dtype=np.uint8)
    for src in sources:
        disp = cv2.circle(disp, (src.x, src.y), 5, (255,0,255), 5)
    plt.imshow(disp, cmap = 'viridis')
    plt.show()