import cv2

cap = cv2.VideoCapture(0)

status, photo = cap.read() # It is use to click the photo.

# #this show the photo and hold it and distroy use close camara
# cv2.imshow("myphoto" , photo)
# cv2.waitKey() == 13
# cv2.destroyAllWindows()


#this section will capture the video here.
##while True:
#    status, photo = cap.read()
#    cv2.imshow("myphoto" , photo)
#    if cv2.waitKey(10) ==13 :
#        break
#cv2.destroyAllWindows()

#cap.release()













