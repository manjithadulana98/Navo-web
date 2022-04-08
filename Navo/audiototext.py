# Python 2.x program to transcribe an Audio file
from unittest import result

import speech_recognition as sr

def audiototext():
    # use the audio file as the audio source
    r = sr.Recognizer()

    # open the file
    with sr.AudioFile('D:/Software Development/Navo/data/Happy.wav') as source:
        # listen for the data (load audio to memory)
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print(text)
        with open('D:/Software Development/Navo/data/Happy.txt', mode='w') as file:
            file.write(text)

# with sr.AudioFile('../../static/it19207346/AudioFiles/Part2.wav') as source:
#     # listen for the data (load audio to memory)
#     audio = r.listen(source)
#     text = r.recognize_google(audio)
#     with open('../../static/it19207346/Text/part2.txt', mode='w') as file:
#         file.write(text)