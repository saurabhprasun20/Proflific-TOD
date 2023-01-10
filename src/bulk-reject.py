import requests, os , sys, json, csv
from dotenv import load_dotenv

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'data'))

load_dotenv()

auth = os.getenv('AUTH_TOKEN')

data = {}
sibB = os.path.join(os.path.dirname(__file__), '..', 'data')

with open(os.path.join(sibB, "reject.csv"), 'r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["submissionId"])

        temp_sub_id = row["submissionId"]
        url = "https://api.prolific.co/api/v1/submissions/"
        submissionId=temp_sub_id
        endpoint = "/transition/"

        final_url = url+submissionId+endpoint
        ##Approve or reject
        payload = json.dumps({
            "action": "REJECT"
        })
        headers = {
        'Authorization': 'Token',
        'Content-Type': 'application/json'
        }

        headers['Authorization'] = auth

        response = requests.request("POST", final_url, headers=headers, data=payload)

        print(response.text)
