from textblob import TextBlob
import emoji
import speech_recognition as sr


def analyze_mood(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.7:
        mood = "overwhelmingly positive"  
    elif polarity > 0.3:
        mood = "positive"
    elif polarity < -0.7:
        mood = "overwhelmingly negative"
    elif polarity < -0.3:
        mood = "negative"
    else:
        mood = "neutral"
    
    return f"Polarity score: {polarity} -> Mood: {mood}"


def listen_linda():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_sphinx(audio)
            
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
        except sr.RequestError as e:
            print(f"Sorry, there was an error from Bing Speech Recognition service; {e}")
        return None

def run_app():
    print("Welcome to the AI-powered Emoji mood classifier!")
    print("say something into the mcirophone, and I will tell you the mood of the text with an emoji.")
    print('say "exit" to quit the app.')

    while True:
        setence = listen_linda()
        if setence is None:
            continue
        if setence.lower() in [exit, "exit", "quit"]:
            print("Goodbye!")
            break
        result = analyze_mood(setence)
        print(result + "\n")

run_app()