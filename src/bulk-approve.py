import requests
import json, os
from dotenv import load_dotenv

url = "https://api.prolific.co/api/v1/submissions/bulk-approve/"

load_dotenv()

auth = os.getenv('AUTH_TOKEN')

payload = json.dumps({
  "study_id": "60f6acb180a7b59ac0621f9e",
  "participant_ids": [
    "60f25f799fbd8a136cc6a9b0",
    "5ce69ff9b1e73b000146186d"
  ]
})

headers = {
  'Authorization': 'Token',
  'Content-Type': 'application/json'
}

headers['Authorization'] = auth

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
