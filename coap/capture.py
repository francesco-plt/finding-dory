import asyncio, os
from aiocoap import *
from json import dumps
from IPython import embed

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

    resources = get_resources()

    for res in resources:
        reqs = []
        reqs.append(Message(code=GET, payload=payload, uri=f"coap://{host}{res}"))
        reqs.append(Message(code=POST, payload=payload, uri=f"coap://{host}{res}"))
        reqs.append(Message(code=PUT, payload=payload, uri=f"coap://{host}{res}"))
        reqs.append(Message(code=DELETE, payload=payload, uri=f"coap://{host}{res}"))

        resps = []
        for req in reqs:
            resps.append(await context.request(req).response)
        embed()
        exit()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
