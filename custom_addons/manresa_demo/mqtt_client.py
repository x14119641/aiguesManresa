import paho.mqtt.client as mqtt
import threading
import logging


_logger = logging.getLogger(__name__)

latest_value = {"message": None}


def on_connect(client, userdata, flags, rc):
    _logger.info(f"Connected to MQTT broker wit result code {str(rc)}")
    client.subscribe("/counter")


def on_message(client, userdata, msg):
    message = msg.payload.decode()
    _logger.info(f"MQTT Message received: {message}")
    latest_value["message"] = message


def start_mqtt_client():
    def run():
        try:
            client = mqtt.Client(protocol=mqtt.MQTTv311)
            client.on_connect = on_connect
            client.on_message = on_message
            
            client.connect("10.8.21.61", 1883, 60)
            client.loop_forever()
        except Exception as e:
            _logger.exception("Error in MQTT thread")

    thread = threading.Thread(target=run, daemon=True)
    thread.start()
    _logger.info("MQTT client thread started")
