import os
import telebot
from moviepy.editor import *
import speech_recognition as sr
from deep_translator import GoogleTranslator as tr
from pytube import YouTube

# Telegram bot tokenini kiritish
TOKEN = '5773060087:AAHpLmsAqn4b8eIQaL997SX85N7wRE5R2WQ'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum! Matn yoki ovozli xabar yuboring")


@bot.message_handler(content_types=['text', 'voice', 'document'])
def echo_message(message):
    # Agar xabar text bo'lsa
    if message.content_type == 'text':
        link = message.text
        yt = YouTube(link)
        # eng yuqori sifatli video sifatini aniqlash
        stream = yt.streams.get_highest_resolution()
        # video yuklash
        stream.download()
        # video faylini "math.mp4" nomiga o'zgartirish
        os.rename(stream.default_filename, 'math.mp4')
        video = VideoFileClip('math.mp4')
        audio = video.audio.write_audiofile('audio.wav')
        r = sr.Recognizer()
        with sr.AudioFile('audio.wav') as source:
            audio = r.record(source)
        text = r.recognize_google(audio, language='en-US')
        tarjima = tr(source='auto', target='uz', ).translate(text)
         with open('tarjima.txt', 'w') as file:
            file.write(text + '\n\n' + tarjima)
            bot.send_document(message.chat.id, file)


    # Agar xabar ovozli fayl bo'lsa
    # elif message.content_type == 'voice':
    #     file_info = bot.get_file(message.voice.file_id)
    #     downloaded_file = bot.download_file(file_info.file_path)
    #     with open('audio.ogg', 'wb') as new_file:
    #         new_file.write(downloaded_file)
    #     audio = AudioSegment.from_ogg('audio.ogg')
    #     audio.export('audio.wav', format='wav')
    #
    #     r = sr.Recognizer()
    #     with sr.AudioFile('audio.wav') as source:
    #         audio = r.record(source)
    #
    #     text = r.recognize_google(audio, language='en-US')
    #     tarjima = tr(source='auto', target='uz', ).translate(text)
    #     with open("tarjima.txt", "rb") as file:
    #         bot.send_document(message.chat.id, file)
    #
    #     os.remove('audio.ogg')
    #     os.remove('audio.wav')


# Botni ishga tushirish
bot.polling(none_stop=True)

# @bot.message_handler(content_types=['text'])
# def youtube_download_vidio(message):
#     bot.send_message(message, 'youtube vido linkini yuboring')
#     link = message.text
#     # YouTube video obyektini yaratish
#     yt = YouTube(link)
#     # eng yuqori sifatli video sifatini aniqlash
#     stream = yt.streams.get_highest_resolution()
#     # video yuklash
#     stream.download()
#     # video faylini "math.mp4" nomiga o'zgartirish
#     os.rename(stream.default_filename, 'math.mp4')
# # Botni ishga tushirish
# bot.polling(none_stop=True)
