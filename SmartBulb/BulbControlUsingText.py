#simple bulb control using text input as "on" or "off" 
import speech_recognition as sr
import serial
import websocket
import time
import os

r = sr.Recognizer()

def send_command_to_esp32(command):
    websocket_url = "ws://192.168.195.136:81"  # Replace with your ESP32 WebSocket server URL
    ws = websocket.create_connection(websocket_url)
    ws.send(command)
    ws.close()

def recognize():

    try:
        text=input()

        print("You said: " + text)
        if "on" in text:
            send_command_to_esp32("on")
            print('Sent 1')
        elif "off" in text:
            send_command_to_esp32("off")
            print('Sent 0')
#
    except:
        print(10)
# Continuously listen for speech
send_command_to_esp32("off")
while True:
    recognize()

