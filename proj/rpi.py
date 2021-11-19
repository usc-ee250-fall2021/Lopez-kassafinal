"""EE 250L Lab 04 Starter Code

Run rpi_pub_and_sub.py on your Raspberry Pi."""

import paho.mqtt.client as mqtt
if __name__ == '__main__':

    client = mqtt.Client()
    client.connect("eclipse.usc.edu",port=1883,keepalive=60)
    client.publish("nathan/green", "green LED on!")
    client.disconnect()


