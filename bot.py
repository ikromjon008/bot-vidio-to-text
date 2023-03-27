import speech_recognition as sr
from moviepy.editor import *
from deep_translator import GoogleTranslator as tr

# audio faylni o'qish uchun recognizer obyektni yaratish
r = sr.Recognizer()

# audio faylni o'qish
with sr.AudioFile('audio1.wav') as source:
    audio = r.record(source)

# Google Speech Recognition xizmatidan foydalanish
text = r.recognize_google(audio, language='en-US')
tarjima = tr(source='auto', target='uz',).translate(text)

# natijani chop etish
print(text)
print(tarjima)

# natijalarni faylga yozish
with open('tarjima.txt', 'w', encoding='utf-8') as file:
    file.write(text + '\n\n' + tarjima)
