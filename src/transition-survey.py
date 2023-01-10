import requests, os , sys, json
from dotenv import load_dotenv

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'data'))

load_dotenv()
auth = os.getenv('AUTH_TOKEN')

url = "https://api.prolific.co/api/v1/studies/"
endpoint = "/transition/"

sibB = os.path.join(os.path.dirname(__file__), '..', 'data')

filename = 'data.json'
with open(os.path.join(sibB, filename), "r+") as jsonFile:
    data = json.load(jsonFile)
    survey_id = data["surveyId"]

final_url = url+survey_id+endpoint

##Update with below status to change the survey status.
# PAUSE: Pause the study
# START: Start a paused study
# STOP: Stop a study completely, to make it active again you will need to increase the number of places
payload = json.dumps({
  "action": "PUBLISH"
})
headers = {
  'Authorization': 'Token',
  'Content-Type': 'application/json'
}
headers['Authorization'] = auth

response = requests.request("POST", final_url, headers=headers, data=payload)

print(response.text)
