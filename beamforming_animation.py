import waves
from tqdm import tqdm
import numpy as np
from matplotlib import pyplot as plt
import cv2
import imageio


if __name__ == "__main__":
    ############
    """let 1 px = 1um"""
    LAMBDA = 40
    HEIGHT = 600
    WIDTH  = 400
    TRANSMITTERS = 20
    ############
    disp = np.zeros((HEIGHT,WIDTH))
    sources = []
    frames = []
    for i in range(-int(TRANSMITTERS/2), int(TRANSMITTERS/2)):
        sources.append(waves.Point_Source(WIDTH/2 + 10*i, HEIGHT-10, LAMBDA))

    for phi in tqdm(np.linspace(-np.pi/4, np.pi/4, 50), desc = "generating frames"):
        disp = np.zeros((HEIGHT,WIDTH))
        for s in range(len(sources)):
            sources[s].alter_phase(s * phi)
            sources[s].gen_wave(disp)
        disp = disp**2 # obtain intensity
        disp = np.array(255 * disp / np.max(disp), dtype=np.uint8)
        for s in range(len(sources)):
            disp = cv2.circle(disp, (sources[s].x, sources[s].y), 3, (255,0,255), 2)
        frames.append(disp)
    frames.extend(frames[::-1])#reverse pass
    imageio.mimwrite("beamforming.gif", np.array(frames).astype(np.uint8), format= '.gif', fps = 20)
    
