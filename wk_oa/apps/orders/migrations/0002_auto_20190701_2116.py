# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-01 13:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderdetail',
            options={'verbose_name': '订单详情', 'verbose_name_plural': '订单详情'},
        ),
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name': '订单', 'verbose_name_plural': '订单'},
        ),
    ]
