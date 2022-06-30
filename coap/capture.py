import asyncio
import random
from aiocoap import *

host = "131.175.120.117"
payload = b""
methods = ["GET", "POST", "PUT", "DELETE"]

# we want to read a resource for each
# line of the resources.txt file
def get_resources():
    with open("resources.txt", "r") as f:
        resources = f.readlines()
    return resources


async def main():

    # if data.json exists, delete it
    if os.path.isfile("data.json"):
        os.remove("data.json")
    # initializing file as a dictionary with an empty list of messages
    with open("data.json", "w") as outfile:
        outfile.write(dumps({"messages": []}, indent=4))

    # creating a client
    context = await Context.create_client_context()

    res = get_resources()

    for r in res:
        if "Get" in r:
            request = Message(code=GET, payload=payload, uri=f"coap://{host}{r}")
        elif "Post" in r:
            request = Message(code=POST, payload=payload, uri=f"coap://{host}{r}")
        elif "Put" in r:
            request = Message(code=PUT, payload=payload, uri=f"coap://{host}{r}")
        elif "Delete" in r:
            request = Message(code=DELETE, payload=payload, uri=f"coap://{host}{r}")
        else:
            continue

        resp = await context.request(request).response
        print("Result: %s\n%r" % (resp.code, resp.payload))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
