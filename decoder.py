import pandas as pd
import numpy as np
from PIL import Image
import os

img = input("Enter image name(with extension) : ")
# img = "result.png"
image = Image.open(img, 'r')
newimg = image.copy()
width, height = newimg.size

datalen = newimg.getpixel((width-1,height-1))[0]
index = 0
data = ""

for i in range(width):
    for j in range(height):
        r,g,b = newimg.getpixel((i, j))
        r = str(np.binary_repr(r, width=8))
        g = str(np.binary_repr(g, width=8))
        b = str(np.binary_repr(b, width=8))
        data += r[7]
        if len(data) >= datalen: break
        data +=g[7]
        if len(data) >= datalen: break
        data +=b[7]
        if len(data) >= datalen: break
    if len(data) == datalen : break

# print(data)
temp_data = ""
text = ""
for i in range(len(data)):
    temp_data += data[i]
    if len(temp_data) == 8 :
        text+= chr(int(temp_data,2))
        temp_data = ""
# os.system("cls")
print("Decoded Text :" , text[0:len(text)-1])
print(" Terminated ...")