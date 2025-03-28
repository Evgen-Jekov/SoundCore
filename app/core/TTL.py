import speech_recognition as sr

def listen_sounde():
    try:
        speech = sr.Recognizer()

        with sr.Microphone() as sound:
            speech.adjust_for_ambient_noise(source=sound, duration=0.5)
            audio = speech.listen(source=sound)
            query = speech.recognize_google(audio_data=audio, language='en-US').lower()
    
        return query
    except sr.UnknownValueError as e:
        return str(e)
    except sr.RequestError as e:
        return str(e)
    except sr.WaitTimeoutError as e:
        return str(e)
    except Exception as e:
        return str(e)