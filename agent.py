import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import random

# Download NLTK data files if you haven't already
nltk.download('punkt')
nltk.download('stopwords')

# Simple Intent Recognition
def get_intent(user_input):
    tokens = word_tokenize(user_input.lower())
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [w for w in tokens if w.isalnum() and w not in stop_words]

    if "weather" in filtered_tokens:
        return "get_weather"
    elif "time" in filtered_tokens:
        return "get_time"
    elif "remind" in filtered_tokens:
        return "set_reminder"
    else:
        return "unknown"

# Simple Task Management
def get_weather():
    return "The weather is sunny with a high of 25°C."

def get_time():
    return f"The current time is {nltk.datetime.now().strftime('%H:%M:%S')}."

def set_reminder(reminder):
    return f"Reminder set for: {reminder}"

# Main Virtual Assistant Function
def virtual_assistant():
    print("Hello! I'm your virtual assistant. How can I help you today?")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Assistant: Goodbye!")
            break

        intent = get_intent(user_input)

        if intent == "get_weather":
            response = get_weather()
        elif intent == "get_time":
            response = get_time()
        elif intent == "set_reminder":
            reminder = user_input.split("remind me to", 1)[1].strip()
            response = set_reminder(reminder)
        else:
            response = "I'm sorry, I didn't understand that."

        print(f"Assistant: {response}")

# Run the virtual assistant
if __name__ == "__main__":
    virtual_assistant()
