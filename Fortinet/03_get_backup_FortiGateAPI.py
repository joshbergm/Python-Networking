##############################################################
##      - Config backup script via FortiGate API            ##
##      - Author: Joshua Bergman                            ##
##      - Version: 0.1 (Draft)                              ##
##      - Date: 22-03-2024                                  ##
##############################################################

from fortigate_api import FortiGateAPI
import getpass
from datetime import datetime
import os

## Define login variables
fortigate_ip = input("FortiGate IP: ")
username = input("Username: ")
token = getpass.getpass(prompt="Token: ", stream=None)

## Define other
pc_username = getpass.getuser()
date = datetime.now().strftime('%d_%m_%Y')
backup_file_path = os.path.join("c:/Users/", pc_username, "Documents/Python-Networking/")

## Assemble API request
fortigate_backup_api = FortiGateAPI(host=fortigate_ip, token=token)
backup_api_request = f'https://{fortigate_ip}/api/v2/monitor/system/config/backup?'

backup_file_response = fortigate_backup_api.fortigate.get(backup_api_request)

## Write backup content to file
if backup_file_response.ok:
    with open(backup_file_path + f'FortiGate_{date}.conf', 'wb') as f:
        f.write(backup_file_response.content)
    print("Config file saved succesfully as:" + backup_file_path + f"FortiGate_{date}.conf")
else:
    print("Failed to retrieve config file, Status code:", backup_file_response.status_code)