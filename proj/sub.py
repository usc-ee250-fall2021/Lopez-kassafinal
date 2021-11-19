import paho.mqtt.client as mqtt
import time
from grovepi import *
import sys
ledg = 2 
ledb = 3
ledr = 4
# This is the Subscriber
pinMode(ledg,"OUTPUT")
pinMode(ledb,"OUTPUT")
pinMode(ledr,"OUTPUT")

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("NaG/led")
  client.message_callback_add("NaG/led", on_colormessage)

def on_message(client, userdata, msg):
  print("on_message: " + msg.topic + " ")

def on_colormessage(client, userdata, msg):
  print('hi', msg.payload.decode())
  if msg.payload.decode() == "green LED on":
    print("green")
    digitalWrite(ledg , 1)
  elif msg.payload.decode() == "green LED off":
    print("green off")
    digitalWrite(ledg , 0)
  elif msg.payload.decode() == "red LED on":
    print("red")
    digitalWrite(ledr , 1)
  elif msg.payload.decode() == "red LED off":
    print("red off")
    digitalWrite(ledr , 0)
  elif msg.payload.decode() == "blue LED on":
    print("blue")
    digitalWrite(ledb , 1)
  elif msg.payload.decode() == "blue LED off":
    print("blue off")
    digitalWrite(ledb , 0)

if __name__ == '__main__':  
  client = mqtt.Client()
  client.on_connect = on_connect
  client.on_message = on_message
  client.connect("eclipse.usc.edu",port=1883,keepalive=60)


  client.loop_start()
  while True:
    time.sleep(1)