import ollama               
import subprocess

def chat_with_ai(messages, model="llama3.2"):
    response = ollama.chat(model=model, messages=messages)
    return response["message"]["content"]

message = [{"role":"system", "content": "Your Name is Assistant and you provide all thing related to user input with full explanation."}]

while True:
   user_input = input("🧑 You: ")
   if user_input.lower() in ["exit", "quit"]:
       print("👋 Goodbye!")
       # Stop the Ollama model automatically
       try:
           subprocess.run(["ollama", "stop", "llama3.2"], check=True)
           print("Ollama model stopped.")
       except Exception as e:
           print(f"Failed to stop Ollama model: {e}")
       break
   message.append({"role": "user", "content": user_input})
   response = chat_with_ai(message)
   print("🤖", response)
