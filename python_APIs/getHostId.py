import requests
import sys
import json

def getHostIdForHost(dtToken, hostDisplayName):
    headerGetHostId={
        "Authorization":"Api-Token"+dtToken,
        "Accept":"application/json",
        "Content-Type":"application/json"
    }
    getVms=json.loads(requests.get('https://mbb49765.live.dynatrace.com/api/v1/oneagents',headers=headerGetHostId).text)
    for currentHost in range(0,len(getVms["hosts"])):
        if getVms["hosts"][currentHost]["hostInfo"]["displayName"]==hostDisplayName:
            return getVms["hosts"][currentHost]["hostInfo"]["entityId"].strip()

if __name__=="__main__":
    if len(sys.argv) !=3:
        print("Please enter correct command line argurments\n1.API Token\n2.Host Diplay Name in Dynatrace")
        sys.exit()
    returnID=getHostIdForHost(sys.argv[1],sys.argv[2])
    print(returnID)