import paho.mqtt.client as mqtt
from influxdb_client import InfluxDBClient, Point, WritePrecision
import os

# MQTT Konfig
MQTT_BROKER = os.getenv("MQTT_BROKER", "mqtt-broker:1883")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_TOPIC = os.getenv("MQTT_TOPIC", "#")  # Standard: Alle Topics abonnieren

# InfluxDB Konfig
INFLUX_URL = os.getenv("INFLUX_URL", "influxdb:8086")
INFLUX_TOKEN = "wwd#Dnb37g2k" # os.getenv("INFLUX_TOKEN", "my-secret-token")

# InfluxDB Client erstellen
client = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN)
write_api = client.write_api(write_options=WritePrecision.NS)

def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT Broker with result code {rc}")
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    print(f"Received message: {msg.topic} {msg.payload.decode()}")
    
    point = (
        Point("mqtt_data")
        .tag("topic", msg.topic)
        .field("value", msg.payload.decode())
    )
    
    write_api.write(record=point)

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
mqtt_client.loop_forever()
