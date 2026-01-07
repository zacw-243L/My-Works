import http.client
import json
import time
import threading

# Maximum allowed characters for user input and ChatGPT response
MAX_CHARACTERS = 400

# Function to send a message to ChatGPT and get a response
def send_message_to_gpt(message):
    conn = http.client.HTTPSConnection("chatgpt-42.p.rapidapi.com")

    # Create payload with user input
    payload = json.dumps({
        "messages": [
            {"role": "user", "content": message}
        ],
        "system_prompt": "",
        "temperature": 0.9,
        "top_k": 5,
        "top_p": 0.9,
        "max_tokens": 256,
        "web_access": False
    })

    headers = {
        'x-rapidapi-key': "",
        'x-rapidapi-host': "chatgpt-42.p.rapidapi.com",
        'Content-Type': "application/json"
    }

    # Send request to ChatGPT
    conn.request("POST", "/conversationgpt4-2", payload, headers)

    # Get response from ChatGPT
    res = conn.getresponse()
    data = res.read()

    # Parse the response JSON
    response_json = json.loads(data.decode("utf-8"))

    # Extract and return the result, truncated to MAX_CHARACTERS if needed
    if response_json.get("status"):
        return response_json["result"][:MAX_CHARACTERS]
    else:
        return "Error: Unable to get a valid response from ChatGPT."


# Function to display a loading indicator
def display_loading_indicator():
    while not stop_loading_indicator:
        for char in "|/-\\":
            print(f"\rChatGPT is thinking {char}", end="")
            time.sleep(0.1)


# Function to start the conversation
def chat_with_gpt():
    print("ChatGPT: Hello! How can I assist you today? If there's a specific task or question, feel free to ask. Otherwise, let me know if you need any general information on anything at all.")

    while True:
        # Capture user input
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("ChatGPT: Goodbye!")
            break

        # Truncate user input to MAX_CHARACTERS if needed
        if len(user_input) > MAX_CHARACTERS:
            user_input = user_input[:MAX_CHARACTERS]
            print(f"You (truncated to {MAX_CHARACTERS} characters): {user_input}")

        global stop_loading_indicator
        stop_loading_indicator = False

        # Start loading indicator in a separate thread
        loading_thread = threading.Thread(target=display_loading_indicator)
        loading_thread.start()

        try:
            # Send user input to ChatGPT and get the response
            gpt_response = send_message_to_gpt(user_input)
        except Exception as e:
            gpt_response = f"Error: {str(e)}"

        # Stop loading indicator
        stop_loading_indicator = True
        loading_thread.join()

        # Print ChatGPT's response
        print(f"\rChatGPT: {gpt_response}")

# Run the chat function
if __name__ == "__main__":
    stop_loading_indicator = False
    chat_with_gpt()
