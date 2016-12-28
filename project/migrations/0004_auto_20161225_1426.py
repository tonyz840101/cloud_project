# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-25 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_measuring_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measuring_data',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='measuring_data',
            name='avg_ex_hour',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='measuring_data',
            name='avg_sleep_hour',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='measuring_data',
            name='height',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='measuring_data',
            name='weight',
            field=models.FloatField(default=0),
        ),
    ]