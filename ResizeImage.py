import cv2
import glob
import os

# Create folder
os.mkdir('images_resized/' + name)
# Absolute path of the target folder
inputFolder = ''
i = 0

for img in glob.glob(inputFolder + '/*.jpg'):
    print(img.split(inputFolder, 1)[1])
    tail = img.split(inputFolder, 1)[1]
    img = cv2.imread(img)
    # Resize image
    resizedImg = cv2.resize(img, (224, 224))
    
    # rename images
    cv2.imwrite('/home/user/images_resized' + tail, resizedImg)
    i += 1
    cv2.imshow('image', resizedImg)
    cv2.waitKey(30)
cv2.destroyAllWindows()