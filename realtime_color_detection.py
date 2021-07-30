import cv2
import numpy as np
from djitellopy import tello

def main():
   me = tello.Tello()
   me.connect()
   me.streamon()
   while True:
       img = me.get_frame_read().frame
       imgmain=cv2.resize(img,(720,540))
       imgHsv=cv2.cvtColor(imgmain,cv2.COLOR_BGR2HSV)
       xarray=[]
       yarray=[]
       lower=np.array([87,137,177])
       upper=np.array([179,255,255])
       mask=cv2.inRange(imgHsv,lower,upper)
       count = 0
       for x in range(720):
           for y in range(540):
               if int(mask[y,x])==255:
                   xarray.append(x)
                   count=count+1
                   yarray.append(y)
       centerx=0
       centery=0
       if len(xarray)!=0:
           centerx=int(np.sum(xarray)/count)
           centery=int(np.sum(yarray)/count)
           cv2.circle(imgmain, (int(centerx), int(centery)), 3, (255, 0, 255), -1)
       cv2.imshow("original",imgmain)
       cv2.imshow("final", mask)
       cv2.waitKey((1))

if __name__=="__main__":
   main()
