import requests
import json

class Api:

    def __init__(self):
        self.url = 'http://localhost:8083/'
        self.headers = {'content-type': 'application/json'}

    def post(self,data):
        response = requests.post( self.url, data = json.dumps(data),  headers=self.headers)

    def get(self,data):
        response = requests.get(self.url, data = json.dumps(data), headers = self.headers)
        return response.text

    def postSold(self,data):
        response = requests.post( self.url+"sold", data = json.dumps(data),  headers=self.headers)

    def getSold(self,data):
        response = requests.get(self.url+"sold", data = json.dumps(data), headers = self.headers)
        return response.text