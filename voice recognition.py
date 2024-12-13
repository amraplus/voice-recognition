import speech_recognition as sr
import pyttsx3
import time

# Initialize the recognizer 
r = sr.Recognizer()
engine = pyttsx3.init()

engine.setProperty('rate', 134)

print("/////////////////////////////////////////////////////////////")
print("\t\tHello I am APlus engine.")
print("/////////////////////////////////////////////////////////////")

engine.say("Hello I am APlus engine")

engine.runAndWait()

while True:    
    try:
        # Use the microphone as source for input
        with sr.Microphone() as source:

            print("\nPlease say something...  ",end = '')

            engine.say("Please say somethin")

            engine.runAndWait()
            
            # Adjust the recognizer to surrounding noise
            r.adjust_for_ambient_noise(source)
            
            # Listen to the audio input
            audio = r.listen(source)
            
            # Recognize the text using Google Web Speech API
            MyText = r.recognize_google(audio)

            MyText = MyText.lower()

            if MyText in ["exit","end","stop","finally",'finish']:
                break

            print(f" {MyText}")

            engine.say(MyText)

            engine.runAndWait()


    except sr.UnknownValueError:
        print("Sorry, I did not understand that. Please try again.")

    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Add a small delay before restarting
            time.sleep(1)
print("\n\nfinally, thanks everyone.")

engine.say("finally thanks everyone")

engine.runAndWait()

print("\nThank you Dr\ Hany Salem.\n\n")

engine.say("Thank you Dr Hany Salem")

engine.runAndWait()
