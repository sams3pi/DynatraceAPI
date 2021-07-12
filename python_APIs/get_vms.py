import sys
import requests,json
def getHosts():
   headerGetVm = my_headers = {
                                 "Authorization":"Api-Token "+sys.argv[1], 
                                 "Accept":"application/json", 
                                 "Content-Type":"application/json",
                              }
   responseGetVm = requests.get('https://mbb49765.live.dynatrace.com/api/v2/entities?entitySelector=type(%22AZURE_VM%22)', headers=headerGetVm)
   #responseGetVm = requests.get(' https://mbb49765.live.dynatrace.com/api/v2/entityTypes', headers=headerGetVm)
   #for typeMon in range(len(responseGetVm.json()['types']) - 1):
   #   print(responseGetVm.json()['types'][typeMon]['type']) 
   print(responseGetVm.text)

if __name__=="__main__":
   if len(sys.argv) != 4:
      print("This requires Token, Search Head and Hostname")
      sys.exit()
   getHosts()