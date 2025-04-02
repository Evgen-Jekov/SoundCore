import speech_recognition as sr
from config import STTConfig

class STT:
    def __init__(self, control : STTConfig):
        self.control = control
        

    def listen_sounde(self):
        try:
            with sr.Microphone() as sound:
                self.control.speech.adjust_for_ambient_noise(source=sound, duration=1)
                audio = self.control.speech.listen(source=sound)
                
                if self.control.engine == 'google':
                    result = self.control.speech.recognize_google(audio_data=audio, language='ru-RU')
                elif self.control.engine == 'vosk':
                    result = self.control.speech.recognize_vosk(audio_data=audio, language='ru-RU')
                
            return result
        except sr.UnknownValueError as e:
            return str(e)
        except sr.RequestError as e:
            return str(e)
        except sr.WaitTimeoutError as e:
            return str(e)
        except Exception as e:
            return str(e)