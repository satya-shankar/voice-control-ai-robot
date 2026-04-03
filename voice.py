import speech_recognition as sr
import serial
import time

# Arduino से serial connection (COM पोर्ट बदलें)
arduino = serial.Serial('COM3', 9600)
time.sleep(2)  # Arduino को reset होने का समय दें

recognizer = sr.Recognizer()
mic = sr.Microphone()

print("Say a command...")

with mic as source:
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    command = recognizer.recognize_google(audio).lower()
    print("You said:", command)

    if "forward" in command:
        arduino.write(b'F')
    elif "back" in command:
        arduino.write(b'B')
    elif "left" in command:
        arduino.write(b'L')
    elif "right" in command:
        arduino.write(b'R')
    elif "stop" in command:
        arduino.write(b'S')
    else:
        print("Command not recognized")

except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
except sr.RequestError:
    print("Could not request results from speech service.")
