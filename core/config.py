from pydantic import BaseModel, Field
from typing import Literal
import speech_recognition as sr

class STTConfig(BaseModel):
    duration : float = Field(default=0.5, gt=0)
    language : str = Field(default='ru-RU')
    timeout : float | None = Field(default=None)
    phrase_time_limit : float | None = Field(default=None)
    engine : Literal['google', 'vosk'] = 'google'
    speech : sr.Recognizer = Field(default_factory=sr.Recognizer)
    source_type : str = Field(default='micro')
    file_path : str | None = Field(default=None)
    
class TTSConfig():
    pass