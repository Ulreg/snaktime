# IMPORT
# SpeechRecognition: This library is used for speech recognition and transcription.
# NLTK: This library is used for grammar correction.
# gTTS: This library is used for text-to-speech synthesis.

import speech_recognition as sr
import nltk
from gtts import gTTS

# Load the audio file
audio_file = sr.AudioFile('~/PycharmProjects/snaktime/audio/Minoptagelse69.m4a')

# Transcribe the audio file into text
r = sr.Recognizer()
with audio_file as source:
    audio_text = r.record(source)

# Correct the grammar of the transcribed text
# Code for grammar correction goes here
# Download necessary data for grammar correction
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Parse and correct grammar
text = nltk.parse.chart.parse(text)

# Generate a text-to-speech audio file
tts = gTTS(text=corrected_text, lang='en')
tts.save('output.mp3')

# Generate TTS audio file
tts = gtts.gTTS(text)
tts.save('path/to/output/file.mp3')