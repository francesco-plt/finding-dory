import asyncio, os
from urllib import response
from aiocoap import *
from json import dumps, dump
from rich import print_json
import colored_traceback

colored_traceback.add_hook()

host = "131.175.120.117"
payload = b""
methods = [GET, POST, PUT, DELETE]

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

    responses = []
    for r in resources:
        reqs = []
        for m in methods:
            reqs.append(Message(code=m, payload=payload, uri=f"coap://{host}{r}"))

        for req in reqs:
            res = await context.request(req).response
            if res.code.is_successful():
                responses.append(
                    {
                        "code": str(res.code),
                        "mid": str(res.mid),
                        "token": str(res.token),
                        "payload": res.payload.decode("utf-8"),
                    }
                )

    resp_json = {"responses": responses}
    with open("data.json", "r+") as f:
        print("Writing to file...")
        dump(resp_json, f, indent=4)
        print("Done. Wrote %d responses" % len(responses))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
