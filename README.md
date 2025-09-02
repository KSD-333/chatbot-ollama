# Chatbot Using Ollama

A simple Python command-line chatbot powered by the Ollama AI model (`llama3.2`). The bot maintains conversation context and provides detailed, user-friendly answers.

## Features

- Interactive chat with AI using Ollama
- Remembers conversation context
- Automatically stops the Ollama model when you exit
- Easy to run and extend

## Requirements

- Python 3.12+
- [Ollama](https://ollama.com/) installed and running
- `ollama` Python package
- Git (for version control)
- llama3.2 from ollama (or you can use any other you want)

## Ollama setup

**Install Ollama [Ollama](https://ollama.com/)**
-  In command prompt paste
 ```sh 
 ollama pull llama3.2 
 ollama list
 ```


## Setup

1. **Clone the repository:**
	```sh
	git clone https://github.com/KSD-333/chatbot-ollama.git
	cd chatbot-ollama
	```

2. **Install dependencies:**
	```sh
	pip install ollama
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

### Example Conversation

```
🧑 You: What is your name?
🤖 My name is Assistant. I'm here to help answer any questions or provide information on a wide range of topics, so feel free to ask me anything!
🧑 You: exit
👋 Goodbye!
Ollama model stopped.
```

- Type your questions and get answers.
- Type `exit` or `quit` to end the chat and automatically stop the Ollama model.

## How It Works

- The chatbot uses the `ollama` Python package to interact with the AI model.
- Conversation history is maintained for context.
- When you exit, the script runs `ollama stop llama3.2` to free resources.

## Customization

- Change the system prompt in `chatbot.py` to modify the bot’s persona or instructions.
- Switch to a different Ollama model by editing the model name in the code.

## Contributing

Feel free to fork the repo and submit pull requests for improvements or new features!


