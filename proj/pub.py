import speech_recognition as sr
import paho.mqtt.client as mqtt

# code needed for voice to text converter 
r = sr.Recognizer()
m = sr.Microphone()
def get_speech():
    try:
        print("A moment of silence, please...")
        with m as source: r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
        while True:
            print("Say something!")
            with m as source: audio = r.listen(source)
            print("Got it! Now to recognize it...")
            try:
                # recognize speech using Google Speech Recognition
                value = r.recognize_google(audio)
                # we need some special handling here to correctly print unicode characters to standard output
                print("{}".format(value))
                client.publish("NaG/led", value)
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    # publish 
    client = mqtt.Client()
    client.connect("eclipse.usc.edu",port=1883,keepalive=60)
    get_speech()
    client.disconnect()


