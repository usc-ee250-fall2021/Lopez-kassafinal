import paho.mqtt.client as mqtt
import time

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("nathan/green")

def on_message(client, userdata, msg):
  if msg.payload.decode() == "green LED on":
    print("green LED on!")
    client.disconnect()
    
client = mqtt.Client()
client.connect("eclipse.usc.edu",port=1883,keepalive=60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()

while True:
    time.sleep(1)