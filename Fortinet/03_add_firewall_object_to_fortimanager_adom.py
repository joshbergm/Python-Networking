##############################################################
##      - Python script for adding address FortiManager     ##
##      - Author: Joshua Bergman                            ##
##      - Version: 0.1 (Draft)                              ##
##      - Date: 16-03-2024                                  ##
##############################################################

import pyFortiManagerAPI
import getpass
import sys

## Define variables
username = input("Username: ")
password = getpass.getpass(prompt="Password: ", stream=None)
host = input("FortiManager IP: ")
objectname = input("Object name: ")
associated_interface = input("Interface (type any for default): ")
subnet = input("IP address / netmask: ")

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
available_adoms = get_adoms_from_fortimanager
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
answer_adom = input(question_adom)

## List available policy packages
available_policy_packages = get_policy_package_from_fortimanager
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
answer_adom = input(question_adom)

## Create address object
FortiManager.add_firewall_address_object(
    objectname,
    associated_interface,
    subnet
)