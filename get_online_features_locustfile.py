from locust import task, HttpUser, between
import os, random
import json
import requests
from datetime import datetime
#from feast import push 


class FeastUser(HttpUser):    
    @task
    def get_online(self):
        event_dict = {
            "feature_service": "hotel_v1",
            "entities": {"hotelId":[1001939328]} ,
        }
        response = self.client.post("/get-online-features", data = json.dumps(event_dict))
        print(response.json())

