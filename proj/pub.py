import speech_recognition as sr
import paho.mqtt.client as mqtt

# code needed for voice to text converter 
# signal or data processing 
# Data collection
rec = sr.Recognizer()
mic = sr.Microphone()
def get_speech():
    try:
        print("Silence please!!!!")
        with mic as source: rec.adjust_for_ambient_noise(source)
        while True:
            print("Speak!!!")
            with mic as source: audio = rec.listen(source)
            print("Got it! You said ...")
            try:
                # recognize speech using Google Speech Recognition
                value = rec.recognize_google(audio)
                # we need some special handling here to correctly print unicode characters to standard output
                print("{}".format(value))
                # publish 
                client.publish("NaG/led", value)
                client.publish("NaG/lcd", value)
            # error check 
            except sr.UnknownValueError:
                print("Oops! Say that again")
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    # publish 
    # Node-to-node communication
    client = mqtt.Client()
    client.connect("eclipse.usc.edu",port=1883,keepalive=60)
    get_speech()
    client.disconnect()


