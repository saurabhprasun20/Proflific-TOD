import requests, os , sys, json
from dotenv import load_dotenv

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'data'))

api_url = "https://api.prolific.co/api/v1/studies/"

load_dotenv()

auth = os.getenv('AUTH_TOKEN')

data = {}
sibB = os.path.join(os.path.dirname(__file__), '..', 'data')

for filename in os.listdir(sibB):
    print(filename)
    if filename == 'automate-data.json':
        f = open(os.path.join(sibB, filename))
        data = json.load(f)
        print(data)


headers = {
  'Authorization': "Token",
  'Content-Type': 'application/json'
}

headers['Authorization'] = auth

response = requests.request("POST", api_url, headers=headers, data=json.dumps(data))
res_data = response.json()

print(res_data["id"])

filename = 'data.json'
with open(os.path.join(sibB, filename), "r+") as jsonFile:
  data = json.load(jsonFile)
  data["surveyId"] = res_data["id"]
  jsonFile.seek(0)  # rewind
  json.dump(data, jsonFile)
  jsonFile.truncate()
