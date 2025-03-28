import speech_recognition as sr

speech = sr.Recognizer()

with sr.Microphone() as sound:
    speech.adjust_for_ambient_noise(source=sound, duration=0.5)
    audio = speech.listen(source=sound)
    query = speech.recognize_google(audio_data=audio, language='en-US').lower()
    print(query)


