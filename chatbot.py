import ollama               
import subprocess
import speech_recognition as sr
import pyttsx3


speech = sr.Recognizer()

def listen_to_user():
    with sr.Microphone() as source:
        print("Calibrating for ambient noise...")
        speech.adjust_for_ambient_noise(source, duration=1)
        print("🎤 Listening...")
        try:
            audio = speech.listen(source)
            user_input = speech.recognize_google(audio)
            print(f"🧑 You: {user_input}")
            return user_input
        except sr.UnknownValueError:
            print("🤖 Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("🤖 Sorry, my speech service is down.")
            return None
           

def text_to_speech(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()


def chat_with_ai(messages, model="llama3.2"):
    response = ollama.chat(model=model, messages=messages)
    return response["message"]["content"]

message = [{"role":"system", "content": "Your Name is Chatbot and you have ability to speack and you have to answer user question in short but sweet manner and at last ask him for any futher requirement releted to his topic and do don't provide long answer so user can wait 2 3 minitues.  do not repeat any info repeated and provide detailed and accurate information when user want. The data sholud look like is humand explaning to the other person."}]

while True:
   user_input = listen_to_user()
   
   if user_input:
       if user_input.lower() in ["exit", "quit","stop"]:
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
       text_to_speech(response)
