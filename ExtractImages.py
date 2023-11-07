import cv2
cap = cv2.VideoCapture('yourvideo.mp4')  # For Webcam

count = 0

while True:
    success, img = cap.read()
    cv2.imwrite(f'Images/watch/{count}.jpg',img)
    count +=1
    cv2.imshow("Original Image ", img)
    cv2.waitKey(1)
