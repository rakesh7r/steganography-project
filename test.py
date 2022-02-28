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

data = "hello! this is user7R"

# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# convert the array to numpy array
# img = np.array(img, dtype=np.long)
# img = np.array(img)
# print(type(img))
# conver a numpy array to binary format
# img = img.tobinary()
# print(img)

binData = ''.join(format(ord(i), '08b') for i in data)

print(binData)

# ==============inserting data into the image==================
img[0][0][0] = len(data)
# for i in range(0, 5):
#     print(img[0][i])

bindataindex = 0

for i in range(len(img)):
    for j in range(len(img[i])):
        for k in range(len(img[i][j])):
            binary = str(np.binary_repr(img[i][j][k], width=8))
            if i == 0 and j == 0 and k == 0 :
                continue
            binary = binary[:7] + str(binData[bindataindex]) + binary[8:]            
            bindataindex += 1
            img[i][j][k] = int(binary, 2)
            if(bindataindex == len(binData)):
                break
        if(bindataindex == len(binData)):
            break    
    if(bindataindex == len(binData)):
        break

print()
# for i in range(0, 5):
    # print(img[0][i])

res = Image.fromarray(img,'RGB')
res.save("result.jpg")
res.show()
# generating the result image



