from vosk import Model, KaldiRecognizer
import pyaudio
import json

model = Model('./pt')
recognizer = KaldiRecognizer(model, 64000)

cap = pyaudio.PyAudio()
stream = cap.open(format = pyaudio.paInt16, channels = 1, rate = 64000, input = True, frames_per_buffer = 32000)
stream.start_stream()

while True:
    data = stream.read(32000)
    if recognizer.AcceptWaveform(data):
        result = recognizer.Result()
        result = json.loads(result)

        if result is not None:
            text = result['text']
            print(text)