# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycampus', '0018_auto_20170418_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Learns_like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('critisID', models.CharField(max_length=20, null=True)),
                ('learn_id', models.IntegerField(null=True)),
                ('liked', models.IntegerField(default=0)),
            ],
        ),
    ]
