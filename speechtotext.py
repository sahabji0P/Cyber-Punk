import speech_recognition as sr

def speech_to_text(file_name):
    recognizer = sr.Recognizer()
<<<<<<< Updated upstream
    recognizer.energy_threshold = 300  # set the energy threshold to a lower value
    recognizer.dynamic_energy_threshold = True
    recognizer.dynamic_energy_adjustment_damping = 0.15
    recognizer.dynamic_energy_adjustment_ratio = 1.5
=======
<<<<<<< Updated upstream

=======
    recognizer.energy_threshold = 300  # set the energy threshold to a lower value
    recognizer.dynamic_energy_threshold = True  # automatically adjust the energy threshold using audio from the first second of the recording
    recognizer.dynamic_energy_adjustment_damping = 0.15 # how slowly to increase the threshold
    recognizer.dynamic_energy_adjustment_ratio = 1.5 # how much to increase the threshold by
>>>>>>> Stashed changes
>>>>>>> Stashed changes
    
    with sr.Microphone() as source:
        print("Speak something...")
        audio = recognizer.listen(source)

        try:
            print()
            text = recognizer.recognize_google(audio)  
            print("Speech recognized: ", text)
            with open(file_name, 'w') as file:
                file.write(text)
            print()
            print("Speech saved to", file_name)

        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
        except sr.RequestError as e:
            print("Error: {0}".format(e))

if __name__ == "__main__":
    file_name = "speech.txt"
    speech_to_text(file_name)
