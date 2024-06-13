import os
import json
import pyaudio
from vosk import Model, KaldiRecognizer

MODEL_PATH = r"INPUT YOUR LOCATION TO YOUR VOSK MODEL."

def get_transcription():
    # Check if the model path exists
    if not os.path.exists(MODEL_PATH):
        print(f"Model path {MODEL_PATH} does not exist. Please download and extract the model.")
        exit(1)

    # Load the model
    model = Model(MODEL_PATH)

    # Create a recognizer with the model
    recognizer = KaldiRecognizer(model, 16000)

    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Open a stream with the required parameters
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    print("Listening...")

    prompt = []

    try:
        while True:
            data = stream.read(4096, exception_on_overflow=False)
            
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                text = json.loads(result).get('text', '')
                print(f"Recognized: {text}")
                prompt.append(text)
                if prompt[-1] == "":
                    break

    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        stream.stop_stream()
        stream.close()
        audio.terminate()

    # Join the prompt list into a single string
    prompt_string = ' '.join(prompt)
    
    # Save the prompt to a file
    with open('prompt.txt', 'w') as f:
        f.write(prompt_string)

    return prompt_string

if __name__ == "__main__":
    get_transcription()
