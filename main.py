import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizipip ng...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        print(f"Request error from Google Speech Recognition service; {e}")
        return ""

def process_query(query):
    if "hello" in query:
        print("Hello! How can I assist you?")
    elif "goodbye" in query:
        print("Goodbye! Have a great day!")
        exit()
    else:
        print("Sorry, I'm not sure how to help with that.")

if _name_ == "_main_":
    while True:
        query = listen()
        if query:
            process_query(query)