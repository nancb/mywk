# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-04 01:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lends', '0002_auto_20190701_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='lendrecord',
            name='is_past',
            field=models.BooleanField(default=0, verbose_name='是否过期'),
        ),
    ]
