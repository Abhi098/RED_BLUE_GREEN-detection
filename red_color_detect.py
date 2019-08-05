import cv2
import numpy as np

# object tracking video 

cap=cv2.VideoCapture(0)
while(1):
	_,img=cap.read()
	hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	# define range of blue color in HSV
	lower_red = np.array([161, 155, 84])
	upper_red = np.array([179, 255, 255])
	# Threshold the HSV image to get only blue colors
	mask = cv2.inRange(hsv, lower_red, upper_red)
	# Bitwise-AND mask and original image
	res = cv2.bitwise_and(img,img, mask= mask)
	cv2.imshow('frame',img)
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)
	k = cv2.waitKey(5) & 0xFF
	if k==27:
		break


cv2.destroyAllWindows()
cap.release()

# low_red = np.array([161, 155, 84])
# high_red = np.array([179, 255, 255])

# low_blue = np.array([94, 80, 2])
# high_blue = np.array([126, 255, 255])


# low_green = np.array([25, 52, 72])
# high_green = np.array([102, 255, 255]) 