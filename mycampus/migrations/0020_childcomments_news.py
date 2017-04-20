# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycampus', '0019_learns_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChildComments_News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('critisID', models.CharField(max_length=20, null=True)),
                ('new_id', models.IntegerField(null=True)),
                ('comment_id', models.IntegerField(null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('content', models.CharField(max_length=255, null=True)),
                ('images', models.ImageField(null=True, upload_to='news_img')),
            ],
        ),
    ]
