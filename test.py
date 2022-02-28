import cv2
import pandas as pd
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']
img = cv2.imread(img_path)
clicked = False
r = g = b = xpos = ypos = 0

data = "hello! this is user7R"

imgList = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# convert the array to numpy array
imgList = np.array(imgList, dtype=np.long)
# imgList = np.array(imgList)
# print(type(imgList))
# conver a numpy array to binary format
# imgList = imgList.tobinary()
# print(imgList)

binData = ''.join(format(ord(i), '08b') for i in data)

print(binData)

# ==============inserting data into the image==================
imgList[0][0][0] = len(data)
# for i in range(0, 5):
#     print(imgList[0][i])

bindataindex = 0

for i in range(len(imgList)):
    for j in range(len(imgList[i])):
        for k in range(len(imgList[i][j])):
            binary = str(np.binary_repr(imgList[i][j][k], width=8))
            if i == 0 and j == 0 and k == 0 :
                continue
            binary = binary[:7] + str(binData[bindataindex]) + binary[8:]            
            bindataindex += 1
            imgList[i][j][k] = int(binary, 2)
            if(bindataindex == len(binData)):
                break
        if(bindataindex == len(binData)):
            break    
    if(bindataindex == len(binData)):
        break

# print()
# for i in range(0, 5):
#     print(imgList[0][i])
