import cv2
import os

for img in os.listdir():
    image=cv2.imread(img,0)
    resized_image=cv2.resize(image, (100,100))
    cv2.imshow(img,resized_image)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite(img.rstrip(".jpg") + "_resized.jpg",resized_image)
