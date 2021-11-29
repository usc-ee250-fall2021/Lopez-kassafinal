import paho.mqtt.client as mqtt
import time
from grovepi import *
from grove_rgb_lcd import *
import sys
ledg = 7 
ledb = 3
ledr = 4
# This is the Subscriber
pinMode(ledg,"OUTPUT")
pinMode(ledb,"OUTPUT")
pinMode(ledr,"OUTPUT")

sys.path.append('../Software/Python/')
sys.path.append('../Software/Python/grove_rgb_lcd')


# subscribe 
# Node-to-node communication
def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("NaG/led")
  client.subscribe("NaG/lcd")
  client.message_callback_add("NaG/led", on_colormessage)
  client.message_callback_add("NaG/lcd", on_lcd)

def on_message(client, userdata, msg):
  print("on_message: " + msg.topic + " ")

# Visualization and/or control (simple web front end) element 


def on_lcd(client, userdata, msg):
  if msg.payload.decode() == "UCLA":
    setText_norefresh("UCLA < USC")	

def on_colormessage(client, userdata, msg):
  # turn green led on
  if msg.payload.decode() == "green LED on":
    digitalWrite(ledg , 1)
  # turn green led off
  elif msg.payload.decode() == "green LED off":
    digitalWrite(ledg , 0)
  # turn red led on
  elif msg.payload.decode() == "red LED on":
    digitalWrite(ledr , 1)
  # turn red led off
  elif msg.payload.decode() == "red LED off":
    digitalWrite(ledr , 0)
  # turn blue led on
  elif msg.payload.decode() == "blue LED on":
    digitalWrite(ledb , 1)
  # turn blue led off
  elif msg.payload.decode() == "blue LED off":
    digitalWrite(ledb , 0)
  # turn on party mode 
  elif msg.payload.decode() == "party mode":
    for i in range (0,10):
      digitalWrite(ledg , 1)
      time.sleep(.5)
      digitalWrite(ledr , 1)
      time.sleep(.5)
      digitalWrite(ledg , 0)
      time.sleep(.5)
      digitalWrite(ledb , 1)
      time.sleep(.5)
      digitalWrite(ledb , 0)
      time.sleep(.5)
      digitalWrite(ledr , 0)
  # turn all leds on
  elif msg.payload.decode() == "all on":
    digitalWrite(ledg , 1)
    digitalWrite(ledr , 1)
    digitalWrite(ledb , 1)
  # turn all leds off
  elif msg.payload.decode() == "all off":
    digitalWrite(ledg , 0)
    digitalWrite(ledr , 0)
    digitalWrite(ledb , 0)
  # usc mode 
  elif msg.payload.decode() == "USC":
    # u
    digitalWrite(ledg , 1)
    time.sleep(.5)
    digitalWrite(ledg , 0)
    time.sleep(.5)
    digitalWrite(ledg , 1)
    time.sleep(.5)
    digitalWrite(ledg , 0)
    time.sleep(.5)
    digitalWrite(ledg , 1)
    time.sleep(1.5)
    digitalWrite(ledg , 0)
    time.sleep(.5)
    # s
    digitalWrite(ledr , 1)
    time.sleep(.5)
    digitalWrite(ledr , 0)
    time.sleep(.5)
    digitalWrite(ledr , 1)
    time.sleep(.5)
    digitalWrite(ledr , 0)
    time.sleep(.5)
    digitalWrite(ledr , 1)
    time.sleep(.5)
    digitalWrite(ledr , 0)
    time.sleep(.5)
    # c
    digitalWrite(ledb , 1)
    time.sleep(1.5)
    digitalWrite(ledb , 0)
    time.sleep(.5)
    digitalWrite(ledb , 1)
    time.sleep(.5)
    digitalWrite(ledb , 0)
    time.sleep(.5)
    digitalWrite(ledb , 1)
    time.sleep(1.5)
    digitalWrite(ledb , 0)
    time.sleep(.5)
    digitalWrite(ledb , 1)
    time.sleep(.5)
    digitalWrite(ledb, 0)
    time.sleep(.5)
  elif msg.payload.decode() == "electrical engineering 250":
    # e
    digitalWrite(ledg , 1)
    time.sleep(.5)
    digitalWrite(ledg , 0)
    time.sleep(.5)

   # e
    digitalWrite(ledr , 1)
    time.sleep(.5)
    digitalWrite(ledr , 0)
    time.sleep(.5)

    # 2
    digitalWrite(ledb , 1)
    time.sleep(.5)
    digitalWrite(ledb , 0)
    time.sleep(.5)
    digitalWrite(ledb , 1)
    time.sleep(.5)
    digitalWrite(ledb , 0)
    time.sleep(.5)
    digitalWrite(ledb , 1)
    time.sleep(1.5)
    digitalWrite(ledb , 0)
    time.sleep(.5)
    digitalWrite(ledb , 1)
    time.sleep(1.5)
    digitalWrite(ledb , 0)
    time.sleep(.5)
    digitalWrite(ledb , 1)
    time.sleep(1.5)
    digitalWrite(ledb , 0)
    time.sleep(.5)

    # 5
    digitalWrite(ledb , 1)
    time.sleep(.5)
    digitalWrite(ledb , 0)
    time.sleep(.5)
    digitalWrite(ledb , 1)
    time.sleep(.5)
    digitalWrite(ledb , 0)
    time.sleep(.5)
    digitalWrite(ledb , 1)
    time.sleep(.5)
    digitalWrite(ledb , 0)
    time.sleep(.5)
    digitalWrite(ledb , 1)
    time.sleep(.5)
    digitalWrite(ledb , 0)
    time.sleep(.5)
    digitalWrite(ledb , 1)
    time.sleep(.5)
    digitalWrite(ledb , 0)
    time.sleep(.5)

    # 0
    digitalWrite(ledb , 1)
    time.sleep(1.5)
    digitalWrite(ledb , 0)
    time.sleep(.5)
    digitalWrite(ledb , 1)
    time.sleep(1.5)
    digitalWrite(ledb , 0)
    time.sleep(.5)
    digitalWrite(ledb , 1)
    time.sleep(1.5)
    digitalWrite(ledb , 0)
    time.sleep(.5)
    digitalWrite(ledb , 1)
    time.sleep(1.5)
    digitalWrite(ledb , 0)
    time.sleep(.5)
    digitalWrite(ledb , 1)
    time.sleep(1.5)
    digitalWrite(ledb , 0)
    time.sleep(.5)

if __name__ == '__main__':  
  # subscribe
  client = mqtt.Client()
  client.on_connect = on_connect
  client.on_message = on_message
  client.connect("eclipse.usc.edu",port=1883,keepalive=60)


  client.loop_start()
  while True:
    time.sleep(1)



