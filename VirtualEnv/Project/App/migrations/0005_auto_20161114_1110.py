# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 17:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_auto_20161114_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notion',
            name='last_updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Last Update'),
        ),
        migrations.AlterField(
            model_name='pattern_piece',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Titel'),
        ),
    ]