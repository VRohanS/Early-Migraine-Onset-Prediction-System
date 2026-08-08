import cv2
import numpy as np
import sounddevice as sd

def get_light():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if not ret:
        return 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return np.mean(gray)

def get_audio():
    rec = sd.rec(44100, samplerate=44100, channels=1)
    sd.wait()
    return np.linalg.norm(rec)