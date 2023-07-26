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
            "feature_service": "hotel_info",
            "entities": {"eg_property_id":[1001939328]} ,
        }
        response = self.client.post("/get-online-features", data = json.dumps(event_dict), verify=True)
        print(response.json())

# class FeastUser(HttpUser):
    
    @task
    def push(self):
        event_dict = {
            "driver_id": [1001],
            "event_timestamp": [str(datetime(2021, 5, 13, 10, 59, 42))],
            "created": [str(datetime(2021, 5, 13, 10, 59, 42))],
            "conv_rate": [1.0],
            "acc_rate": [3.0],
            "avg_daily_trips": [1000],
            "string_feature": "test2",
        }
        push_data = {
            "push_source_name":"driver_stats_push_source",
            "df":event_dict,
            "to":"online",
        }
        self.client.post(
            "/push",
            data=json.dumps(push_data))
        
    