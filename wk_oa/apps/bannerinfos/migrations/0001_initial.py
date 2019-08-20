# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-29 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255, verbose_name='轮播图地址')),
                ('name', models.CharField(max_length=50, verbose_name='轮播图名称')),
            ],
            options={
                'verbose_name': '轮播图模型',
                'verbose_name_plural': '轮播图模型',
                'db_table': 'wklc_bannerInfo',
            },
        ),
    ]
