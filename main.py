import speech_recognition as sr
import webbrowser
import pyttsx3
import google.generativeai as genai

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.setProperty("rate", 180)
    engine.say(text)
    engine.runAndWait()

# Function to process commands using Generative AI
def aiProcess(command):
    API_KEY = "API_KEY"  # Replace with your API key

    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"{command}. Don't use ** in your response. Response in only text and add new lines as required.")
        return response.text

    except Exception as e:
        return f"An error occurred while processing AI response: {e}"

# Function to process user commands
def processCommand(c):
    if "open google" in c.lower():
        speak("Opening Google.")
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        speak("Opening Facebook.")
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        speak("Opening YouTube.")
        webbrowser.open("https://youtube.com")
    else:
        output = aiProcess(c)
        speak(output)

# Main loop to listen for commands
if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for the wake word 'Jarvis'...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

            # Recognize the wake word
            command = recognizer.recognize_google(audio).lower()
            if command == "jarvis":
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Jarvis is listening for your command...")
                    audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
                command = recognizer.recognize_google(audio)
                processCommand(command)

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand. Please try again.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"Error: {e}")
