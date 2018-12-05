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

def info():
    print("In info function")
    creds=Post.objects.first()

    print("assigning creds")
    config['StatIP']=creds.SIP
    config['Netmask']=creds.Netmask

    config['gateway']=creds.Gateway
    config['Network']=creds.NetworkIP
    config['Broadcast']=creds.Broadcast
    config['DNS']=creds.Dns_nameservers
    print("getting attributes yidi yada")
    jstring = json.dumps(config)

    with open("/home/techuser/config.json", "w+") as handle:
        handle.write(jstring)
    print("done")

def InterfaceWrite():
    with open ("/home/techuser/config.json", "r") as handle:
        configString = handle.read()
        config= json.loads(configString)

    interface = open("interfaces","w+")
    interface.write("source-directory /etc/network/interfaces.d \n")
    interface.write ("auto lo \n")
    interface.write ("iface lo inet loopback \n")

    StatIP = config['StatIP']
    dns=config['DNS']

    netmask=config['Netmask']
    network=config['Network']
    broadcast=config['Broadcast']
    gateway=config['gateway']

    interface.write ("auto eth0 \n")
    interface.write ("iface eth0 inet static \n")
    interface.write("address "+StatIP+"\n")
    interface.write("\t"+"netmask "+netmask+"\n")
    interface.write("\t"+"network "+network+"\n")
    interface.write("\t"+"broadcast "+broadcast+"\n")
    interface.write("\t"+"gateway "+gateway+"\n") 
    interface.write("\t"+"dns-nameservers "+dns+"\n")
    interface.write("\n")

    interface.close()

def CheckConnection():
    ps = subprocess.Popen(['iwconfig'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    try:
        output = subprocess.check_output(('grep', 'ESSID'), stdin=ps.stdout).decode()
        status = output.split('ESSID:')[1].split('/')[0]
        if status == 'off':
            print("Wi-Fi not connected")#do something about this, reload the page or sum
            return False
        else:
            print("Wi-Fi connected")
            return True
    except subprocess.CalledProcessError:
        # grep did not match any lines
        print("No wireless networks connected")
        return False

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
