
from django import forms
from .models import ConfigInfo
from .models import dhcp
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('SIP', 'Netmask', 'Gateway', 'NetworkIP', 'Broadcast', 'Dns_nameservers')

class ConfigInfoForm(forms.ModelForm):
        class Meta:
            model=ConfigInfo
            fields=('SSID','psk','sIP','netmask','gateway','networkIP','broadcast','dns_nameservers',)

class dhcpForm(forms.ModelForm):
        class Meta:
            model=dhcp
            fields=('SSID','psk',)
