import os
import moviepy.editor as mp
from moviepy.video.io.VideoFileClip import VideoFileClip
import speech_recognition as sr

def videotoaudio(t):
    video = VideoFileClip(r"D:/Software Development/Navo/data/" + t)
    audioclip = video.audio
    audioclip.write_audiofile(r"D:/Software Development/Navo/data/Happy.wav")

# video = VideoFileClip(r"../../static/it19207346/VideoFiles/Pythagoras_Part2.mp4")
# audioclip = video.audio
# audioclip.write_audiofile(r"../../static/it19207346/AudioFiles/part2.wav")


