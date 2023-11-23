import os
import speech_recognition as sr
from pydub import AudioSegment

def convert_to_wav(input_path, output_path):
    audio = AudioSegment.from_mp3(input_path)
    audio.export(output_path, format="wav")

def train_stt_model(audio_folder, language):
    recognizer = sr.Recognizer()
    model_data = []

    for filename in os.listdir(audio_folder):
        if filename.endswith(".mp3"):
            mp3_path = os.path.join(audio_folder, filename)
            wav_path = os.path.join(audio_folder, filename.replace(".mp3", ".wav"))

            # Convert MP3 to WAV
            convert_to_wav(mp3_path, wav_path)

            with sr.AudioFile(wav_path) as source:
                audio = recognizer.record(source)
                text = recognizer.recognize_google(audio, language=language)
                model_data.append((wav_path, text))

    return model_data

# Replace these paths with your actual audio folders and language codes
english_audio_folder = r"C:\Users\My PC\Desktop\userhelp\english_audio"
hindi_audio_folder = r"C:\Users\My PC\Desktop\userhelp\hindi_audio"
kannada_audio_folder = r"C:\Users\My PC\Desktop\userhelp\kannada_audio"
telugu_audio_folder = r"C:\Users\My PC\Desktop\userhelp\telugu_audio"

# Train the model for each language
english_model_data = train_stt_model(english_audio_folder, "en-IN")
hindi_model_data = train_stt_model(hindi_audio_folder, "hi-IN")
kannada_model_data = train_stt_model(kannada_audio_folder, "kn-IN")
telugu_model_data = train_stt_model(telugu_audio_folder, "te-IN")

# Display the training data
for audio_path, text in english_model_data:
    print(f"English Audio: {audio_path}, Text: {text}")

for audio_path, text in hindi_model_data:
    print(f"Hindi Audio: {audio_path}, Text: {text}")

for audio_path, text in kannada_model_data:
    print(f"Kannada Audio: {audio_path}, Text: {text}")

for audio_path, text in telugu_model_data:
    print(f"Telugu Audio: {audio_path}, Text: {text}")
