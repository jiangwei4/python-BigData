import requests
import json

class Api:

    def __init__(self):
        self.url = 'http://localhost:8083/'

    def post(self,data):
        url = "http://localhost:8083/"
        headers = {'content-type': 'application/json'}
        response = requests.post( url, data = json.dumps(data),  headers=headers)

    def get(self,data):
        requests.get(self.url,params = {})