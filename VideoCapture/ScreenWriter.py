import cv2
from PIL import ImageGrab
import numpy as np
import sys


class ScreenWriter:

    def __init__(self,switch,display_width,display_height):
        self.fourcc = cv2.VideoWriter_fourcc(*'DIVX')
        self.out = cv2.VideoWriter('output.avi',self.fourcc,20.0,(display_width,display_height))
        self.switch = switch

    def startRecord(self):
        try:
            while self.switch:
                img = np.array(ImageGrab.grab())
                frame = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                #cv2.imshow("Recording",frame)
                self.out.write(frame)

                #if cv2.waitKey(1) == ord('q'):
                        #break
        except InterruptedError:
            pass

    def stopRecord(self):
        self.out.release()
        self.switch = False
