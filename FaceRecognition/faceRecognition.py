# import face_recognition

# import websocket
# import time
# import os
# import requests


# def send_command_to_esp32(command):
#     websocket_url = "ws://192.168.200.182:81"  # Replace with your ESP32 WebSocket server URL
#     ws = websocket.create_connection(websocket_url)
#     ws.send(command)
#     ws.close()

# def recognize_faces():
#     # Load images and encode faces
#     known_face_encodings = []
#     known_face_names = []

#     # Load and encode images for each person
#     for i in range(11):
#         image = face_recognition.load_image_file(f"faces/person{i+1}.jpg")  # Update the path here
#         encoding = face_recognition.face_encodings(image)[0]  # Assuming there's only one face in each image
#         known_face_encodings.append(encoding)
#         known_face_names.append(f"Person {i+1}")

#     # New image for recognition
#     unknown_image = face_recognition.load_image_file("faces/person5.jpg")  # Update the path here
#     unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

#     # Compare with known faces
#     matches = face_recognition.compare_faces(known_face_encodings, unknown_encoding)

#     if True in matches:
#         first_match_index = matches.index(True)
#         print(f"This is {known_face_names[first_match_index]}")
#         send_command_to_esp32("off")
#         print("Sent 0")
#     else:
#         print("Unknown person")
#         send_command_to_esp32("on")
#         print('Sent 1')




# import cv2
# import face_recognition
# import websocket

# def send_command_to_esp32(command):
#     websocket_url = "ws://192.168.43.38:81"  # Replace with your ESP32 WebSocket server URL
#     ws = websocket.create_connection(websocket_url)
#     ws.send(command)
#     ws.close()

# def recognize_faces_in_video():
#     # Load known faces
#     known_face_encodings = []
#     known_face_names = []

#     for i in range(11):
#         # Load and encode known faces
#         known_image = face_recognition.load_image_file(f"faces/person{i+1}.jpg")
#         known_encoding = face_recognition.face_encodings(known_image)[0]
#         known_face_encodings.append(known_encoding)
#         known_face_names.append(f"Person {i+1}")

#     # Open webcam capture
#     video_capture = cv2.VideoCapture(0)

#     while True:
#         # Read a single frame from the webcam
#         ret, frame = video_capture.read()

#         # Find all face locations and encodings in the current frame
#         face_locations = face_recognition.face_locations(frame)
#         face_encodings = face_recognition.face_encodings(frame, face_locations)

#         for face_encoding in face_encodings:
#             # Compare face encodings with known faces
#             matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#             name = "Unknown"

#             if True in matches:
#                 first_match_index = matches.index(True)
#                 name = known_face_names[first_match_index]

#                 # Send command to ESP32 based on recognition result
#                 if name == "Unknown":
#                     send_command_to_esp32("on")
#                 else:
#                     send_command_to_esp32("off")

#             # Draw rectangle and label on the face
#             top, right, bottom, left = face_locations[0]
#             cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
#             cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

#         # Display the resulting frame
#         cv2.imshow('Video', frame)

#         # Break the loop if 'q' is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release video capture and close OpenCV windows
#     video_capture.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     recognize_faces_in_video()


import cv2
import face_recognition
import websocket

def send_command_to_esp32(command):
    websocket_url = "ws://192.168.195.136:81"  # Replace with your ESP32 WebSocket server URL
    ws = websocket.create_connection(websocket_url)
    ws.send(command)
    ws.close()

def recognize_faces():
    # Load images and encode faces
    known_face_encodings = []
    known_face_names = []

    # Load and encode images for each person
    for i in range(5):
        image = face_recognition.load_image_file(f"faces/person{i+1}.jpg")
        print(image)
        encoding = face_recognition.face_encodings(image)[0]  # Assuming there's only one face in each image
        known_face_encodings.append(encoding)
        known_face_names.append(f"Person {i+1}")

    # Capture image from webcam
    print("capturing")
    video_capture = cv2.VideoCapture(0)
    ret, frame = video_capture.read()

    # Find faces in the frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    print("loaded")
    if len(face_encodings) > 0:
        # Assuming only one face is captured in the webcam frame
        unknown_encoding = face_encodings[0]

        # Compare with known faces
        matches = face_recognition.compare_faces(known_face_encodings, unknown_encoding)

        if True in matches:
            first_match_index = matches.index(True)
            print(f"This is {known_face_names[first_match_index]}")
            # send_command_to_esp32("off")
            print("Sent 0")
        else:
            print("Unknown person")
            # send_command_to_esp32("on")
            print('Sent 1')

    video_capture.release()
    cv2.destroyAllWindows()

# Continuously listen for speech
# send_command_to_esp32("off")
while True:
    recognize_faces()



# import face_recognition
# import cv2
# import serial
# import time

# # Connect to Arduino via Serial
# arduino_port = "COM3"  # Update with your Arduino's serial port
# ser = serial.Serial(arduino_port, 9600)
# time.sleep(2)  # Wait for the Arduino to initialize

# # Load known face encodings
# known_face_encodings = []
# known_face_names = ["person8"]

# for name in known_face_names:
#     image_path = f"{name}.jpg"
#     img = face_recognition.load_image_file(image_path)
#     encoding = face_recognition.face_encodings(img)[0]
#     known_face_encodings.append(encoding)

# # Initialize video capture
# video_capture = cv2.VideoCapture(0)

# while True:
#     # Capture frame-by-frame
#     ret, frame = video_capture.read()

#     # Find face locations and encodings
#     face_locations = face_recognition.face_locations(frame)
#     face_encodings = face_recognition.face_encodings(frame, face_locations)

#     for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#         # Check if the face matches any known faces
#         matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

#         name = "Unknown"

#         if True in matches:
#             first_match_index = matches.index(True)
#             name = known_face_names[first_match_index]

#         # Send recognition result to Arduino
#         ser.write(name.encode())

#         # Draw rectangle and name on the frame
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
#         font = cv2.FONT_HERSHEY_DUPLEX
#         cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

#     # Display the resulting frame
#     cv2.imshow('Video', frame)

#     # Break the loop if 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release video capture and close windows
# video_capture.release()
# cv2.destroyAllWindows()