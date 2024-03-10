# Face Recognition using Python and ESP32

This project demonstrates how to perform face recognition using Python and ESP32 microcontroller. It utilizes the OpenCV and face_recognition libraries in Python to detect and recognize faces from a webcam feed. When a recognized face is detected, a command is sent to an ESP32 microcontroller to trigger an action, such as turning off a buzzer. Else if an intruder is detected the buxxer turns on the buzzer alterting the user.

## Requirements

- Python (version 3.9 recommended)
- OpenCV (for capturing images from webcam)
- face_recognition (for face detection and recognition)
- websocket-client (for communicating with ESP32 via WebSocket)

## Setup

1. **Install Python Dependencies:**
   Install the required Python libraries using pip:
   ```bash
   pip install opencv-python face_recognition websocket-client
   ```

2. **ESP32 Setup:**
   Ensure your ESP32 microcontroller is connected to your network and has a WebSocket server running. Replace the WebSocket URL in the `send_command_to_esp32()` function with the URL of your ESP32 WebSocket server.

3. **Face Images:**
   Prepare images of the faces you want to recognize. Ensure that each image contains only one face and is saved in the `faces` directory with the naming convention `personX.jpg`, where X is a sequential number starting from 1.

## Usage

1. **Run the Python Script:**
   Run the Python script `face_recognition_esp32.py` using the following command:
   ```bash
   python face_recognition_esp32.py
   ```

2. **Face Recognition:**
   The script will continuously capture frames from the webcam and perform face recognition. If a recognized face is detected, a command will be sent to the ESP32 microcontroller.

## Notes

- Ensure that the ESP32 WebSocket server is reachable from the machine running the Python script.
- Make sure that the face images used for recognition are clear and distinct to improve recognition accuracy.
- Customize the actions triggered by the ESP32 microcontroller based on your project requirements.

## Contributors

- Nithya Vaibhavi(https://github.com/NithyaVaibhavi)
