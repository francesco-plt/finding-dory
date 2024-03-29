import paho.mqtt.client as mqtt
from json import dumps, dump, load
from uuid import uuid4
from datetime import datetime as dt
from time import time
import os


host = "131.175.120.117"
port = 1883
Connected = False
client_id = str(uuid4())


def delete_content(pfile):
    pfile.seek(0)
    pfile.truncate()


# function to export a given payload to a JSON file
def json_append(payload):
    with open("data.json", "r+") as f:

        # parsing JSON file
        jsonf = load(f)
        # appending payload
        jsonf["messages"].append(payload)

        # cleaning up JSON file
        # and writing it
        delete_content(f)
        dump(jsonf, f, indent=4)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected  # Use global variable
        Connected = True  # Signal connection
    else:
        print("Connection failed")


# we want to create a dictionary to store message data
def on_message(client, userdata, message):
    msg = {
        "topic": message.topic,
        "payload": message.payload.decode("utf-8"),
        "qos": message.qos,
        "retain": message.retain,
    }
    print("[%s] new message:" % dt.now().strftime("%Y-%m-%d, %H:%M:%S"))
    print(dumps(msg, indent=4))
    print("\n")
    json_append(msg)


def main():

    # if data.json exists, delete it
    if os.path.isfile("data.json"):
        os.remove("data.json")
    # initializing file as a dictionary with an empty list of messages
    with open("data.json", "w") as outfile:
        outfile.write(dumps({"messages": []}, indent=4))

    # setting up the MQTT client
    print("Client ID: ", client_id)
    print("Setting up MQTT client...")
    client = mqtt.Client(client_id)
    client.on_connect = on_connect  # attach function to callback
    client.on_message = on_message

    client.connect(host, port)
    client.subscribe("#")

    start = time()
    listen_interval = 60 * 60  # 1 hour
    while True:
        print("[%s] Still running..." % dt.now().strftime("%Y-%m-%d, %H:%M:%S"))
        client.loop()
        current = time()
        if (current - start) > listen_interval:
            print("Time limit reached. Exiting...")
            break


if __name__ == "__main__":
    main()
