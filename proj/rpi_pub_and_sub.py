"""EE 250L Lab 04 Starter Code

Run rpi_pub_and_sub.py on your Raspberry Pi."""

import paho.mqtt.client as mqtt
import time
from grovepi import *
from grove_rgb_lcd import *
import sys
# port of led 
ledg = 2 
ledb = 3
ledr = 4

# initialization 
set_bus("RPI_1")
pinMode(ledg,"OUTPUT")
pinMode(ledb,"OUTPUT")
pinMode(ledr,"OUTPUT")
#pinMode(button,"INPUT")
sys.path.append('../../Software/Python/')


def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
def on_press(key):
    try: 
        k = key.char # single-char keys
    except: 
        k = key.name # other keys
    
    if k == 'w':
        print("w")
        #send "w" character to rpi
        client.publish("natan/lcd", "w")
    elif k == 'a':
        print("a")
        # send "a" character to rpi
        client.publish("natan/lcd", "a")
        # print LED_OFF
        print("LED_ON")
        # send "LED_ON" 
        client.publish("natan/led", "LED_ON")
    elif k == 's':
        print("s")
        # send "s" character to rpi
        client.publish("natan/lcd", "s")
    elif k == 'd':
        print("d")
        # send "d" character to rpi
        client.publish("natan/lcd", "d")
        # print LED_OFF
        print("LED_OFF")
        # send "LED_OFF"
        client.publish("natan/led", "LED_OFF")
# led callback 
def on_ledg(client, userdata, msg):
    #on 
    if str(msg.payload, "utf-8") == "green LED on":
        digitalWrite(ledg,1)		# Send HIGH to switch on LED
    #off
    elif str(msg.payload, "utf-8") == "green LED off":
        digitalWrite(ledg,0)

def on_ledb(client, userdata, msg):
    #on 
    if str(msg.payload, "utf-8") == "blue LED on":
        digitalWrite(ledb,1)		# Send HIGH to switch on LED
    #off
    elif str(msg.payload, "utf-8") == "blue LED off":
        digitalWrite(ledb,0)

def on_ledr(client, userdata, msg):
    #on 
    if str(msg.payload, "utf-8") == "red LED on":
        digitalWrite(ledr,1)		# Send HIGH to switch on LED
    #off
    elif str(msg.payload, "utf-8") == "red LED off":
        digitalWrite(ledr,0)

if __name__ == '__main__':
    
    lis = keyboard.Listener(on_press=on_press)
    lis.start() # start to listen on a separate thread
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    
    if __name__ == '__main__':
    #setup the keyboard event listener
    lis = keyboard.Listener(on_press=on_press)
    lis.start() # start to listen on a separate thread
while True:
    time.sleep(1)


