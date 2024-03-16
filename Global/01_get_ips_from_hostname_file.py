##############################################################
##      - Python script to get IP's from hostnames          ##
##      - Author: Joshua Bergman                            ##
##      - Version: 0.1 (Draft)                              ##
##      - Date: 16-03-2024                                  ##
##############################################################

import socket
import getpass
import os

## Assemble path
pc_username = getpass.getuser()
file_path = os.path.join("c:/Users/", pc_username, "Documents/Python-Networking/")

## Define variables
input_file = os.path.join(file_path, "hostnamelist.txt")

## Get IP from hostname function
def resolve_from_hostname(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        return None

## Read hostname, get ip and print in terminal
with open(input_file, 'r') as hostname_file:
    for line in hostname_file:
        hostname = line.strip()
        ip_address = resolve_from_hostname(hostname)
        print(ip_address, " - ", hostname)
