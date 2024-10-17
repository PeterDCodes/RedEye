import cv2


print(cv2.__version__)
#camera set up for testing
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('webcam', frame)