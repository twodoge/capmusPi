# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 04:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycampus', '0005_auto_20170411_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learns',
            name='images',
            field=models.ImageField(null=True, upload_to='learn_img'),
        ),
    ]