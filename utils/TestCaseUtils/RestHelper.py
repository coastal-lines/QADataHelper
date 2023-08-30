import json
import requests

class RestApi:

    def __init__(self, server):
        self.server = server

    def get_defects(self, objectID, credits):
        url = f"https://{self.server}/slm/webservice/v2.0/TestCase/{objectID}/Defects"
        headers = {
            'Authorization': f'Basic {credits}'
        }
        response = requests.request("GET", url, headers=headers)
        json_response = json.loads(response.text)

        return json_response["QueryResult"]["TotalResultCount"]
        
    def get_total_duration(self, objectID, credits):
        url = f"https://{self.server}/slm/webservice/v2.0/TestCase/{objectID}/results?&pagesize=200&start=1"
        headers = {
            'Authorization': f'Basic {credits}', 'PageSize': '200'
        }
        # add catch 404
        response = requests.request("GET", url, headers=headers)
        json_response = json.loads(response.text)

        return json_response["QueryResult"]["Results"]

