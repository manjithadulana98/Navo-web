import os
import speech_recognition as sr
import ffmpeg
 t= 
command2mp3 = "ffmpeg -i Happy.mp4 Happy.mp3"
command2wav = "ffmpeg -i Happy.mp3 Happy.wav"

os.system(command2mp3)
os.system(command2wav)

r = sr.Recognizer()

with sr.AudioFile('Happy.wav') as source:
    audio = r.record(source, duration=100)
    
print(r.recognize_google(audio))