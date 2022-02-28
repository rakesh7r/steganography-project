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
clicked = False
r = g = b = xpos = ypos = 0

data = ""

print(img)


res = Image.fromarray(img,'RGB')
res.save("result.jpg")
res.show()