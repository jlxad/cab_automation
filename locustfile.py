from locust import HttpLocust, TaskSet, task
import json
import unittest2
import requests


class MyTaskSet(TaskSet):


    @task(1)
    def segment_post(l):


        request = {
            "type": "AND",
            "value": [{
                "type": "country",
                "value": "us"
            }, {
                "type": "OR",
                "value": [{
                    "type": "brand",
                    "value": {
                        "id": 9
                    }
                }, {
                    "type": "behavior",
                    "value": "go"
                },
                    {
                        "type": "category",
                        "value": {
                            "id": "581208"
                        }
                    }
                ]
            }
            ]
        }

        path = "/segment_size?query=" + str(json.dumps(request))
        response = l.client.get(path,headers={"User-Agent":"locust"})
        if response.status_code is not 200:
            raise Exception("Request for segment size failed")




class MyLocust(HttpLocust):
    weight = 1
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 15000