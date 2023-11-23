from flask import Flask, render_template, request
import speech_recognition as sr
from googletrans import Translator
from pydub import AudioSegment
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

translator = Translator()

def convert_audio(audio_file):
    # Get the filename from the FileStorage object
    filename = secure_filename(audio_file.filename)

    # Ensure the 'uploads' directory exists
    uploads_dir = os.path.join(os.getcwd(), 'uploads')
    os.makedirs(uploads_dir, exist_ok=True)

    # Save the audio file
    audio_path = os.path.join(uploads_dir, filename)
    audio_file.save(audio_path)

    # Convert audio file to WAV format
    audio = AudioSegment.from_file(audio_path)
    converted_audio_path = os.path.join(uploads_dir, os.path.splitext(filename)[0] + ".wav")
    audio.export(converted_audio_path, format="wav")

    return converted_audio_path

def recognize_speech(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        print("Speech Recognition Result:", text)
        return text
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def translate_text(text, target_language):
    translation = translator.translate(text, dest=target_language)
    return translation.text

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'audio_file' in request.files:
            audio_file = request.files['audio_file']
            if audio_file.filename != '':
                # Process audio file
                converted_audio = convert_audio(audio_file)
                audio_text = recognize_speech(converted_audio)
                if audio_text:
                    target_language = request.form['target_language']
                    translated_text = translate_text(audio_text, target_language)
                    return render_template('index.html', original_text=audio_text, translated_text=translated_text)

    return render_template('index.html', original_text=None, translated_text=None)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
