
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    SIP = models.CharField(max_length=200)
    Netmask = models.CharField(max_length=200)
    Gateway = models.CharField(max_length=200)
    NetworkIP = models.CharField(max_length=200)
    Broadcast = models.CharField(max_length=200)
    Dns_nameservers = models.CharField(max_length=200)


class ConfigInfo(models.Model):
    SSID = models.CharField(max_length=50)
    psk = models.CharField(max_length=50)
    sIP = models.CharField(max_length=20)
    netmask = models.CharField(max_length=20)
    gateway = models.CharField(max_length=20)
    networkIP=models.CharField(max_length=20)
    broadcast=models.CharField(max_length=20)
    dns_nameservers=models.CharField(max_length=20)

class dhcp(models.Model):
    SSID=models.CharField(max_length=50)
    psk=models.CharField(max_length=50)
