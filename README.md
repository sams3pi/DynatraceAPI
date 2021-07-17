# DynatraceAPI
## Introduction
This repository contains sample Python scripts that can be used to modify/create configuration on Dynatrace. They can be used in conjuction to one another. In the backend scripts use Dynatrace Configuration and Environemnt APIs.
Dynatrace API Token are always passed as command line argument (sys.argv[1]) while running the code so that it is not kept in the code.

There is Ansible Code (playbook.yml) as well which can be used to deploy one agent on the servers. This uses the Dynatrace OneAgent role from Dynatrace that is available on Ansible Galaxy.

## Scripts
There are multiple scripts at this moment </br>
createMaintenance.py -> Creates Maintenance windows in dynatrace. This can be helpful in multiple situations like Scheduled Hardware Maintenance and Quarterly Patching to supress the alerts. </br>
craeteSynthetic.py -> Creates Synthetic Monitors on Dynatrace to monitor your application URLs. Specially useful to check the reachability of endpoints. </br>
disableMonitoring.py -> This can be used to disable the host from being monitored in Dynatrace. Particularly useful when you do not want to provide admin rights to people to do the same. This can act as an abstraction layer. </br>
getHostId.py -> Provide the host ID as an input to other scripts based on the Display names in Dynatrace. End users should be able to use scripts based on host names witout knowing the host IDs. </br>
playbook.yml -> Deploy and configure Dynatrace One agent on the servers using Ansible and Dynatrace OneAgent Ansible Role from Ansible Galaxy.
inventory -> Inventory of servers in which the oneagent has to be installed.

## Requirements
1. Python3 (yum install python3)
2. PIP3 (yum install python3-pip)
3. Requests Module from Python (pip3 install requests)
4. Ansible > 2.7 (pip3 install ansible/yum install ansible)
5. Ansible OneAgent Role (ansible-galaxy install dynatrace.oneagent)