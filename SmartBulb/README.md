# Bulb Control with Text Input and Speech Recognition using DGX Server

This project demonstrates how to control a bulb using both text input and speech recognition. It utilizes an ESP32 microcontroller, Arduino, and Python scripts to interact with the bulb. The bulb can be controlled either by sending text commands via a web interface or by issuing voice commands through a server-based AI powered by DGX Server.

## Features

- Control the bulb manually via a web interface with text input.
- Control the bulb using voice commands through a server-based AI.
- Integrates with DGX Server for speech recognition and natural language processing.

## Software Requirements

- Arduino IDE
- Python (version 3.9 recommended)
- Python Libraries
  - SpeechRecognition
  - pyaudio
  - requests (for interacting with DGX Server)
- DGX Server bulb api

## Hardware Requirements

- ESP32 microcontroller or similar
- Bulb (connected to a relay for control)
- Jumper wires
- Power supply

### Installation

1. Clone this repository to your local machine
   ```bash
      git clone https://github.com/your-username/bulb-control-with-dgx-server.git
   ```

3. Install the required Python libraries:
```bash
      pip install SpeechRecognition pyaudio requests
 ```  

4. Install and set up DGX Server on your machine. Follow the instructions provided by DGX Server documentation for installation.

### Setup Arduino

1. Connect the relay module to your ESP32 according to the circuit diagram.
2. Upload the Arduino code from `arduino_code/bulb_control.ino` to your ESP32 using the Arduino IDE.

### Running the Python Scripts

1. Start DGX Server and ensure it's running.
2. Navigate to the `python_code` directory.
3. Run `bulb_control_server.py`:

     python bulb_control_server.py
 

4. Follow the instructions provided by DGX Server to set up your voice model and train it if necessary.

### Controlling the Bulb

- **Web Interface**: Access the web interface at `http://localhost:5000` or your ESP32's IP address to control the bulb manually with text input.
- **Voice Control**: Issue voice commands after setting up and training the server-based AI with DGX Server.

## Usage

- Use the web interface or issue voice commands to turn the bulb on or off.
- Experiment with different voice commands and text inputs to control the bulb in various ways.

## Contributors

- Nithya Vaibhavi(https://github.com/Nithya Vaibhavi)
- Jahnavi Sangam().
