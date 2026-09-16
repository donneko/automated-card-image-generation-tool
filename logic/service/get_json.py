import json

def getConfig():
    with open("config.json", encoding="utf-8") as f:
        return json.load(f)

def getInputData(fileName):
    with open(fileName, encoding="utf-8") as f:
        return json.load(f)
