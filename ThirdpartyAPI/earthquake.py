import requests
import Config.config as config


def earthquake():
    response = requests.get(config.earthquake_endpoint)
    earthquakeinfo = response.json()
    return earthquakeinfo
