import cv2
import os
from cvzone.HandTrackingModule import HandDetector

# Capture image from webcam
cap = cv2.VideoCapture(0)
status, photo = cap.read()
cap.release()

if not status:
    print("Failed to capture image.")
    exit()

cv2.imshow('Jatin Pic', photo)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Initialize hand detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Detect hand
img, hands = detector.findHands(photo)

if hands:
    hand = hands[0]
    fingers = detector.fingersUp(hand)

    if fingers == [0, 1, 0, 0, 0]:
        os.system("start notepad")
    elif fingers == [0, 1, 1, 0, 0]:
        os.system("start https://www.google.com")
    elif fingers == [1, 1, 1, 1, 1]:
        os.system("start msedge")  # or "start MicrosoftEdge" depending on your system
    else:
        print("Gesture not recognized.")
else:
    print("No hand detected.")
