import requests

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer T1530GW4R81PRD3MHSQGHJOI9D3GZG5Y4K7BTK0G'
}

job_id = input("Enter the Job ID: ")

url = f'https://api.runpod.ai/v2/vuusai5vaeia2x/status/{job_id}'

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.text)
