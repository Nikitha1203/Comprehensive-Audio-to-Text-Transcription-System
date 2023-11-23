# Comprehensive-Audio-to-Text-Transcription-System
 audio-to-text transcription system that utilizes cutting-edge technologies to convert spoken words into written text. This project is designed to handle various audio formats and provide accurate transcriptions, making it a valuable tool for applications such as speech recognition, voice assistants, and more.

Features
Multi-format Audio Support: AcousticDecipher supports a wide range of audio formats, ensuring flexibility and compatibility with different sources.

High Accuracy Transcription: Leveraging advanced speech recognition algorithms, the system achieves high accuracy in transcribing spoken content.

Easy Integration: The project is built with simplicity and ease of integration in mind, allowing developers to seamlessly incorporate it into their applications.

Requirements
Python 3.10
Flask==2.0.0
googletrans==4.0.0-rc1
pydub==0.25.1
SpeechRecognition
PocketSphinx
gunicorn==20.1.0

Docker file :
docker build -t your_image_name:your_tag .
docker run  -p 5001:5001  your_image_name:your_tag 
Access the Application
Visit http://localhost:5001

![Screenshot 2023-11-23 112521](https://github.com/Nikitha1203/Comprehensive-Audio-to-Text-Transcription-System/assets/109364397/5fb14965-f18e-4841-8238-3feca6feb0a2)
