# Audio-to-Text

This project is a simple web application that allows users to upload audio files (MP3, WAV), transcribe them into text using a Hugging Face speech-to-text model (`facebook/wav2vec2-large-xlsr-53`), and view or download the transcribed text.

## Features

- Upload audio files (MP3, WAV).
- Click a button to process the file and transcribe it to text.
- View the transcribed text on the web page.
- Easy-to-use web interface built with Flask.
- Uses Hugging Face's `wav2vec2` model for accurate speech-to-text transcription.

To run this application, you'll need to have the following installed on your local machine:

- Python 3.x
- Flask
- PyTorch
- Hugging Face Transformers
- Soundfile

# Audio-to-Text Transcriber

This project is a simple web application that allows users to upload audio files (MP3, WAV), transcribe them into text using a Hugging Face speech-to-text model (`facebook/wav2vec2-large-xlsr-53`), and view or download the transcribed text.

## Features

- Upload audio files (MP3, WAV).
- Click a button to process the file and transcribe it to text.
- View the transcribed text on the web page.
- Easy-to-use web interface built with Flask.
- Uses Hugging Face's `wav2vec2` model for accurate speech-to-text transcription.

## Requirements

To run this application, you'll need to have the following installed on your local machine:

- Python 3.x
- Flask
- PyTorch
- Hugging Face Transformers
- Soundfile

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/audio-to-text-transcriber.git
    ```

2. Navigate into the folder

    ```bash
    cd audio-to-text-transcriber
    ```

3. Install the required dependencies

    ```bash
    pip install -r requirements.txt
    ```

4. (Optional) Alternatively, you can manually install the required libraries using

    ```bash
    pip install flask transformers torch soundfile
    ```

## Project Structure

```bash
/audio-to-text
    /templates
        index.html      # Frontend for uploading audio
        result.html     # Frontend to display transcribed text
    app.py             # Python backend (Flask app)
    requirements.txt   # List of dependencies
```

- **app.py**: Main Python file where the Flask web application runs. Handles the backend logic for file uploading, audio processing, and transcribing.
- **index.html**: The HTML form where users can upload their audio files.
- **result.html**: The HTML page that displays the transcribed text.

## Usage

1. Run the Flask App:

   ```bash
   python app.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

3. Upload an audio file (MP3 or WAV) using the provided form.

4. After the file is processed, the transcribed text will be displayed on a new page.

## Model

The transcription is performed using the `facebook/wav2vec2-large-xlsr-53` model from Hugging Face. This model is pre-trained for automatic speech recognition (ASR) and is capable of transcribing spoken language into text with high accuracy.

## Acknowledgements

- Hugging Face for providing the pre-trained ASR model.
- Flask for creating the web application.
- PyTorch for deep learning framework used by Hugging Face models.
- Soundfile for handling audio file processing.
