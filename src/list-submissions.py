import requests, os , sys, json
from dotenv import load_dotenv

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'data'))

url = "https://api.prolific.co/api/v1/studies/"
endpoint = "/submissions/"

load_dotenv()

auth = os.getenv('AUTH_TOKEN')

sibB = os.path.join(os.path.dirname(__file__), '..', 'data')

filename = 'data.json'
with open(os.path.join(sibB, filename), "r+") as jsonFile:
    data = json.load(jsonFile)
    survey_id = data["surveyId"]

final_url = url+survey_id+endpoint

print(final_url)

payload={}
headers = {
  'Authorization': 'Token',
}
headers['Authorization'] = auth

response = requests.request("GET", final_url, headers=headers, data=payload)

print(response.text)
