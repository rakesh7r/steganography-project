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

binData = ''.join(format(ord(i), '08b') for i in data)
# print(binData)
img[0][0][0] = len(data)
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



res = Image.fromarray(img,'RGB')
res.save("result.jpg")
res.show()



# ============================= decode.py =============================
datalen2 = img[0][0][0] * 8
print(binData)
bindataindex = 0
data2 = ""
bindata2 = ""
print(data)
for i in range(len(img)):
    for j in range(len(img[i])):
        for k in range(len(img[i][j])):
            if i == 0 and j == 0 and k == 0 : 
                continue
            binary = str(np.binary_repr(img[i][j][k], width=8))
            bindata2 += binary[7]
            bindataindex += 1
            if datalen2 == bindataindex : break
        if datalen2 == bindataindex : break
    if datalen2 == bindataindex : break
print(data2, end="")
# =================== converting back to original text ====================
bindataindex = 0
temp_data = ""
for i in range(datalen2):
    temp_data += bindata2[i]
    if len(temp_data) == 8 :
        data2 += chr(int(temp_data,2))
        temp_data = ""
print(data2)