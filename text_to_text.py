import cohere
co = cohere.Client('ENTER YOUR API KEY HERE!')

def chat_with_cohere(prompt):
    response = co.generate(
        model='command-r-plus',  # You can select different model sizes
        prompt=prompt,
        max_tokens=250,
        temperature=0.7
    )
    return response.generations[0].text.strip()

def main():
    # Read the prompt from the file
    with open('prompt.txt', 'r') as f:
        prompt_string = f.read()
    
    # Process the text as needed
    print(f"Processing text: {prompt_string}")
    
    # Example processing (You can replace this with your actual processing logic)
    processed_text = prompt_string.upper()  # Convert to uppercase as an example
    
    # Save the processed text to a file to be used by text-to-voice.py
    with open('processed_text.txt', 'w') as f:
        f.write(processed_text)

    prompt = "You are JARVIS (Just a Rather Very Intelligent System), a highly advanced AI assistant designed to assist users in a wide range of tasks. You possess extensive knowledge in various domains, including science, technology, mathematics, and more. Your responses should be intelligent, insightful, and helpful, yet kind of witty and funny. You are expected to interact in a professional yet approachable manner, providing accurate and concise answers to queries. Engage in meaningful conversations, and strive to understand and assist the user to the best of your abilities. "

    user_input = prompt + processed_text

    response = chat_with_cohere(user_input)
    print(response)

    with open('response.txt', 'w') as f:
        f.write(response)



if __name__ == "__main__":
    main()
