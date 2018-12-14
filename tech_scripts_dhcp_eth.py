#!/usr/bin/env python3
import json
import re
import os.path
import pathlib
import uuid
import subprocess
import os
import django
from shutil import copyfile

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

os.environ.setdefault("DJANGO_SERRINGS_MODULE", "mysite.settings")

from blog.models import Post

def InterfaceWrite():
    with open ("/home/techuser/config.json", "r") as handle:
        configString = handle.read()
        config= json.loads(configString)

    interface = open("/etc/network/interfaces","w+")
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
            cmd = 'bash -c /home/techuser/turndown.sh'
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            process.wait()
            assert process  returncode == 0

            copyfile('/home/pi/Docker/NewP/NewProject/interfaces.bak','/etc/network/interfaces')
            print("copied  BACK  OGS")
            cmd = 'bash -c /home/techuser/turnup.sh'
            process=subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            process.wait()
            asset process.returncode == 0 

            print (e)
            print ("Ethernet internet Failed.")
    return False

if __name__ =='__main__':
    con =False
    config = {}
    #Choice_two = 0
    print("Enter The Dragon Code")
    print("Turning down pi network services")
    subprocess.call(['bash','/home/techuser/turndown.sh'])
    print("getting the info now")
    info()
    print("writing the info to the interfaces file")
    InterfaceWrite()
    subprocess.call(['bash','/home/techuser/turnup.sh'])
    check_ethernet()
    print("ethernet test ends")
