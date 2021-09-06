import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker)

while True:
    randNumber = randrange(10)
    client.publish("Temperature",randNumber)
    print("Just published" + str(randNumber) + "to Topic TEMPERATURE")
    time.sleep(1)