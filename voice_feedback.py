import pyttsx3

def speak(text):
    """Convert text to speech with a slower rate."""
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')  # Get the default speed
    engine.setProperty('rate', rate - 50)  # Slow it down (you can decrease more if needed)
    
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Face the camera properly!")  # Test the function
