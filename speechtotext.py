import speech_recognition as sr
rec = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    rec.adjust_for_ambient_noise(source)
    print("recording started..")
    audio = rec.listen(source)

file = open("s2txt.txt", "a")
try:
    file.write("\n" + rec.recognize_google(audio))

except sr.UnknownValueError:
    print("Audio is too noisy :(")

file.close()
