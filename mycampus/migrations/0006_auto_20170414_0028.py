# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 00:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycampus', '0005_auto_20170413_2240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teasingwall',
            old_name='formsb',
            new_name='fromsb',
        ),
    ]
