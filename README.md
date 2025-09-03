# Voice-Enabled Chatbot with Ollama

A simple, voice-enabled Python chatbot powered by the Ollama AI model (`llama3.2`). The bot listens to your voice, responds with text-to-speech, and maintains conversation context.

## Features

- **Voice Input**: Speak your questions to the chatbot.
- **Text-to-Speech Output**: Hear the AI’s responses spoken aloud.
- **Interactive Chat**: Engages in a continuous conversation.
- **Context-Aware**: Remembers previous parts of the conversation.
- **Automatic Cleanup**: Stops the Ollama model when you exit.

## Requirements

- Python 3.12+
- [Ollama](https://ollama.com/) installed and running
- `ollama` Python package
- `SpeechRecognition` package
- `pyttsx3` package
- `PyAudio` (for microphone access)

## Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/KSD-333/chatbot-ollama.git
   cd chatbot-ollama
   ```

2. **Install dependencies:**
   ```sh
   pip install ollama SpeechRecognition pyttsx3 PyAudio
   ```

3. **Ensure Ollama is running and the model is available:**
   ```sh
   ollama run llama3.2
   ```

## Usage

Run the chatbot from your terminal:
```sh
python chatbot.py
```

### How to Interact

1. The bot will say, "🎤 Listening..."
2. Speak your question into the microphone.
3. The bot will print your question, then speak its response.
4. To exit, say "exit," "quit," or "stop."

### Example Conversation

```
Calibrating for ambient noise...
🎤 Listening...
🧑 You: What is your name?
🤖 My name is Chatbot. How can I help you today?
🎤 Listening...
🧑 You: exit
👋 Goodbye!
Ollama model stopped.
```

## How It Works

- **Speech Recognition**: Uses the `SpeechRecognition` library to capture and transcribe your voice.
- **AI Chat**: Sends the transcribed text to the Ollama model for a response.
- **Text-to-Speech**: Uses `pyttsx3` to convert the AI’s text response into speech.
- **Automatic Cleanup**: Runs `ollama stop llama3.2` to free up resources when the chat ends.

## Customization

- **Change the AI's Persona**: Modify the system prompt in `chatbot.py` to change the bot’s personality or instructions.
- **Use a Different Model**: Switch to another Ollama model by changing the model name in the code.

## Contributing

Feel free to fork the repo and submit pull requests for improvements or new features!


