import sys
import requests,json
def createSynthetic():

   syntheticBodymin = {
      "frequencyMin": 10,
      "type": "HTTP",
      "name": "restExample",
      "locations": [
         "GEOLOCATION-B1B096907F0E9A8C"
      ],
      "enabled": True,
      "script": {
      },
      "tags": [
         "fromAPI"
      ]
   }


   syntheticBody=json.dumps(syntheticBodymin)

   headerPostSynthetic = my_headers = {
                                 "Authorization":"Api-Token "+sys.argv[1], 
                                 "Accept":"application/json", 
                                 "Content-Type":"application/json",
                              }
   responseSyntheticMonitor = requests.post('https://mbb49765.live.dynatrace.com/api/v1/synthetic/monitors', headers=headerPostSynthetic, data=syntheticBody)
   print(responseSyntheticMonitor)
   print(responseSyntheticMonitor.text)

if __name__=="__main__":
   if len(sys.argv) != 5:
      print("This requires Token, Search Head and Hostname")
      sys.exit()
   createSynthetic()