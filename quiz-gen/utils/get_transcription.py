# Imports
import assemblyai as aai
import streamlit as st

# Audio to Text
def get_transcription():
    aai.settings.api_key = "673d17f0f011440282ba2d69bd311e71"

    # URL of the file to transcribe
    FILE_URL = "audio.mp3"

    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(FILE_URL)

    print("Audio to Text Converted.")

    return transcript.text