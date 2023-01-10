import requests, os
import json
from dotenv import load_dotenv

url = "https://api.prolific.co/api/v1/submissions/"
submissionId="1234"
endpoint = "/transition/"

load_dotenv()

auth = os.getenv('AUTH_TOKEN')

final_url = url+submissionId+endpoint
##Approve or reject
payload = json.dumps({
  "action": "APPROVE"
})
headers = {
  'Authorization': 'Token',
  'Content-Type': 'application/json'
}

headers['Authorization'] = auth

response = requests.request("POST", final_url, headers=headers, data=payload)

print(response.text)
