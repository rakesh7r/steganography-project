import cv2
import pandas as pd
import argparse
import numpy as np
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']
img = cv2.imread(img_path)
data = ""

datalen = img[0][0][0]
print("Data length: ", datalen)

bindataindex = 0
for i in range(len(img)):
    for j in range(len(img[i])):
        for k in range(len(img[i][j])):
            binary = str(np.binary_repr(img[i][j][k], width=8))
            if i == 0 and j == 0 and k == 0 :
                continue
            data += binary[len(binary)-1]
            bindataindex += 1
            if(bindataindex == datalen):
                break
        if bindataindex == datalen : 
            break
    if bindataindex == datalen : 
        break
            
print("Decoded Data : " ,data)