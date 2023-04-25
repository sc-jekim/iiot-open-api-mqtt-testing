from flask import Flask, jsonify, request
import paho.mqtt.client as mqtt
import time

app = Flask(__name__)

# Set up MQTT client
mqtt_client = mqtt.Client()


# Define MQTT event handlers
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


def on_message(client, userdata, msg):
    print("Received message: {}".format(message.payload.decode("utf-8")))


# Set MQTT event handlers
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

# Connect to MQTT broker
mqtt_client.connect("localhost", 1883, 60)

# Start the MQTT client loop
mqtt_client.loop_forever()


# Define Flask routes
@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'MQTT mockup server is running!'})


@app.route('/publish', methods=['POST'])
def publish():
    topic = request.json['/mqtttest']
    payload = request.json['payload']
    mqtt_client.publish(topic, payload)
    return jsonify({'message': 'Message published successfully!'})


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
