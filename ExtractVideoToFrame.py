import cv2

# Opens the Video file
video_path = './example.mp4'
cap = cv2.VideoCapture(video_path)
i = 0
while cap.isOpened():
    ret, frame = cap.read()
    if ret is False:
        break
    cv2.imwrite('frame' + str(i) + '.jpg', frame)
    i += 1

cap.release()
cv2.destroyAllWindows()
