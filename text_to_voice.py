import pyttsx3

def text_to_speech():
    # Read the response from the file
    with open('response.txt', 'r') as f:
        response = f.read()

    # Initialize the TTS engine with the Microsoft TTS engine
    engine = pyttsx3.init(driverName='sapi5')

    # Set properties before speaking
    engine.setProperty('rate', 150)  # Speed percent (can go over 100)
    engine.setProperty('volume', 0.9)  # Volume 0-1
    
    # Specify the voice ID for the desired JARVIS-like voice
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    engine.setProperty('voice', voice_id)

    # Speak the text
    engine.say(response)
    engine.runAndWait()

if __name__ == "__main__":
    text_to_speech()
