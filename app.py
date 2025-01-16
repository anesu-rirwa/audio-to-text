from flask import Flask, render_template, request
import torch # PyTorch 
from transformers import pipeline # Hugging Face Transformers for NLP
import soundfile as sf # PySoundFile for reading audio file

# Initialize Flask app
app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return render_template('index.html')