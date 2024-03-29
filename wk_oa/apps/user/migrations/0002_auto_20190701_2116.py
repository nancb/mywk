# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-01 13:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': '用户回报金额', 'verbose_name_plural': '用户回报金额'},
        ),
        migrations.AlterModelOptions(
            name='card',
            options={'verbose_name': '用户银行卡绑定', 'verbose_name_plural': '用户银行卡绑定'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户信息', 'verbose_name_plural': '用户信息'},
        ),
        migrations.AlterModelOptions(
            name='user_card',
            options={'verbose_name': '用户银行卡关联', 'verbose_name_plural': '用户银行卡关联'},
        ),
        migrations.AlterModelOptions(
            name='user_verify',
            options={'verbose_name': '用户验证关联', 'verbose_name_plural': '用户验证关联'},
        ),
        migrations.AlterModelOptions(
            name='verify',
            options={'verbose_name': '用户身份验证', 'verbose_name_plural': '用户身份验证'},
        ),
    ]
