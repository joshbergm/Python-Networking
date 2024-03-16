##############################################################
##      - Python script for adding address FortiManager     ##
##      - Author: Joshua Bergman                            ##
##      - Version: 0.1 (Draft)                              ##
##      - Date: 16-03-2024                                  ##
##############################################################

import pyFortiManagerAPI
import getpass
import sys
import subprocess

## Define variables
username = input("Username: ")
password = getpass.getpass(prompt="Password: ", stream=None)
host = "FortiManager IP"

## Assemble FortiManager connection details
FortiManager = pyFortiManagerAPI.FortiManager(
    host,
    username,
    password
)

## Define parameters
fortimanager_policy_package = FortiManager.get_policy_packages()

## Get ADOM's
def get_adoms_from_fortimanager():
    fortimanager_adoms = FortiManager.get_adoms()
    adom_list = fortimanager_adoms.stdout.split('\n')
    return adom_list

available_adoms = get_adoms_from_fortimanager

if not available_adoms:
    print("No ADOM available")
    sys.exit()

question_adom = {
    'type': 'list',
    'name': 'ADOM',
    'message': 'Please select ADOM',
    'ADOM': available_adoms
}

answer_adom = input(question_adom)