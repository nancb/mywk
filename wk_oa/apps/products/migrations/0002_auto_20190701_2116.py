# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-01 13:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': '理财产品信息', 'verbose_name_plural': '理财产品信息'},
        ),
        migrations.AlterModelOptions(
            name='productstyle',
            options={'verbose_name': '理财产品类型', 'verbose_name_plural': '理财产品类型'},
        ),
    ]