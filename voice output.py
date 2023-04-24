import pyttsx3

def speak(audio):
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 190)
    engine.say(audio)
    engine.runAndWait()

if __name__ == '__main__':

    speak(raw_input('Enter the data to speak: '))
