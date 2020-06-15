import cv2

cam = cv2.VideoCapture(0)#cv2.VideoCapture("./video.mp4")
model = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")

while True:
	ret, frame = cam.read()
	if ret == True:
		gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # bgr -> grayscale conversion
		faces = model.detectMultiScale(gray_frame, 1.3, 5)
		for face in faces:
			x, y, w, h = face

			cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
		cv2.imshow("window", frame)
		key = cv2.waitKey(1) # 1ms
		if key == ord("q"):
			break
	else:
		break

cam.release()
cv2.destroyAllWindows()