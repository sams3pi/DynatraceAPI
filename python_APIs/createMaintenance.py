import sys
import requests,json

from requests.api import head

def createMaintenance(dtToken):
    payloadMaintenance={
  "name": "Main app update",
  "description": "Deployment of a new version of the main application",
  "type": "PLANNED",
  "suppression": "DONT_DETECT_PROBLEMS",
  "scope": {
    "entities": [
    	],
    "matches": [
      {
        "type": "HOST",
        "tags": [
          {
            "context": "CONTEXTLESS",
            "key": "batch",
            "value": 1
          }
        ],
        "tagCombination": "OR"
      }
    ]
  },
  "schedule": {
    "recurrenceType": "ONCE",
    "start": "2021-07-31 08:00",
    "end": "2021-07-31 13:00",
    "zoneId": "UTC+02:00"
  }
}

    payloadMaintenance=json.dumps(payloadMaintenance)
    headerMaintenance = {
        "Authorization":"Api-Token "+dtToken,
        "Content-Type":"application/json"
    }
    responseMaintenance=requests.post('https://mbb49765.live.dynatrace.com/api/config/v1/maintenanceWindows',headers=headerMaintenance,data=payloadMaintenance)
    print(responseMaintenance)
    print(responseMaintenance.text)

if __name__=="__main__":
    if len(sys.argv)!=2:
        print("Please provide correct command line arguments.\n1.API Token\n2.Display Name of Host from Dynatrace")
        sys.exit()
    createMaintenance(sys.argv[1])
    #Provide Dynatrace Token as command line argument while running the code