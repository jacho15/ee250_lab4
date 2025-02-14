import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected to broker with result code " + str(rc))
    client.subscribe(f"jacho/pong")

def on_message(client, userdata, msg):
    number = int(msg.payload.decode()) + 1
    print(f"Received: {msg.payload.decode()} → Sending: {number}")
    time.sleep(1)  # Delay to avoid flooding
    client.publish(f"jacho/ping", str(number))

if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("test.mosquitto.org", 1883, 60)
    client.loop_start()

    time.sleep(2)

    print(f"Starting chain with: {1}")
    client.publish(f"jacho/ping", str(1))

    client.loop_forever()
