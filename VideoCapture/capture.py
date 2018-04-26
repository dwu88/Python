import cv2,time
from mss import mss
import numpy
video =cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while True:

    check, frame = video.read()
    print(type(frame))
    if check == True:


        # Write frame
        out.write(frame)
        # Show current captured image
        cv2.imshow("Capturing", frame)
        key=cv2.waitKey(1)

        # Stop catpure by pressing the q key
        if key==ord('q'):
            break
    else:
        break

video.release()
out.release()
cv2.destroyAllWindows()
