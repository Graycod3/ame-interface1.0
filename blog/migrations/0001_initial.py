# Generated by Django 2.1.3 on 2018-11-27 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SSID', models.CharField(max_length=200)),
                ('Psk', models.CharField(max_length=200)),
                ('SIP', models.CharField(max_length=200)),
                ('Netmask', models.CharField(max_length=200)),
                ('Gateway', models.CharField(max_length=200)),
                ('NetworkIP', models.CharField(max_length=200)),
                ('Broadcast', models.CharField(max_length=200)),
                ('Dns_nameservers', models.CharField(max_length=200)),
            ],
        ),
    ]
