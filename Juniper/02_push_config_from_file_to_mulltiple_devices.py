##############################################################
##      - Python script for applying Juniper config         ##
##      - Author: Joshua Bergman                            ##
##      - Version: 0.1 (Draft)                              ##
##      - Date: 15-03-2024                                  ##
##############################################################

## Import libraries
import netmiko
import getpass
import os
from time import sleep
from netmiko import ConnectHandler

## Define variables
username = input("Username: ")
password = getpass.getpass(prompt="Password: ", stream=None)
device_type = 'juniper_junos'
port = '22'

## Get username for file handling
pc_username = getpass.getuser()

## Create file path
config_file_path = os.path.join("c:/Users/", pc_username, "Documents/PythonJuniper/")

## Define file names
configuration_file_input = os.path.join(config_file_path, "config.txt")
ip_address_file = os.path.join(config_file_path, "iplist.txt")
output_file = os.path.join(config_file_path), "output.txt"

with open(ip_address_file, 'r') as ip_file:
    ## Loop through each line in the IP address file
    for line in ip_file:
        ## Strip newline characters from the line
        line = line.strip()

        try:
            ## SSH connection details
            juniper = {
            'device_type': device_type,
            'host': line,
            'username': username,
            'password': password,
            'port': port,
            }

            # Create SSH session
            net_connect = ConnectHandler(**juniper)

            # Send config to switch
            net_connect.config_mode()
            net_connect.send_config_from_file(configuration_file_input)

            # Commit changes
            net_connect.commit()

            # Disconnect SSH session
            net_connect.disconnect()

            print("Config pushed to:", line)
            output_file.write("Config pushed to: " + line + "\n")

        except netmiko.ssh_exception.NetMikoTimeoutException:
            print("SSH connection timed out to: ", line)
            output_file.write("SSH connection timed out to: " + line + "\n")
            continue  # Continue to the next IP address

        except netmiko.ssh_exception.NetMikoAuthenticationException:
            print("SSH authentication failed for:", line)
            output_file.write("SSH authentication failed for: " + line + "\n")
            continue  # Continue to the next IP address

        except Exception as e:
            print("An error occurred for: ", line, e)
            output_file.write("An error occurred for: " + line + "\n")
            continue  # Continue to the next IP address

        sleep(0.2)