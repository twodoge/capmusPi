# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycampus', '0015_auto_20170417_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_like',
            name='liked',
            field=models.IntegerField(default=0),
        ),
    ]
