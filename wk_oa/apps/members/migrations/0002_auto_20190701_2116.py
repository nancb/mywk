# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-01 13:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='members',
            options={'verbose_name': '会员等级', 'verbose_name_plural': '会员等级'},
        ),
    ]
