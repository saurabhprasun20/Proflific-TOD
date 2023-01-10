import requests, os
from dotenv import load_dotenv

url = "https://api.prolific.co/api/v1/studies/"

load_dotenv()
auth = os.getenv('AUTH_TOKEN')

payload={}
headers = {
  'Authorization': 'Token',
}

headers['Authorization'] = auth

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
