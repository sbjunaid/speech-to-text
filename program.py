import speech_recognition as sr
audio_file=("j.wav")
r=sr.Recognizer()
with sr.AudioFile(audio_file) as src:
    audio=r.record(src)
try:
    print("audio file contains"+r.recognize_google(audio))
except sr.UnknownValueError:
    print("google speech recognition not understands")
except sr.RequestError:
    print("couldnot got the results")
    

