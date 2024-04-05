import paho.mqtt.client as mqtt

# Configura los parámetros de conexión MQTT
MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_TOPIC = "led_control"

# Función para manejar los mensajes MQTT
def on_message(client, userdata, message):
    payload = message.payload.decode("utaf-8")
    print("Mensaje recibido:", payload)

# Configura el cliente MQTT
client = mqtt.Client()
client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.subscribe(MQTT_TOPIC)
client.loop_start()

# Bucle principal
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
