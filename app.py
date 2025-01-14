from flask import Flask, render_template, request # Flask for web app
import torch # PyTorch 
from transformers import pipeline # Hugging Face Transformers for NLP
import soundfile as sf # PySoundFile for reading audio file