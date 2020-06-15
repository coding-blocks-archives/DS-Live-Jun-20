import cv2
import numpy as np

cam = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

face_data = []

dataset_path = "./data/"

name  = input("Enter your name : ")


while True:
    ret, frame = cam.read()
    if ret == False:
        continue
        
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # bgr -> grayscale conversion
    faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)
    
    

    for face in faces:
        x, y, w, h = face
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
        
        offset = 10
        face_section = frame[y-offset : y+h+offset , x-offset : x+w+offset]
        face_section = cv2.resize(face_section , (100 , 100))
        
        face_data.append(face_section)
        
        cv2.imshow("cropped face", face_section)
    
    cv2.imshow("window", frame)

    key = cv2.waitKey(1) # 1ms
    if key == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()

# print(len(face_data))
# print(face_data[0].shape)

face_data = np.array(face_data)
face_data = face_data.reshape(face_data.shape[0], 3*100*100)
print(face_data.shape)

np.save(dataset_path+name + ".npy", face_data)
print("data saved at " + dataset_path+name + ".npy")













