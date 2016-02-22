import sqlite3
import requests
import json

from utilities.httpService import HttpService
from utilities.db import DbService


class StartMonitoring:
    def __init__(self):
        self.http = HttpService("admin","district","")
        self.db = DbService()
        self.conn = sqlite3.connect(r"services.sqlite")

    def write_service_up(self):
        print "Status - works"


    def write_service_down(self,serviceName,serviceUrl):
        print "Status - Does not work"
        self.db.insert_into_monitor(serviceName,serviceUrl,"Service is Down")
        self.db.print_all_in_monitor()

    def write_assertion_failed(self,serviceName,serviceUrl):
        print "Status - Does not work"
        self.db.insert_into_monitor(serviceName,serviceUrl,"Assertion Failed")
        self.db.print_all_in_monitor()

    def run(self):
        with open('data/validations.json', 'r') as myfile:
            service_and_urls = json.loads(myfile.read())

        # service_and_urls = self.db.get_all_services_and_url()

        for service in service_and_urls:
            print "pinging service - " + service["serviceName"]
            print "URL - " + service["URL"]
            if service["validateOutput"] == False:
                try:
                    response = self.http.get(service["URL"])
                    self.write_service_up()
                except requests.exceptions.RequestException:
                    self.write_service_down(service["serviceName"],service["URL"])

            else:
                try:
                    response = self.http.get_and_verify(service["URL"],service["output"])
                    if response == True:
                        self.write_service_up()
                    else:
                        self.write_assertion_failed(service["serviceName"],service["URL"])
                except requests.exceptions.RequestException:
                    self.write_service_down(service["serviceName"],service["URL"])
