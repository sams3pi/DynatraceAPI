import sys
import requests,json
from getHostId import *

def disableMonitoring(dtToken, displayName):
    host_id=getHostIdForHost(dtToken, displayName)
    print(host_id)
    MonitoringConfigMin={
        "monitoringEnabled": False,
        "MonitoringMode": "FULL_STACK"
    }
    MonitoringConfig=json.dumps(MonitoringConfigMin)
    headerDisableMonitoring ={
        "Authorization":"Api-Token"+dtToken,
        "Accept":"application/json",
        "Content-Type":"application/json"
    }
    responseDisableMonitoring=requests.put('https://mbb49765.live.dynatrace.com/api/config/v1/hosts/{}/monitoring'.format(host_id),headers=headerDisableMonitoring,data=MonitoringConfig)
    print(responseDisableMonitoring)

if __name__=="__main__":
    if len(sys.argv)!=3:
        print("Please provide correct command line arguments.\n1.API Token\n2.Display Name of Host from Dynatrace")
        sys.exit()
    disableMonitoring(sys.argv[1],sys.argv[2])