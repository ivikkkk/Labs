
import numpy as np
from PIL import Image
from math import floor


img_mat= np.zeros ((1000,1000,3),dtype = np.uint8)
#x0,y0,x1,y1 = 50.4, 30.5, 123.45,987.65
def line ( img_mat,x0,y0,x1,y1):
   # print (x0,y0,x1,y1)
    dMax= max(abs (floor(x0)-floor(x1)),abs (floor(y0)-floor(y1)))
    L= dMax + 1

    if (L==1):
         img_mat[floor(y0),floor(x0)]= 255
    else :
        dx = (x1- x0)/(L-1)
        dy = (y1- y0)/(L-1)
        for _ in range (int(L)):
            img_mat[floor(y0),floor(x0)]= 255
            x0 += dx
            y0+= dy
v=[]
f=[]
file = open('model.obj')

for s in file:
    spl = s.split ()
    if (spl[0] == 'v'):
        v.append ([float(spl[1]),float( spl[2]),float( spl [3])])

    if (spl[0] == 'f'):
        f.append ([int(spl[1].split('/')[0]), int( spl[2].split('/')[0]), int( spl[3].split('/')[0])])
for i in range (len(v)):
    
         m = v[i][0]*5000 + 500
         n = - v[i][1]*5000 + 500
         img_mat[floor(n),floor(m)]= 255




for i in range (len(f)):
    x0= v[f[i][0]-1][0]*5000 + 500
    y0= -v[f[i][0]-1][1]*5000 + 500
    x1= v[f[i][1]-1][0]*5000 + 500
    y1= -v[f[i][1]-1][1]*5000 + 500
    x2= v[f[i][2]-1][0]*5000 + 500
    y2= -v[f[i][2]-1][1]*5000 + 500

    line(img_mat,x0,y0,x1,y1)
    line(img_mat,x1,y1,x2,y2)
    line(img_mat,x2,y2,x0,y0)



img = Image.fromarray(img_mat)
img.save('img.png')
