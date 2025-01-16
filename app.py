import os
import librosa
import torch
import streamlit as st
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer

# Load Wav2Vec2 model and tokenizer
MODEL_NAME = "facebook/wav2vec2-base-960h"
tokenizer = Wav2Vec2Tokenizer.from_pretrained(MODEL_NAME)
model = Wav2Vec2ForCTC.from_pretrained(MODEL_NAME)

# Streamlit App
st.title("Audio to Text Transcription")
st.write("Upload an audio file (wav, mp3, flac) to transcribe it to text.")

uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3", "flac"])

if uploaded_file is not None:
    try:
        # Save the uploaded file temporarily
        file_path = os.path.join("temp_audio", uploaded_file.name)
        os.makedirs("temp_audio", exist_ok=True)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

        # Load and process the audio file
        st.write("Processing the audio file...")
        audio, sr = librosa.load(file_path, sr=16000)
        input_values = tokenizer(audio, return_tensors="pt", sampling_rate=16000).input_values
        logits = model(input_values).logits
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = tokenizer.batch_decode(predicted_ids)[0]

        # Display the transcription
        st.success("Transcription completed successfully!")
        st.text_area("Transcription", transcription, height=200)

        # Clean up the temporary file
        os.remove(file_path)

    except Exception as e:
        st.error(f"An error occurred: {e}")
