import requests
import time
import json

# Load data from external JSON file
with open("XLInstance_test_input.json", "r") as json_file:
    data = json.load(json_file)

url = "https://api.runpod.ai/v2/vuusai5vaeia2x/runsync"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer T1530GW4R81PRD3MHSQGHJOI9D3GZG5Y4K7BTK0G"
}
response = requests.post(url, json=data, headers=headers)
response_data = response.json()
print("Response Data",response_data)
with open("response.json", "w") as json_file:
    json.dump(response_data, json_file)