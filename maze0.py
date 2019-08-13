from PIL import Image
import numpy as np
import ql_adv
import PIL
from skimage.io import imsave
def main(img):
    img = Image.open(img)
    l =[]
    for i in range(img.size[0]):
        x = []
        for j in range(img.size[1]):
            px = img.getpixel((i,j))
            x.append(px[0]/255)
        l.append(x)
    size  = ((img.size[0]-2)//16)
    ld = []

    for i in range(size):
        for j in range(size):
            x = []
            if l[j*16+1][i*16+8]==1:
                x.append(j-1+i*size)
            if l[j*16+17][i*16+8]==1:
                x.append(j+1 + i*size)
            if l[j*16+8][i*16+1]==1:
                x.append(j-size+i*size)
            if l[j*16+8][i*16+17]==1:
                x.append(j+size + i*size)
            ld.append(x) 
    ldd = []
    ins  = 0
    fs = 0
    for i in ld:
        x = []
        for j in i:
            if not (j<0 or j>(size**2)-1):
                x.append(j)
            elif j<0:
                ins = ld.index(i)
            else:
                fs = ld.index(i)
        ldd.append(x)
    ob = ql_adv.maze(size*size,ldd,ins,fs)
    route = ob.main()
    path = []
    i = route
    for j in range(len(i)-1):
        if i[j]-i[j+1]==1:
            path.append('l')
        if i[j]-i[j+1]==-1:
            path.append('r')
        if i[j]-i[j+1]==size:
            path.append('u')
        if i[j]-i[j+1]==size*-1:
            path.append('d')
    cell = route[0]
    dest = route[-1]
    xc = cell%size       
    xi1 = 9 + 16*xc
    xi2 = 10 + 16*xc
    yi = 10  
    for i in range(11):
        l[xi1][yi] = 128
        l[xi2][yi] = 128
        yi -= 1
    xc = dest%size 
    yc = dest//size
    xi1 = 9 + 16*xc
    xi2 = 10 + 16*xc
    yi = size*16-7
    for i in range(9):
        l[xi1][yi] = 128
        l[xi2][yi] = 128
        yi += 1

    for i in range(len(path)):
        cell = route[i]
        dest = route[i+1]
        dir = path[i]
        xc = cell%size 
        yc = cell//size
        if dir=='r':
            xi = 9 + 16*xc
            yi1 = 9 + 16*yc
            yi2 = 10 + 16*yc
            for i in range(18):
                l[xi][yi1] = 128
                l[xi][yi2] = 128
                xi += 1
        if dir=='l':
            xi = 10 + 16*xc
            yi1 = 9 + 16*yc
            yi2 = 10 + 16*yc
            for i in range(18):
                l[xi][yi1] = 128
                l[xi][yi2] = 128
                xi -= 1
        if dir=='u':
            xi1 = 9 + 16*xc
            xi2 = 10 + 16*xc
            yi = 10 + 16*yc
            for i in range(18):
                l[xi1][yi] = 128
                l[xi2][yi] = 128
                yi -= 1
        if dir=='d':
            xi1 = 9 + 16*xc
            xi2 = 10 + 16*xc
            yi = 9 + 16*yc
            for i in range(18):
                l[xi1][yi] = 128
                l[xi2][yi] = 128
                yi += 1

    for i in range(len(l)):
        for j in range(len(l)):
            if l[i][j]==128:
                l[i][j] = 0.5
    imsave('test.png',np.asarray(l).transpose()[:,:])
    inp = 'test.png'
