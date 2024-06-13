import subprocess

def main():
    print("Welcome to the JARVIS system (Just A Rather Very Intelligent System)")
    print("\n" * 2)

    while True:
        try:
            # Run voice-to-text.py
            print("Running voice-to-text.py...")
            subprocess.run(["python", r"voice-to-text.py"])
            
            # Run text-to-text.py
            print("\nRunning text-to-text.py...")
            subprocess.run(["python", r"text_to_text.py"])
            
            # Run text-to-voice.py
            print("\nRunning text-to-voice.py...")
            subprocess.run(["python", r"text_to_voice.py"])
            
            # Optionally, add a condition to break the loop
            # You can check for a specific word in the response to break the loop
            with open('prompt.txt', 'r') as f:
                response = f.read().strip().lower()
                if 'exit' in response:
                    print("Exiting the JARVIS system.")
                    break

        except KeyboardInterrupt:
            print("\nExiting the JARVIS system.")
            break

if __name__ == "__main__":
    main()
