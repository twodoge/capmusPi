# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 20:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycampus', '0014_auto_20170414_2020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments_news',
            old_name='new',
            new_name='new_id',
        ),
    ]
