##############################################################
##      - Python script for adding address FortiManager     ##
##      - Author: Joshua Bergman                            ##
##      - Version: 0.1 (Draft)                              ##
##      - Date: 16-03-2024                                  ##
##############################################################

import pyFortiManagerAPI
import getpass
import sys
import prompt

## Define variables
username = input("Username: ")
password = getpass.getpass(prompt="Password: ", stream=None)

## FortiManager Variables
### Host
host = ""
while not host:
    host = input("FortiManager IP: ")
    if not host:
        print("FortiManager IP cannot be empty. Please enter a valid IP.")

### Objectname
objectname = ""
while not objectname:
    objectname = input("Object name: ")
    if not objectname:
        print("Object name cannot be empty. Please enter a valid name.")

### Associated interface
associated_interface = ""
while not associated_interface:
    associated_interface = input("Interface (type any for default): ")
    if not associated_interface:
        print("Interface cannot be empty. Please enter a valid interface name.")

### Subnet
subnet = ""
while not subnet:
    subnet = input("IP address / netmask: ")
    if not subnet:
        print("IP address / netmask cannot be empty. Please enter a valid value.")

## Assemble FortiManager connection details
FortiManager = pyFortiManagerAPI.FortiManager(
    host,
    username,
    password
)

## Get ADOM's
def get_adoms_from_fortimanager():
    fortimanager_adoms = FortiManager.get_adoms()
    adom_list = fortimanager_adoms.stdout.split('\n')
    return adom_list

## Get policy packages
def get_policy_package_from_fortimanager():
    fortimanager_policy_package = FortiManager.get_policy_packages()
    policy_package_list = fortimanager_policy_package.stdout.split('\n')
    return policy_package_list

## List available adoms
available_adoms = get_adoms_from_fortimanager()
if not available_adoms:
    print("No ADOM available")
    sys.exit()

## Create question with aquired ADOM's
question_adom = {
    'type': 'list',
    'name': 'ADOM',
    'message': 'Please select ADOM',
    'ADOM': available_adoms
}
answer_adom = prompt(question_adom)

## List available policy packages
available_policy_packages = get_policy_package_from_fortimanager()
if not available_policy_packages:
    print("No Policy Package available")
    sys.exit()


## Create question with aquired policy packages
question_adom = {
    'type': 'list',
    'name': 'Policy Package',
    'message': 'Please select Policy Package',
    'Policy_Package': available_policy_packages
}
answer_adom = prompt(question_adom)

## Create address object
FortiManager.add_firewall_address_object(
    objectname,
    associated_interface,
    subnet
)