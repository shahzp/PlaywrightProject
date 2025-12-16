import json
class Jsonread():
    def __init__(self):
        pass

    def readJson(self, path) -> list:
        with open(path) as f:
            data = json.load(f)
            return data['userCredentials']




