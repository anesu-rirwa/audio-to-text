from flask import Flask, render_template, request
import torch # PyTorch 
from transformers import pipeline # Hugging Face Transformers for NLP
import soundfile as sf # PySoundFile for reading audio file

# Initialize Flask app
app = Flask(__name__)

# Loading the model
model = pipeline("automatic-speech-recognition", model="facebook/wav2vec2-large-xlsr-53")

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# Audio File Processing
@app.route('/process', methods=['POST'])
def process_audio():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']

    if file.filename == '':
        return 'No selected file'
    
    # Read the audio file
    audio_data, sample_rate = sf.read(file)

    # Convert the audio data to tensor (suitable format for the model)
    audio_data = torch.tensor(audio_data, dtype=torch.float32)

    # Transcribe the audio
    transcription = model(audio_data)

    # Get the transcribed text
    transcribed_text = transcription['text']

    # Return the transcribed text
    return render_template('results.html', transcribed_text=transcribed_text)

if __name__ == '__main__':
    app.run(debug=True)