import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture =cv2.VideoCapture(0)

# Load Known Faces

priya_image = face_recognition.load_image_file("faces/priya.jpeg")
priya_encoding = face_recognition.face_encodings(priya_image)[0]

shivii_image = face_recognition.load_image_file("faces/shivii.jpeg")
shivii_encoding = face_recognition.face_encodings(shivii_image)[0]

known_face_encodings = [priya_encoding, shivii_encoding]
known_face_names = ["Priya" , "Shivii"]

# list of expected students
students = known_face_names.copy()

face_locations = []
face_encodings = []

# Get the current date and time
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f= open(f"{current_date}.csv", "w+", newline="")
lnwriter=csv.writer(f)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame,(0,0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Recognize faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encodings)
        best_match_index = np.argmin(face_distance)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]

    cv2.imshow("Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
          


