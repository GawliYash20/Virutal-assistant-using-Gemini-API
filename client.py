import pyttsx3
import google.generativeai as genai


engine = pyttsx3.init()
engine.setProperty("rate", 180)

# model config
API_KEY = "API_KEY"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


response = model.generate_content(
    "Explain how AI works dont use ** in you response. Response in only text and add new line as required",
    stream=True,
)

text = ""
for chunk in response:
    text += chunk.text

# Accumulate the streaming resonse into a complete text


# speak the response
engine.say(text)
engine.runAndWait()
engine.stop()