import speech_recognition as sr
import time

#source: https://github.com/Uberi/speech_recognition/blob/master/examples/background_listening.py

# this is called from the background thread
def callback(recognizer, audio):
    #received audio data, now we'll recognize it using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print(recognizer.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

class speech_recognizer:

    stop_listening=None

    def __init__(self):
        r = sr.Recognizer()
        m = sr.Microphone()
        with m as source:
            r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening

        # start listening in the background (note that we don't have to do this inside a `with` statement)
        self.stop_listening = r.listen_in_background(m, callback)
        # `stop_listening` is now a function that, when called, stops background listening

        while(True):
            time.sleep(10)

    
    def stop(self):
        self.stop_listening()