import paho.mqtt.client as mqtt
import logging



    # Define the MQTT broker, port, and topic
broker_address = "110.14.175.90"
port = 9884
topic = "location_ngl"

    # Define the MQTT username and password
username = "user01"
password = "user01"

logger = logging.getLogger('mqtt_receiver')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('mqtt_receiver.log')
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

logger.addHandler(fh)

    # Define the on_connect callback function
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))
    client.subscribe(topic)

    # Define the on_message callback function
def on_message(client, userdata, message):
    print("Received message: {}".format(message.payload.decode("utf-8")))
    logger.info("Received message '" + str(message.payload) + "' on topic '" + message.topic + "'")

    # Create an MQTT client instance
client = mqtt.Client()

    # Set the MQTT username and password
client.username_pw_set(username, password)

    # Set the callback functions
client.on_connect = on_connect
client.on_message = on_message

    # Connect to the MQTT broker
client.connect(broker_address, port=port)

    # Start the MQTT client loop
client.loop_forever()
