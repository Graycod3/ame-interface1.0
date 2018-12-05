#!/usr/bin/env python3
import json
import re
import os.path
import pathlib
import uuid
import subprocess
import os
import django

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

os.environ.setdefault("DJANGO_SERRINGS_MODULE", "mysite.settings")

from blog.models import Post

def InterfaceWrite():
    with open ("/home/techuser/config.json", "r") as handle:
        configString = handle.read()
        config= json.loads(configString)

    interface = open("interfaces","w+")
    interface.write("source-directory /etc/network/interfaces.d \n")
    interface.write ("auto lo \n")
    interface.write ("iface lo inet loopback \n")


    interface.close()

def check_ethernet():
    import socket
    for timeout in [1]:
        try:
            print ("checking internet connection..")
            socket.setdefaulttimeout(timeout)
            host = socket.gethostbyname("www.google.com")
            s = socket.create_connection((host, 80), 2)
            s.close()
            print ("Ethernet  internet Successful.")
            return True

        except Exception as e:
            print (e)
            print ("Ethernet internet Failed.")
    return False

if __name__ =='__main__':
    con =False
    config = {}
    #Choice_two = 0
    print("Enter The Dragon Code")
    while con == False:
        print("Turning down pi network servies")
        #subprocess.call(['bash','/home/techuser/turndown.sh'])
        print("getting the info now")
        info()
        print("writing the info to the interfaces file")
        InterfaceWrite()
        subprocess.call(['bash','/home/techuser/turnup.sh'])
        con = check_ethernet()
        if  check_ethernet()==True:
             print("ethernet good")
             con = check_ethernet()
()
