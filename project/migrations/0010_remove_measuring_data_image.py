# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 08:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_user_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measuring_data',
            name='image',
        ),
    ]
