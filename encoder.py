import pandas as pd
import numpy as np
from PIL import Image

img = input("Enter image name(with extension) : ")
# img = "colorpic.png"
image = Image.open(img, 'r')
newimg = image.copy()

data = input("Enter data to be encoded: ")
data +=  "0"

if len(data) == 0: 
    raise Exception('Data is empty')

binData = ''.join(format(ord(i), '08b') for i in data)

bindataindex = 0

width, height = newimg.size
newimg.putpixel((width-1,height-1), (len(data), 0, 0))

for i in range(width):
    for j in range(height):
        if bindataindex >= len(binData):break
        r,g,b = newimg.getpixel((i, j))
        r = str(np.binary_repr(r, width=8))
        g = str(np.binary_repr(g, width=8))
        b = str(np.binary_repr(b, width=8))
        r = r[:7] + str(binData[bindataindex])
        bindataindex += 1
        if bindataindex >= len(binData):break
        g = g[:7] + str(binData[bindataindex])
        bindataindex += 1
        if bindataindex >= len(binData):break
        b = b[:7] + str(binData[bindataindex])
        bindataindex += 1
        if bindataindex >= len(binData):break
        newimg.putpixel((i, j), (int(r, 2), int(g, 2), int(b, 2)))
        if(i == width-1 and j == height-1):
            break
    if bindataindex >= len(binData):
        break
print(binData)    
newimg.save("result.png")
# newimg.show()