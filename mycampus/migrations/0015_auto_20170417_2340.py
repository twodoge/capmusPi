# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 23:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycampus', '0014_news_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news_like',
            old_name='critisID',
            new_name='critis',
        ),
        migrations.RenameField(
            model_name='news_like',
            old_name='new_id',
            new_name='new',
        ),
    ]
