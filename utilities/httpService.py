import json
import requests
import logging

class HttpService:
    def __init__(self, username, password, service_url):
        self.username = username
        self.password = password
        self.service_url = service_url
        logging.getLogger("requests").setLevel(logging.WARNING)

    def get(self, url, params=None):
        return requests.get("%s%s" % (self.service_url, url), auth=(self.username, self.password), params=params)

    def get_and_verify(self, url, response_to_verify, params=None):
        response = requests.get("%s%s" % (self.service_url, url), auth=(self.username, self.password), params=params)
        
        if response_to_verify in str(response.content):
            return True
        else:
            return False

    def post(self, url, data, should_fail=True, headers={'Content-type': 'application/json', 'Accept': 'text/plain'}):
        if type(data) is dict:
            data = json.dumps(data)

        response = requests.post("%s%s" % (self.service_url, url), auth=(self.username, self.password), data=data, headers=headers)

        if response.status_code == 500 or response.status_code == 404 and should_fail:
            logging.error("Something went wrong. Recieved an HTTP %s. Cross check!" % response.status_code)
            exit(1)

        return response.status_code

    def put(self, url, data, headers={'Content-type': 'application/json', 'Accept': 'text/plain'}):
        if type(data) is dict:
            data = json.dumps(data)

        response = requests.put("%s%s" % (self.service_url, url), auth=(self.username, self.password), data=data, headers=headers)
        if response.status_code == 500 or response.status_code == 404 and should_fail:
            logging.error("Something went wrong. Recieved an HTTP %s. Cross check!" % response.status_code)
            exit(1)
            
        return response.status_code

    def delete(self, url):
        response = requests.delete("%s%s" % (self.service_url, url), auth=(self.username, self.password))
        return response.status_code