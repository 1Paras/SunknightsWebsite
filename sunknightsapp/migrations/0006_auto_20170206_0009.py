# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-06 00:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunknightsapp', '0005_remove_pointsinfo_masterypointssubtract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clanuser',
            name='description',
            field=models.CharField(blank='', default='', max_length=1500),
        ),
        migrations.AlterField(
            model_name='dailyquest',
            name='task',
            field=models.CharField(max_length=500),
        ),
    ]
