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

from device_interfaces.models import ConfigInfo

def info():
    print("In info function")
    creds=ConfigInfo.objects.first()

    print("assigning creds")
    config['ssid']=creds.SSID
    config['password']=creds.psk
    config['StatIP']=creds.sIP
    config['Netmask']=creds.netmask

    config['gateway']=creds.gateway
    config['Network']=creds.networkIP
    config['Broadcast']=creds.broadcast
    config['DNS']=creds.dns_nameservers
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

    ssid = config['ssid']
    StatIP = config['StatIP']
    password = config['password']
    dns=config['DNS']

    netmask=config['Netmask']
    network=config['Network']
    broadcast=config['Broadcast']
    gateway=config['gateway']

    interface.write("allow-hotplug wlan0 \n")
    interface.write("auto wlan0 \n")
    interface.write("\n")
    interface.write("iface wlan0 inet static \n")

    interface.write ("\t"+"wpa-ssid "+'"'+ssid+'"'+"\n")
    interface.write ("\t"+"wpa-psk "+'"'+password+'"'+"\n")
    interface.write ("\t"+"address "+StatIP+"\n")
    interface.write("\t"+"netmask "+netmask+"\n")

    interface.write("\t"+"network "+network+"\n")
    interface.write("\t"+"broadcast "+broadcast+"\n")
    interface.write("\t"+"gateway "+gateway+"\n")
    interface.write("\t"+"dns-nameservers "+dns+"\n")

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
        con = CheckConnection()
        if CheckConnection()==True:
             con = CheckConnection()
        else:
             
