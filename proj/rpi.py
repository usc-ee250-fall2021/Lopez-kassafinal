"""EE 250L Lab 04 Starter Code

Run rpi_pub_and_sub.py on your Raspberry Pi."""

import paho.mqtt.client as mqtt
if __name__ == '__main__':

    client = mqtt.Client()
    client.connect("localhost",1883,60)
    client.publish("topic/test", "Hello world!")
    client.disconnect()


