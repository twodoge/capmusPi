# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycampus', '0003_auto_20170415_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments_learns',
            name='images',
            field=models.ImageField(null=True, upload_to='learn_img'),
        ),
        migrations.AddField(
            model_name='comments_learns',
            name='learn_id',
            field=models.IntegerField(null=True),
        ),
    ]
