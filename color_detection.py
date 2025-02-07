import cv2
from utils import get_limits
from PIL import Image


blue=[255,0,0] 
cap=cv2.VideoCapture(0)


while True:
    ret, frame=cap.read()

 

    get_limits(color=blue)



    hsvImage=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    
    lowerlimits, upperLimits= get_limits(color=blue)

    mask=cv2.inRange(hsvImage, lowerlimits, upperLimits)
    
  
    mask1=Image.fromarray(mask)
    
    
   

    
    bbox=mask1.getbbox()


    if bbox is not None:
       x1,y1, x2, y2= bbox
       frame=cv2.rectangle(frame, (x1,y1),(x2,y2), (0,255,0), 5)

       cv2.putText(frame, "Blue", (x1,y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0),0)



    cv2.imshow('Frame', frame)

    #stop program by pressing q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()

