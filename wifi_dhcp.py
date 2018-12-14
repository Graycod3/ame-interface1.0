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

from blog.models import dhcp

def info():
    print("In info function")
    creds=dhcp.objects.first()

    print("assigning creds")
    config['ssid']=creds.SSID
    config['password']=creds.psk
    print("getting attributes yidi yada")
    jstring = json.dumps(config)

    with open("/home/techuser/config.json", "w+") as handle:
        handle.write(jstring)
    print("done")
def InterfaceWrite():
    with open ("/home/techuser/config.json", "r") as handle:
        configString = handle.read()
        config= json.loads(configString)

    interface = open("/etc/network/interfaces","w+")
    interface.write("source-directory /etc/network/interfaces.d \n")
    interface.write ("auto lo \n")
    interface.write ("iface lo inet loopback \n")

    ssid = config['ssid']
    password = config['password']

    interface.write("allow-hotplug wlan0 \n")
    interface.write("auto wlan0 \n")
    interface.write("\n")
    interface.write("iface wlan0 inet dhcp \n")
    interface.write ("\t"+"wpa-ssid "+'"'+ssid+'"'+"\n")
    interface.write ("\t"+"wpa-psk "+'"'+password+'"'+"\n")

    interface.close()


def CheckConnection():
    ps = subprocess.Popen(['iwconfig'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
   # try:
    output = subprocess.check_output(('grep', 'ESSID'), stdin=ps.stdout).decode()
    status = output.split('ESSID:')[1].split('/')[0]
    if status == 'off':
        print("Wi-Fi not connected")#do something about this, reload the page or sum
        cmd = 'bash -c /home/techuser/turndown.sh'
        process=subprocess.Popen(cmd, shell=True, stdout =subprocess.PIPE)
        process.wait()
        print(process.returncode)
        assert process.returncode == 0

        copyfile('/home/pi/Docker/NewP/NewProject/interfaces.bak','/etc/network/interfaces')
        print("Copied back OG config")
        cmd = 'bash -c /home/techuser/turnup.sh'
        process=subprocess.Popen(cmd, shell=True, stdout =subprocess.PIPE)
        process.wait()
        assert process.returncode == 0 
        return False
    else:
        print("Wi-Fi connected HEY")
        return True
   # except subprocess.CalledProcessError:
        # grep did not match any lines
    #    print("No wireless networks connected")
    #    return False


if __name__ =='__main__':
    con =False
    config = {}
    #Choice_two = 0
    print("Enter The Dragon Code")
    print("Turning down pi network servies")
    subprocess.call(['bash','/home/techuser/turndown.sh'])
    print("getting the info now")
    info()
    print("writing the info to the interfaces file")
    InterfaceWrite()
    print("done writing")
    subprocess.call(['bash','/home/techuser/turnup.sh'])
    print("Starting Network Services")
    con = CheckConnection()
    print("checking Internet connection")
