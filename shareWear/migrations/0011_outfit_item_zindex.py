# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 21:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareWear', '0010_profile_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='outfit_item',
            name='zIndex',
            field=models.CharField(default=b'1', max_length=100),
        ),
    ]
