import paho.mqtt.client as paho
import time

def on_publish(client, userdata, mid):
    print("mid: "+str(userdata))

client = paho.Client()                                                            
client.on_publish = on_publish
client.connect("10.155.0.214", 1883)
client.loop_start()

while True:
    for i in range(1,6):
        for t in range(15):
            (rc, mid) = client.publish("feeds/color1", "00ff00", qos=1)
            (rc, mid) = client.publish("feeds/color2", "00ff00", qos=1)
            (rc, mid) = client.publish("feeds/effect", str(i), qos=1)
            print(i)
            time.sleep(3)

