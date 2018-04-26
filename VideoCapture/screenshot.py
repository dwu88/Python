import cv2
import numpy as np
from PIL import ImageGrab

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Xin.avi',fourcc,20.0,(800,600))


while True:

    img = ImageGrab.grab()
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
    cv2.imshow('Records Screen',frame)
    out.write(frame)


    if cv2.waitKey(1) == 27:
        break
        
out.release()
cv2.destroyAllWindows()
