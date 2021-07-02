import requests
import json

def getFrame():
    return requests.get("127.0.0.1/Stream")

def getCoords():
    return json.loads(requests.get("127.0.0.1/Stream"))