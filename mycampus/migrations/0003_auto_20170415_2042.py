# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-15 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycampus', '0002_auto_20170415_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments_news',
            name='content',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
