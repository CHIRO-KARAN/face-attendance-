import cv2

#ip cam
import urllib
import numpy as np
import imutils

url="http://192.168.43.131:8080/shot.jpg"


cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
count = 0

while(True):

    ret,frame = cap.read() # return a single frame in variable `frame`

    #ip cam
    
imgPath=urllib.urlopen(url)
imgNp=np.array(bytearray(imgPath.read()),dtype=np.uint8)
img=cv2.imdecode(imgNp,-1)
frame=imutils.resize(img, width=600)
    
cv2.imshow('image',frame) #display the captured image
key =  cv2.waitKey(1) & 0xFF    
    
if key == ord('c'):   #save on pressing 'c'        
        cv2.imwrite(str(count)+'.png',frame)
        count=count+1
        print(count)
        cv2.destroyAllWindows()
        
if key == ord('q'):
        cv2.destroyAllWindows()
            break

cap.release()
