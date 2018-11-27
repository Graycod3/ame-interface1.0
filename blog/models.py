
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    SSID = models.CharField(max_length=200)
    Psk = models.CharField(max_length=200)
    SIP = models.CharField(max_length=200)
    Netmask = models.CharField(max_length=200)
    Gateway = models.CharField(max_length=200)
    NetworkIP = models.CharField(max_length=200)
    Broadcast = models.CharField(max_length=200)
    Dns_nameservers = models.CharField(max_length=200)
