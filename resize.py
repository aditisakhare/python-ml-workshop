#Write a script that resizes all images in a directory to 100x100. For your convenience, you can find attached a ZIP file with #some images in the Resources.


import cv2
import glob

images=glob.glob("*.jpg")

print(images)

for image in images:
    img=cv2.imread(image,0)
    re=cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,re)