import speech_recognition as sr

def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        audio = recognizer.listen(source)

    with sr.Microphone() as source:
       print("Listening...")
       recognizer.adjust_for_ambient_noise(source, duration=1)
       audio = recognizer.listen(source)

    try:

        text = recognizer.recognize_google(audio)

        return text.lower()

    except Exception:

        return ""
    