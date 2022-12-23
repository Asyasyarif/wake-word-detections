import threading
import time
import sounddevice as sd
import librosa
import numpy as np
from tensorflow.keras.models import load_model
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 1)

fs = 22050
seconds = 2

model = load_model("saved_model/WWD.h5")

def listener():
    while True:
      myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
      sd.wait()
      mfcc = librosa.feature.mfcc(y=myrecording.ravel(), sr=fs, n_mfcc=40)
      mfcc_processed = np.mean(mfcc.T, axis=0)
      prediction_thread(mfcc_processed)
      time.sleep(0.001)

def voice_thread():
    listen_thread = threading.Thread(target=listener, name="ListeningFunction")
    listen_thread.start()

def prediction(y):
    prediction = model.predict(np.expand_dims(y, axis=0))
    if prediction[:, 1] > 0.925:
      # if engine._inLoop:
      #   engine.endLoop()
      print("Hiiiii")
      time.sleep(0.1)

def prediction_thread(y):
    pred_thread = threading.Thread(target=prediction, name="PredictFunction", args=(y,))
    pred_thread.start()

voice_thread()