# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-04 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20190701_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='orderNum',
            field=models.CharField(default=None, max_length=255, verbose_name='订单号'),
        ),
    ]