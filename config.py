import sys


API_URL_dev = "http://ec2-52-206-132-150.compute-1.amazonaws.com:8050"

if len(sys.argv) > 2:
    if sys.argv[2] == "prod":
     API_URL= "http://ec2-52-206-109-219.compute-1.amazonaws.com:8050"

    if sys.argv[2] == "qa":
     API_URL = "http://ec2-35-163-23-118.us-west-2.compute.amazonaws.com:8050"

if len(sys.argv) > 3:
    file_path = '/media/ephemeral0/xad/userstore/dump.txt'
else:
    file_path = '/Users/sakthigurumaharaj/Desktop/xad/sakthixad/cab_automation/resources/dump.txt'


# API_URL = "http://ec2-52-206-109-219.compute-1.amazonaws.com:9050"

brand_id = "1"
category_id = "581208"


